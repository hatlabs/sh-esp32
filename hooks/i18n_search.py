"""Give every language edition its own search index.

`mkdocs-static-i18n` merges all editions into one `search/search_index.json`,
and Material resolves that file against `__config.base`, which points at the
site root on every page. Searching from a translated page therefore returns
hits in every other language.

This hook splits the merged index by locale, writes each edition its own copy,
and repoints `__config.base` on the edition's pages at the edition root, which
is the only value Material derives the index URL from.

The i18n plugin builds each language with a nested `build()` call and merges the
index in its own post-build handler, which runs at priority -100. This one runs
after it, and skips the nested builds, where the merged index does not exist yet.
"""

import json
import re
from pathlib import Path

from mkdocs.exceptions import PluginError
from mkdocs.plugins import event_priority

CONFIG_SCRIPT = re.compile(
    r'(<script id="__config" type="application/json">)(.*?)(</script>)', re.S
)


@event_priority(-200)
def on_post_build(config):
    """Split the merged search index into one index per language edition."""
    i18n = config["plugins"].get("i18n")
    if i18n is None or i18n.building:
        return

    index_path = Path(config["site_dir"]) / "search" / "search_index.json"
    if not index_path.exists():
        raise PluginError(f"i18n_search: no merged search index at {index_path}")

    languages = i18n.config.languages
    default = next(lang.locale for lang in languages if lang.default)
    locales = [lang.locale for lang in languages if lang.build and not lang.default]

    index = json.loads(index_path.read_text(encoding="utf-8"))
    editions = {locale: [] for locale in locales}
    default_docs = []
    for doc in index["docs"]:
        locale, _, path = doc["location"].partition("/")
        if locale in editions:
            editions[locale].append({**doc, "location": path})
        else:
            default_docs.append(doc)

    empty = sorted(locale for locale, docs in editions.items() if not docs)
    if empty or not default_docs:
        raise PluginError(
            "i18n_search: no index entries for "
            + ", ".join(empty + ([default] if not default_docs else []))
        )

    stemmers = set(index.get("config", {}).get("lang", []))
    site_dir = Path(config["site_dir"])
    for locale, docs in editions.items():
        edition_index = {
            **index,
            "docs": docs,
            "config": {
                **index["config"],
                "lang": [locale] if locale in stemmers else ["en"],
            },
        }
        target = site_dir / locale / "search" / "search_index.json"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(edition_index), encoding="utf-8")
        _repoint_base(site_dir / locale)

    index["docs"] = default_docs
    index["config"] = {
        **index["config"],
        "lang": [default] if default in stemmers else ["en"],
    }
    index_path.write_text(json.dumps(index), encoding="utf-8")


def _repoint_base(edition_dir):
    """Point `__config.base` at the edition root instead of the site root."""
    for page in edition_dir.rglob("*.html"):
        depth = len(page.parent.relative_to(edition_dir).parts)
        base = "/".join([".."] * depth) if depth else "."

        def rewrite(match):
            settings = json.loads(match.group(2))
            settings["base"] = base
            return match.group(1) + json.dumps(settings) + match.group(3)

        text = page.read_text(encoding="utf-8")
        patched, count = CONFIG_SCRIPT.subn(rewrite, text, count=1)
        if not count:
            raise PluginError(f"i18n_search: no __config script in {page}")
        page.write_text(patched, encoding="utf-8")

#!/usr/bin/env python3
"""Rewrite English anchor fragments in a translation to the translated slugs.

Anchor slugs come from heading text, so a translated heading gets a different
slug and every link pointing at it breaks — including links on pages nobody
touched. Translators leave the English fragment in place; this maps it across.

The mapping is positional: the structure comparison already proves the
translation has the same headings in the same order, so the nth heading of the
English page and the nth heading of the translation are the same heading. That
is stronger than matching on text, which cannot work once the text is in another
language.

Usage: map_anchors.py <site-dir> <lang> [--apply]
Without --apply it only reports what it would change.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HEADING_ID = re.compile(r"<h[1-6] id=\"([^\"]+)\"")
LINK = re.compile(r"\]\(([^)\s]*#[^)\s]+)\)")


def built_ids(site: Path, language: str, page: str) -> list[str]:
    """Heading ids of a built page, in document order.

    The default language has no URL segment of its own — `docs/en/index.md` is
    served at the site root, not under `en/` — so English pages are looked up
    without a prefix.
    """
    stem = page[: -len(".md")]
    stem = "" if stem == "index" else stem.removesuffix("/index")
    prefix = "" if language == "en" else language
    parts = [p for p in (prefix, stem) if p]
    html = site.joinpath(*parts, "index.html")
    if not html.exists():
        raise SystemExit(
            f"No built page for {language}/{page} at {html} — build the site first."
        )
    return HEADING_ID.findall(html.read_text(encoding="utf-8"))


def target_page(link: str, page: str) -> str | None:
    """The markdown page a link points at, relative to the docs root."""
    path, _, _ = link.partition("#")
    if link.startswith(("http://", "https://", "mailto:")):
        return None
    if not path:
        return page
    resolved = (Path(page).parent / path).as_posix()
    resolved = Path(resolved).resolve().relative_to(Path.cwd().resolve()).as_posix()
    return resolved if resolved.endswith(".md") else None


def main() -> int:
    site, language = Path(sys.argv[1]), sys.argv[2]
    apply = "--apply" in sys.argv
    docs = Path("docs")

    english = {
        p.relative_to(docs / "en").as_posix(): built_ids(
            site, "en", p.relative_to(docs / "en").as_posix()
        )
        for p in (docs / "en").rglob("*.md")
    }
    translated = {page: built_ids(site, language, page) for page in english}

    changes, unmapped = [], []
    for page in sorted(english):
        source = docs / language / page
        if not source.exists():
            continue
        text = original = source.read_text(encoding="utf-8")
        for link in set(LINK.findall(text)):
            path, _, fragment = link.partition("#")
            target = target_page(link, page)
            if target is None or target not in english:
                continue
            ids_en, ids_tr = english[target], translated[target]
            if fragment not in ids_en:
                continue
            if len(ids_en) != len(ids_tr):
                unmapped.append(
                    f"{language}/{page} -> {link}: {target} has "
                    f"{len(ids_en)} headings in English, {len(ids_tr)} translated"
                )
                continue
            replacement = ids_tr[ids_en.index(fragment)]
            if replacement != fragment:
                text = text.replace(f"]({link})", f"]({path}#{replacement})")
                changes.append(
                    f"  {language}/{page}\n      {fragment}  ->  {replacement}"
                )
        if text != original:
            if apply:
                source.write_text(text, encoding="utf-8")

    verb = "rewritten" if apply else "to rewrite"
    print(f"{len(changes)} anchors {verb} in docs/{language}.")
    for change in changes:
        print(change)
    if unmapped:
        print(f"\n{len(unmapped)} could not be mapped — structure differs:")
        for problem in unmapped:
            print(f"  {problem}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

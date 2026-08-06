#!/usr/bin/env python3
"""Report which translations are missing or out of date.

A translation records the git blob hash of the English source it was written
against, in its own frontmatter:

    ---
    translated_from: <blob hash of docs/en/<path> at translation time>
    ---

The English page carries nothing, so an English edit needs no ceremony: editing
it changes its content, which changes its hash, which makes every translation of
it report as stale on its own.

Reports; never blocks. Exit status is 0 unless the check itself could not run.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

import yaml

DOCS = Path("docs")
STAMP_KEY = "translated_from"


class _Loader(yaml.SafeLoader):
    """mkdocs.yml carries python/name tags that SafeLoader refuses to parse."""


_Loader.add_multi_constructor("", lambda loader, suffix, node: None)


def configured_languages() -> tuple[str, list[str]]:
    """Return (default language, other languages) from the i18n plugin config."""
    config = yaml.load(Path("mkdocs.yml").read_text(encoding="utf-8"), Loader=_Loader)
    for plugin in config.get("plugins", []):
        if isinstance(plugin, dict) and "i18n" in plugin:
            languages = plugin["i18n"]["languages"]
            default = next(l["locale"] for l in languages if l.get("default"))
            others = [l["locale"] for l in languages if not l.get("default")]
            return default, others
    raise SystemExit("mkdocs.yml has no i18n plugin configuration")


def blob_hash(path: Path) -> str:
    return subprocess.run(
        ["git", "hash-object", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout.strip()


def stamp_of(path: Path) -> str | None:
    """Read translated_from from a page's frontmatter, if it has one."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    front = yaml.safe_load(text[4:end]) or {}
    value = front.get(STAMP_KEY)
    return str(value) if value else None


def english_diff(stamped: str, current: Path) -> str | None:
    """Diff the stamped English blob against the English page as it stands now.

    The current page is compared from the working tree rather than as a stored
    object: `git hash-object` computes a hash without writing the object, so
    diffing two hashes would fail on the side that was never stored.
    """
    blob = subprocess.run(
        ["git", "cat-file", "-p", stamped], capture_output=True, text=True,
    )
    if blob.returncode != 0:
        return None  # stamped blob not in this clone — CI needs fetch-depth: 0
    with tempfile.TemporaryDirectory() as tmp:
        was = Path(tmp) / current.name
        was.write_text(blob.stdout, encoding="utf-8")
        result = subprocess.run(
            ["git", "diff", "--no-index", "--no-color", str(was), str(current)],
            capture_output=True, text=True,
        )
    # --no-index exits 1 when the files differ, which is the expected case.
    # Drop the file headers: they carry a temporary path, and the page is
    # already named in the surrounding report.
    noise = ("diff --git ", "index ", "--- ", "+++ ")
    return "\n".join(
        line for line in result.stdout.splitlines()
        if not line.startswith(noise)
    )


@dataclass
class Entry:
    language: str
    page: str          # path relative to the language directory
    state: str         # missing | unstamped | stale | orphaned | current
    expected: str      # blob hash the translation should record
    diff: str | None = None


def collect(default: str, languages: list[str], want_diff: bool) -> list[Entry]:
    sources = sorted(p for p in (DOCS / default).rglob("*.md"))
    entries: list[Entry] = []
    for source in sources:
        relative = source.relative_to(DOCS / default)
        expected = blob_hash(source)
        for language in languages:
            target = DOCS / language / relative
            if not target.exists():
                entries.append(Entry(language, str(relative), "missing", expected))
                continue
            stamped = stamp_of(target)
            if stamped is None:
                entries.append(Entry(language, str(relative), "unstamped", expected))
            elif stamped == expected:
                entries.append(Entry(language, str(relative), "current", expected))
            else:
                diff = english_diff(stamped, source) if want_diff else None
                entries.append(Entry(language, str(relative), "stale", expected, diff))

    # A translation whose source was deleted is invisible to the loop above,
    # because that walks the sources. It is still a page being served.
    for language in languages:
        root = DOCS / language
        for translation in sorted(root.rglob("*.md")):
            if not (DOCS / default / translation.relative_to(root)).exists():
                entries.append(
                    Entry(language, str(translation.relative_to(root)), "orphaned", "")
                )
    return entries


def render_text(entries: list[Entry]) -> str:
    out = []
    for language in sorted({e.language for e in entries}):
        rows = [e for e in entries if e.language == language]
        counts = {s: sum(1 for e in rows if e.state == s) for s in
                  ("current", "stale", "unstamped", "missing", "orphaned")}
        out.append(f"{language}: " + "  ".join(f"{k}={v}" for k, v in counts.items()))
        for entry in rows:
            if entry.state != "current":
                out.append(f"  {entry.state:9s} {entry.page}")
                if entry.expected:
                    out.append(f"    {STAMP_KEY}: {entry.expected}")
    return "\n".join(out)


def render_markdown(entries: list[Entry], only: set[str] | None) -> str:
    shown = [e for e in entries if only is None or e.page in only]
    out = ["## Translation status", ""]
    for language in sorted({e.language for e in entries}):
        rows = [e for e in entries if e.language == language]
        counts = {s: sum(1 for e in rows if e.state == s) for s in
                  ("current", "stale", "unstamped", "missing", "orphaned")}
        summary = ", ".join(f"{v} {k}" for k, v in counts.items() if v)
        out.append(f"**{language}** — {summary}")
    out.append("")

    behind = [e for e in shown if e.state != "current"]
    if not behind:
        out.append("Every translation of the pages in scope is current.")
        return "\n".join(out)

    out += ["| Language | Page | State | Stamp to record |",
            "|:---|:---|:---|:---|"]
    for entry in behind:
        out.append(f"| {entry.language} | `{entry.page}` | {entry.state} | `{entry.expected}` |")
    out.append("")

    for entry in behind:
        if entry.diff:
            out += [f"<details><summary>English changes since "
                    f"<code>{entry.language}/{entry.page}</code> was translated</summary>",
                    "", "```diff", entry.diff.rstrip(), "```", "", "</details>", ""]
        elif entry.state == "stale":
            out.append(f"<!-- {entry.page}: stamped blob not in this clone; "
                       f"CI needs fetch-depth: 0 -->")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=("text", "markdown"), default="text")
    parser.add_argument("--diff", action="store_true",
                        help="include the English diff for stale pages")
    parser.add_argument("--only-pages", nargs="*", metavar="PATH",
                        help="restrict the detail section to these docs/<lang>/-relative paths")
    args = parser.parse_args()

    default, languages = configured_languages()
    if not languages:
        print("No translation languages configured.")
        return 0

    entries = collect(default, languages, want_diff=args.diff)
    if args.format == "markdown":
        only = set(args.only_pages) if args.only_pages else None
        print(render_markdown(entries, only))
    else:
        print(render_text(entries))
    return 0


if __name__ == "__main__":
    sys.exit(main())

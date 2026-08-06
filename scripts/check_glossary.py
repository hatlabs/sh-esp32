#!/usr/bin/env python3
"""Check that a translation actually uses the terms its glossary prescribes.

A glossary read before translating looks followed afterwards, because rereading
one's own text confirms whatever it already says. Every language branch so far
reached review with a term the glossary defines and the pages ignore — a second
name for the same connector, one page apart, which no reader can reconcile.

The check is indirect but cheap: if a glossary term appears in the English
source and its prescribed translation appears nowhere in the target language,
some other word is doing that job. Run it before opening a pull request.

It finds a term that is never used, not a term that has acquired a rival. German
says both `Spannungsausfall` and `Stromausfall` for *blackout* and passes here,
because the prescribed word does appear. Catching that needs the rival named,
which is what the glossary cannot know in advance.

Exit status is 1 if any prescribed term is unused.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

GLOSSARIES = {
    "fi": "finnish-glossary.md",
}

ROW = re.compile(r"^\| *`?([^|`]+?)`? *\| *`?([^|`]+?)`? *\|")
SHORTEST_TERM = 5
# Below this length a shared substring is more likely a compound than a clash.
BOUNDARY_FROM = 8
# An English term used once may be phrased around; twice is a pattern.
MIN_ENGLISH_USES = 2


def read_pages(directory: Path, only: set[str] | None = None) -> str:
    """Concatenate a language's markdown with code and frontmatter removed.

    `only` restricts the read to a set of paths relative to the directory. The
    English side is read that way so that a page nobody has translated cannot
    make its vocabulary look missing: asking whether a translation uses a
    prescribed term is meaningful only for pages that were translated at all.
    """
    out = []
    for page in sorted(directory.rglob("*.md")):
        if only is not None and page.relative_to(directory).as_posix() not in only:
            continue
        raw = page.read_text(encoding="utf-8")
        text = re.sub(r"^---\n.*?\n---\n", "", raw, flags=re.S)
        text = re.sub(r"```.*?```", " ", text, flags=re.S)
        out.append(re.sub(r"`[^`\n]*`", " ", text))
    return fold("\n".join(out).lower())


def terms(glossary: Path) -> list[tuple[str, str]]:
    """Extract (english, translation) pairs from the glossary tables."""
    pairs = []
    for line in glossary.read_text(encoding="utf-8").splitlines():
        row = ROW.match(line)
        if not row:
            continue
        english, translated = row.group(1).strip(), row.group(2).strip()
        if english.lower().startswith("english") or set(english) <= set(":- "):
            continue
        pairs.append((english, translated))
    return pairs


def fold(text: str) -> str:
    """Flatten the spelling differences that inflection introduces.

    Romance plurals move accents around — `tapón` becomes `tapones`, `imagen`
    becomes `imágenes` — and Italian sets its apostrophe as U+2019 where a
    glossary cell is typed with U+0027. Comparing the letters underneath keeps
    those from reading as a term the pages never used.
    """
    text = text.replace("’", "'").replace("ʼ", "'")
    return "".join(
        c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c)
    )


def alternatives(term: str) -> list[str]:
    """Split a glossary cell into the forms that would each satisfy it."""
    term = re.sub(r"\s*\([^)]*\)", "", term).lower()
    return [part.strip() for part in term.split("/") if part.strip()]


def inflectable(term: str) -> re.Pattern[str]:
    """Match a term in whatever form a sentence needs.

    Every word may take an ending, not just the last one: Finnish inflects both
    halves of `vapaa tila` and French pluralises both halves of `bouchon
    obturateur`, so anchoring on the phrase as written finds neither. A verb
    phrase also takes its object in the middle — `aseta CM5 uudelleen
    paikalleen` — so a couple of words are allowed to intervene.

    The match must start at a word boundary, or a compounding language reports
    a term as used when only a longer word containing it is present: Finnish
    `virtalähde` (power supply) is a substring of `vakiovirtalähde` (constant
    current source), two different components. Without the boundary this check
    returns a false green, which is worse than a false alarm — a checker that
    passes when it should not is no checker at all.

    The boundary only applies when the term starts with a word character. A row
    like `−32 V and +32 V` opens with a minus sign, and `\\b` before a non-word
    character asserts the opposite of what is meant — it would demand a letter
    immediately before the minus and match nothing.

    It also only applies to terms long enough that a shared substring is
    unlikely to be coincidence. A compounding language legitimately puts a short
    common noun at the end of a compound — Danish `pakke` inside `salgspakke`
    and `softwarepakke` is the same concept — so demanding a boundary there
    reports correct prose as a violation. `virtalähde` at ten characters
    appearing only inside `vakiovirtalähde` is a signal; `pakke` at five is not.
    """
    words = [re.escape(w[: max(3, len(w) - 3)]) + r"\w*" for w in fold(term).split()]
    body = r"(?:\W+\w+){0,2}\W+".join(words)
    folded = fold(term)
    long_enough = len(folded.replace(" ", "")) >= BOUNDARY_FROM
    boundary = r"\b" if long_enough and re.match(r"\w", folded) else ""
    return re.compile(boundary + body)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "language", choices=sorted(GLOSSARIES), help="target language code"
    )
    parser.add_argument("--docs", default="docs", help="documentation root")
    parser.add_argument(
        "--glossaries",
        default="solutions/translation",
        help="directory holding the glossaries",
    )
    args = parser.parse_args()

    target = Path(args.docs) / args.language
    done = {p.relative_to(target).as_posix() for p in target.rglob("*.md")}
    english = read_pages(Path(args.docs) / "en", only=done)
    translated = read_pages(target)
    glossary = Path(args.glossaries) / GLOSSARIES[args.language]

    checked, unused = 0, []
    for source, target in terms(glossary):
        wanted, have = alternatives(source), alternatives(target)
        # A row may offer several renderings — `plus (+) / miinus (−)`. Dropping
        # only the ones too short to match reliably would leave the row
        # demanding the survivors, so a page using `plusnapa` and never needing
        # the negative half reads as a violation. If any alternative is too
        # short to judge, the whole row is.
        if not wanted or not have:
            continue
        if min(len(w) for w in wanted + have) < SHORTEST_TERM:
            continue
        uses = sum(english.count(w) for w in wanted)
        if uses < MIN_ENGLISH_USES:
            continue
        checked += 1
        if not any(inflectable(h).search(translated) for h in have):
            unused.append((source, target, uses))

    print(f"Checked {checked} glossary terms against docs/{args.language}.")
    if unused:
        print(f"\n{len(unused)} prescribed but unused — something else took over:\n")
        for source, target, uses in unused:
            print(f"  {source}  ->  {target}   (English {uses}×, translation never)")
        return 1
    print("Every prescribed term is in use.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

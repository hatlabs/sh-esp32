#!/usr/bin/env python3
"""Count the typography rules a translation has to obey, per language.

Written after two naive greps produced only false positives: searching for the
character pair »…« in Norwegian matches the gap *between* two correct «…» pairs,
and searching for a space before a colon matches English comments inside code
fences. Both looked like defects and neither was one.

So quotations are checked by walking the marks in order and requiring them to
alternate open, close, open, close — which is what "the pairs are the right way
round" actually means — and everything is measured with code fences, inline code
and admonition syntax removed first.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Which mark opens a quotation, and which closes it, per language.
QUOTES = {
    "fi": ("”", "”"),  # ”…” — the same character opens and closes
}
# French is the one language that *requires* a space before ; : ! ? — and
# requires it to be unbreakable, so the line never breaks before the mark.
# Everywhere else any space there is an error, which is why this cannot be one
# rule for all: applying the French habit elsewhere is a known leak, and
# applying the majority rule to French would flag every correct sentence.
SPACE_REQUIRED = {"fr"}
PLAIN_SPACE_BEFORE_PUNCT = re.compile(r"\u0020[;:!?]")
# German compounds a multi-word proper name with hyphens throughout —
# NMEA-2000-Netzwerk, Signal-K-Server — and its glossary calls a missing hyphen
# there the most visible marker of a translation done by someone who does not
# write German. Every other language treats that same chain as an error, and a
# hyphen at the *junction* between a product name and a common noun
# (HaLOS-avbilder) is right in the Germanic languages and wrong in the Romance
# ones. One rule cannot serve all three cases, so each is scoped to where its
# glossary asks for it.
HYPHEN_CHAINS = re.compile(r"NMEA-2000|Signal-K|Raspberry-Pi|Compute-Module")
CHAINS_ALLOWED = {"de"}
JUNCTION_HYPHEN = re.compile(
    r"\b(?:HALPI2|HaLOS|NMEA 2000|Signal K|Raspberry Pi|E7T)-"
    r"[a-z\u00e1\u00e9\u00ed\u00f3\u00fa\u00f1\u00e0\u00e8\u00ec\u00f2\u00f9]"
)
JUNCTION_FORBIDDEN = {"es", "it"}
SPACE_BEFORE_PUNCT = re.compile(r"[   ][;:!?]")


def prose(text: str) -> str:
    """The text a reader sees, with everything that is markup taken out.

    Inline code becomes a placeholder rather than nothing: deleting it joins the
    words on either side and manufactures a space before the next punctuation
    mark, which is exactly the false positive this function exists to avoid.
    """
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "\n", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "X", text)
    text = re.sub(r'^!!! \w+ ".*"$', "", text, flags=re.M)  # admonition syntax quotes
    text = re.sub(r"\]\([^)]*\)", "]", text)  # link targets
    # A table's delimiter row carries the column alignment as colons — | ---: |
    # — which reads as a space before a colon and is not prose at all.
    text = re.sub(r"^[|\s:-]+$", "", text, flags=re.M)
    # Repository names and filenames are identifiers that happen to contain
    # hyphens — HALPI2-hardware, HALPI2-schematic_v0.6.1.pdf — and reading them
    # as compounds of the target language invents defects that are not there.
    text = re.sub(r"https?://\S+", "X", text)
    text = re.sub(
        r"\b[\w.-]+\.(?:pdf|zip|png|jpe?g|md|txt|json|ya?ml|step|bin|conf|sock)\b",
        "X",
        text,
    )
    return text


def quotation_faults(text: str, opening: str, closing: str) -> list[str]:
    """Marks must alternate open, close, open, close — and end closed."""
    if opening == closing:
        count = text.count(opening)
        return [] if count % 2 == 0 else [f"odd number of {opening} ({count})"]
    faults, depth = [], 0
    for index, char in enumerate(text):
        if char == opening:
            if depth:
                faults.append(
                    f"{opening} opens while already open: "
                    f"...{text[max(0, index - 40) : index + 20]}..."
                )
            depth += 1
        elif char == closing:
            if not depth:
                faults.append(
                    f"{closing} closes nothing: "
                    f"...{text[max(0, index - 40) : index + 20]}..."
                )
            else:
                depth -= 1
    if depth:
        faults.append(f"{depth} quotation(s) never closed")
    return faults


def main() -> int:
    languages = sys.argv[1:] or sorted(QUOTES)
    worst = 0
    for language in languages:
        opening, closing = QUOTES[language]
        pages = sorted(Path("docs", language).rglob("*.md"))
        quotes = spacing = chains = 0
        problems: list[str] = []
        for page in pages:
            text = prose(page.read_text(encoding="utf-8"))
            for fault in quotation_faults(text, opening, closing):
                quotes += 1
                problems.append(f"    {page}: {fault}")
            rule = (
                PLAIN_SPACE_BEFORE_PUNCT
                if language in SPACE_REQUIRED
                else SPACE_BEFORE_PUNCT
            )
            for match in rule.finditer(text):
                spacing += 1
                wrong = "breakable space" if language in SPACE_REQUIRED else "space"
                problems.append(
                    f"    {page}: {wrong} before '{match.group()[-1]}': "
                    f"...{text[max(0, match.start() - 40):match.end() + 10]}..."
                )
            allowed = language in CHAINS_ALLOWED
            chain_rule = () if allowed else HYPHEN_CHAINS.finditer(text)
            for match in chain_rule:
                chains += 1
                problems.append(
                    f"    {page}: hyphen inside a product name '{match.group()}'"
                )
            if language in JUNCTION_FORBIDDEN:
                for match in JUNCTION_HYPHEN.finditer(text):
                    chains += 1
                    problems.append(
                        f"    {page}: junction hyphen '{match.group()}' "
                        f"— not used in this language"
                    )

        marks = sum(prose(p.read_text(encoding="utf-8")).count(opening) for p in pages)
        status = "ok" if not problems else f"{len(problems)} PROBLEMS"
        print(
            f"{language}: {len(pages)} pages, {marks} quotations "
            f"({opening}…{closing}), quote faults {quotes}, spacing {spacing}, "
            f"hyphen chains {chains} — {status}"
        )
        for problem in problems[:8]:
            print(problem)
        worst = max(worst, len(problems))
    return 1 if worst else 0


if __name__ == "__main__":
    sys.exit(main())

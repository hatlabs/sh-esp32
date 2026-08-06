#!/usr/bin/env python3
"""Verify that every internal anchor in the built site resolves to a real id.

Anchors are generated from heading text, so translating a heading changes its
slug and silently breaks every link pointing at it — including links on pages
that were not touched, which is why this is a delayed fault: a cross-page anchor
keeps working until its *target* page is translated. `mkdocs build --strict`
does not validate anchors at all.

Run against a built site directory. Exit status is 1 if any anchor is broken.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from urllib.parse import unquote, urldefrag

HREF = re.compile(r'href="([^"]+)"')
ID = re.compile(r'\sid="([^"]+)"')


def collect_pages(site: str) -> dict[str, set[str]]:
    """Map each built page to the set of element ids it defines."""
    ids: dict[str, set[str]] = {}
    for root, _, files in os.walk(site):
        for name in files:
            if name.endswith(".html"):
                path = os.path.join(root, name)
                text = open(path, encoding="utf-8").read()
                ids[os.path.realpath(path)] = set(ID.findall(text))
    return ids


def resolve(href: str, page: str, site: str, base: str) -> str | None:
    """Resolve an href to the built file it points at, or None if not ours."""
    target, _ = urldefrag(href)
    target = unquote(target)
    if not target:
        return os.path.realpath(page)
    if target.startswith("/"):
        if not target.startswith(base):
            return None
        path = os.path.normpath(os.path.join(site, target[len(base):]))
    else:
        path = os.path.normpath(os.path.join(os.path.dirname(page), target))
    if not path.endswith(".html"):
        path = os.path.join(path, "index.html")
    return os.path.realpath(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", nargs="?", default="site")
    parser.add_argument("--base", default="/halpi2/",
                        help="path component of site_url, for root-absolute links")
    args = parser.parse_args()

    ids = collect_pages(args.site)
    if not ids:
        # Passing on an empty site would be a false green: the build produced
        # nothing, or the path is wrong, and neither is "all anchors resolve".
        print(f"No built pages found under {args.site!r} — nothing to check.",
              file=sys.stderr)
        return 2

    broken: list[tuple[str, str, str]] = []
    checked = 0

    for page in sorted(ids):
        for href in HREF.findall(open(page, encoding="utf-8").read()):
            if href.startswith(("http://", "https://", "mailto:", "data:")):
                continue
            _, fragment = urldefrag(href)
            if not fragment:
                continue
            target = resolve(href, page, args.site, args.base)
            if target is None:
                continue
            checked += 1
            relative = os.path.relpath(page, args.site)
            if target not in ids:
                broken.append((relative, href, "target page does not exist"))
            elif unquote(fragment) not in ids[target]:
                broken.append((relative, href, "no such anchor on the target page"))

    print(f"Checked {checked} anchor links across {len(ids)} pages.")
    if broken:
        print(f"\n{len(broken)} broken:\n")
        for page, href, why in broken:
            print(f"  {page}\n      -> {href}   ({why})")
        return 1
    print("All anchors resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

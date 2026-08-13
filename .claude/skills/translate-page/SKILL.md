---
name: translate-page
description: Translate a documentation page from docs/en/ into another language and stamp it. Use when asked to translate a page, add a language, or bring a stale translation up to date in this repo.
---

# Translate a documentation page

Translation here is a repeatable operation, not an ad-hoc prompt. The rules below
exist because each of them was broken once and cost real work.

## Inputs

- A page path under `docs/en/`, or a page reported by
  `uv run translation-status` as `missing` or `stale`.
- A target language directory, e.g. `docs/fi/`.

## Before translating

1. **Read the glossary for the target language** —
   `solutions/translation/finnish-glossary.md` for Finnish, and its equivalent
   for other languages. It fixes terminology, unit formatting, address form and
   what stays in English. Follow it exactly.
2. If the page introduces a term the glossary does not cover, **add it to the
   glossary** in the same change. Do not invent a one-off translation: the whole
   point is that the same English term reads the same way on every page.
3. If the page is `stale` rather than `missing`, read the English diff the
   status report prints. Translate the change, not the whole page.

## Translating

The translation lives at the mirrored path — `docs/en/hardware/index.md`
becomes `docs/fi/hardware/index.md`. Only markdown goes under the language
directory; images stay with the English source and are shared.

**Preserve structure exactly.** Same headings, list items, numbered steps,
images, admonitions, table rows, footnotes and code fences, in the same order.

**Never touch:**

- Code fences and their contents, including comments inside them
- Inline code: commands, file paths, hostnames, config keys
- UI strings the reader will see on their own screen in English
- Product, protocol and hardware names
- Image filenames and paths

**Always convert:** units to SI spacing and decimal comma (`0.9A` → `0,9 A`,
`5.5 x 2.1 mm` → `5,5 × 2,1 mm`). This is not optional formatting; it is the
correct way to write the value.

**Two markdown traps** that neither `--strict` nor GitHub's preview catches —
both are documented in `solutions/best-practices/`:

- A blank line before the first item of a list
- Four spaces, not three, for a sub-list under a numbered step

**Never write an `en/` or `fi/` segment into a path inside a page.** The
language comes from which directory the file lives in.

## Anchors

Anchors derive from heading text, so translating a heading changes its slug.
Slugs strip diacritics and lowercase: `Mikä HALMET on?` → `mika-halmet-on`.

Two distinct jobs:

1. **Inside the page you are translating** — rewrite every `](#…)` to the
   translated heading's slug.
2. **In pages you are not touching** — a link like
   `](./operation.md#status-led-indicators)` in an already-translated page keeps
   working until `operation.md` is translated, and breaks the moment it is. This
   is a delayed fault. After translating, run the anchor check across the whole
   built site, not just your page.

Do not guess slugs. Build, then read the real ids out of the generated HTML.

## Stamping

The stamp records the git blob hash of the English source the translation was
written against. Write it with the helper, never by hand:

```bash
uv run stamp-translation docs/fi/hardware/index.md
```

**Stamp only when you have actually translated.** A stamp updated without real
translation work reports green and makes the staleness invisible — that is the
one failure the status check cannot detect, and this skill is where the
discipline lives. If you touched only the target language (fixing wording,
fixing a typo), the English source did not change: leave the stamp alone.

## Adding a language to the site

When a locale is added to `mkdocs.yml`, check the language selector too. The
Material theme caps the open menu at `10rem`, which fits five entries at the
site's font size; the sixth language onward scrolls out of sight behind a
scrollbar that gives no hint anything is below it.

`docs/stylesheets/extra.css` should carry:

```css
.md-select:focus-within .md-select__inner,
.md-select:hover .md-select__inner {
  max-height: min(24rem, 75vh);
}
```

24rem clears thirteen entries; the viewport term keeps the menu on screen on a
short display. The same block is in the HALPI2 and HALMET repositories — keep
the three identical, and add it to any further site that gains a second
language.

Verify by measuring rather than by eye: open the site, read the rule's
`max-height` off the stylesheet, and compare it against the list's natural
height with `.md-select__list.getBoundingClientRect()`. Hovering for a
screenshot is unreliable — the menu often has not opened by the time the frame
is captured.

## Verifying

All four, every time:

```bash
uv run mkdocs build --strict
uv run check-anchors site
uv run translation-status
uv run check-glossary fi
uv run check-typography fi
```

**Leave every anchor fragment in its English form while translating**, then map
them all at once once the language is complete and the site has been built:

```bash
uv run map-anchors site fi          # report
uv run map-anchors site fi --apply  # rewrite
```

The mapping is positional — the nth heading of the English page and the nth
heading of the translation are the same heading — which is why the structure
comparison below has to pass first. Matching on heading text cannot work once
the text is in another language.

**Measure the glossary, do not reread it.** Rereading your own pages confirms
whatever they already say, so the terminology looks consistent right up until a
reviewer finds the same connector under two names on adjacent pages. Every
language so far shipped that mistake, and each time it landed on the last pages
translated, once the glossary had stopped being opened. `check-glossary`
reports terms the glossary prescribes and the pages never use — the signature of
a rival word having quietly taken over.

The same applies to whatever typography rules the glossary sets. Test them
against the text: count the quotation marks and check they pair, count the
spaces before `;:!?`, count the address form. A rule that was read looks
followed.

and a structure comparison against the source:

```bash
python3 - <<'PY'
import re
en = 'docs/en/hardware/index.md'; fi = 'docs/fi/hardware/index.md'
def stats(p):
    t = re.sub(r'^---\n.*?\n---\n', '', open(p, encoding='utf-8').read(), flags=re.S)
    return {k: len(re.findall(v, t, re.M)) for k, v in {
        'headings': r'^#{1,6} ', 'bullets': r'^\s*[-*] ', 'numbered': r'^\s*\d+\. ',
        'images': r'!\[', 'admonitions': r'^!!! ', 'table rows': r'^\|',
        'fences': r'^```'}.items()}
a, b = stats(en), stats(fi)
print(a); print(b); print('match' if a == b else 'MISMATCH')
PY
```

A mismatch means content was dropped or merged. Find it before committing.

Finally, confirm no numeric value drifted: every number in the English text
should appear in the translation, unless it was deliberately spelled out as a
word. A wrong voltage or current in an installation guide is a safety problem,
not a typo.

## Committing

One commit per logical group of pages. If pages cross-link each other, translate
and commit them together — otherwise the intermediate commit has links pointing
at headings that do not exist yet.

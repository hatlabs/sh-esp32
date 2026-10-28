# SH-ESP32 Quick Start Guide

The printed leaflet that ships with the SH-ESP32, written in [Typst](https://typst.app).

## Physical format

One A4 sheet, printed on both sides, makes two guides. The sheet is cut lengthwise down the middle into two identical 105 × 297 mm strips. Each strip is folded twice in a double parallel fold into eight 74.25 × 105 mm portrait panels. Folded, a guide is the same size as an A7 packet.

The strip reads horizontally: 297 mm wide, 105 mm tall, with vertical folds. The front side carries panels F1–F4 left to right. Turned over about its vertical axis, the back side carries B1–B4 left to right as the reader sees them, so each back panel sits behind the front panel in the mirrored position:

```
  front side, reading orientation
  +-----------+-----------+-----------+-----------+
  | F1        | F2        | F3        | F4        |
  | Links     | Warranty, | back      | cover     |
  |           | DoC       | cover     |           |
  +-----------+-----------+-----------+-----------+

  back side, after turning the strip over
  +-----------+-----------+-----------+-----------+
  | B1        | B2        | B3        | B4        |
  | Intro,    | Assembly  | Enclosure | Powering, |
  | Contents  |           |           | Software  |
  +-----------+-----------+-----------+-----------+
    behind F4   behind F3   behind F2   behind F1
```

Folded, F4 is the cover and F3 the back cover, and F1 and F2 face each other inside. The reading order is F4, B1–B4, F1, F2, F3.

On the A4 sheet each strip runs down the page. The front strip is turned counterclockwise, so the cover F4 is at the top of page 1. The back strip on page 2 is turned clockwise, with B1 at the top. Long-edge duplex backs each sheet point (x, y) with (210 mm − x, y), which puts every back panel upright behind its front panel once the strip is turned over.

```
   front side (page 1)          back side (page 2)
  +------------+------------+  +------------+------------+
  | F4 cover   | F4 cover   |  | B1         | B1         |
  +------------+------------+  +------------+------------+
  | F3 back    | F3 back    |  | B2         | B2         |
  +------------+------------+  +------------+------------+
  | F2         | F2         |  | B3         | B3         |
  +------------+------------+  +------------+------------+
  | F1         | F1         |  | B4         | B4         |
  +------------+------------+  +------------+------------+
               ^ cut                        ^ cut
```

Every panel is laid out on its own, so no sentence crosses a fold. Content stays at least 6 mm from every panel edge, which keeps it clear of the printer's unprintable border, the cut and the folds, and absorbs small duplex misregistration. The build fails if a panel's content does not fit.

## Building

Requires Typst 0.15. The fonts in `fonts/` are the only ones used, so the output is the same on every machine.

```
./run build     # build/quickstart.pdf
./run proof     # build/quickstart-proof.pdf, with fold and cut lines
./run labels    # build/quickstart-labels.pdf, panel names and UP arrows only
./run preview   # build/quickstart-1.png (front) and build/quickstart-2.png (back)
```

The document version is the `version` variable at the top of `quickstart.typ`.

## Printing

Print `build/quickstart.pdf` on A4 with these settings:

- duplex, flip on long edge
- 100 % scale (no "fit to page")

Then cut each sheet down the middle. Hold a strip front side up with F1–F4 reading left to right. Fold it in half along the centre line, folding F3 and F4 behind F1 and F2. Then fold the left half over onto the right half, so that F1 and F2 meet face to face. F4 is now on top as the cover, and F3 is on the back.

To check a printer's duplex registration and orientation, print `build/quickstart-labels.pdf` the same way: after cutting and turning a strip over, B1 must be behind F4, B4 behind F1, and every arrow must point up.

## Licenses

IBM Plex Sans and IBM Plex Mono are licensed under the SIL Open Font License 1.1; see `fonts/OFL.txt`.

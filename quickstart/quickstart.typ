// SH-ESP32 Quick Start Guide. README.md describes the sheet, the panel order
// and the folding.

// The source revision, e.g. "2026-10-28 11299c7", which ./run passes in so a
// printed guide can be traced to its source.
#let revision = sys.inputs.at("revision", default: none)
#let guides = sys.inputs.at("guides", default: "false") == "true"
// Replaces every panel with its name and orientation markers, for checking
// the duplex imposition.
#let labels = sys.inputs.at("labels", default: "false") == "true"

#let strip-length = 297mm
#let strip-height = 105mm
#let panel-count = 4
#let panel-width = strip-length / panel-count
#let panel-height = strip-height
// Keeps content clear of the printer's unprintable edge, the centre cut and
// the folds, with room for duplex misregistration.
#let margin = 6mm
#let content-width = panel-width - 2 * margin
#let content-height = panel-height - 2 * margin

#let ink = rgb("#2e2014")
#let band-grey = rgb("#b0b4bd")
#let link-blue = rgb("#2a5ea0")
#let guide-colour = rgb("#e0007a")

#set document(title: "SH-ESP32 Quick Start Guide", author: "Hat Labs Oy")
#set page(paper: "a4", margin: 0pt)
#set text(
  font: "IBM Plex Sans",
  size: 8.5pt,
  fill: ink,
  lang: "en",
  hyphenate: false,
)
#set par(leading: 0.62em, spacing: 0.9em)
// The source text uses straight apostrophes.
#set smartquote(enabled: false)
// Never break the product name at its hyphen.
#show "SH-ESP32": box

#set heading(outlined: false, bookmarked: false)
#show heading: it => block(above: 1.1em, below: 0.75em, text(
  font: "IBM Plex Mono",
  size: 12pt,
  weight: "regular",
  it.body,
))

#let diamond = box(baseline: 0.2pt, polygon(
  stroke: 0.5pt + ink,
  (2.2pt, 0pt),
  (4.4pt, 2.2pt),
  (2.2pt, 4.4pt),
  (0pt, 2.2pt),
))
#set list(marker: diamond, indent: 0.3em, body-indent: 0.6em, spacing: 0.65em)

// A labelled web address. Print readers type the address, so it has no
// scheme, and the monospace face keeps characters such as l and 1 apart.
#let site(name, address) = block(above: 1.1em, below: 1.1em, {
  text(weight: "bold", name)
  linebreak()
  text(font: "IBM Plex Mono", size: 8pt, address)
})

#let email(address) = link("mailto:" + address, text(fill: link-blue, address))

#let label-body(name) = {
  place(top + left, text(size: 10pt)[#(name)TL])
  place(bottom + right, text(size: 10pt)[#(name)BR])
  place(center + horizon, align(center, text(size: 28pt)[↑ \ UP \ #name]))
}

// One panel is an independent block: its content must fit inside the
// margins, otherwise compilation fails instead of text silently spilling
// across a fold.
#let panel(name, body) = block(
  width: panel-width,
  height: panel-height,
  inset: margin,
  if labels { label-body(name) } else {
    context {
      let size = measure(block(width: content-width, body))
      assert(
        size.height <= content-height,
        message: "panel " + name + " overflows by " + repr(size.height - content-height),
      )
      body
    }
  },
)

// Front side.

#let f1 = [
  = Links

  For further information, visit the following sites:

  #site[Hat Labs][hatlabs.fi]
  #site[SH-ESP32 documentation][docs.hatlabs.fi/sh-esp32]
  #site[Discussion board][github.com/hatlabs/discussions]
  #site[SensESP project][signalk.org/SensESP]
]

#let f2 = [
  = Warranty and Support

  The SH-ESP32 comes with a two year manufacturer warranty. If you think your device is defective, contact Hat Labs at #email("info@hatlabs.fi") and we will help you out.

  Support for hardware and software development can only be provided via the discussion board listed under Links.

  = Declaration of Conformity

  SH-ESP32 is in conformity with the relevant European Union harmonisation legislation.
]

#let f3 = {
  align(center + horizon, {
    image("images/hat-labs-logo.svg", height: 16mm)
    v(4mm)
    [Hat Labs Oy \ hatlabs.fi \ #email("info@hatlabs.fi")]
  })
  if revision != none { place(bottom + right, text(size: 6pt, revision)) }
}

#let f4 = {
  block(width: 100%, fill: band-grey, inset: (x: 4mm, y: 3mm), grid(
    columns: (1fr, auto),
    align: top,
    text(size: 15pt, fill: white, top-edge: "cap-height")[SH-ESP32 \ Quick Start \ Guide],
    image("images/hat-labs-logo.svg", height: 10mm),
  ))
  v(1fr)
  image("images/sh-esp32-board.jpg", width: 100%)
}

// Back side.

#let b1 = [
  = Introduction

  Congratulations on your new Sailor Hat with ESP32 (SH-ESP32) marine electronics headwear! SH-ESP32 is a powerful development board for creating sensor and control devices for boats. This leaflet will help you get started with creating new stuff on SH-ESP32.

  = Package Contents

  Check that the package contains the following items:

  - SH-ESP32 v2 board
  - A goodie bag with the following contents:
    - 1 pc 4-pin Phoenix MC compatible terminal block plug for NMEA 2000 I/O
    - 1 pc 2-pin terminal block plug for power input
    - 1 pc 2x20 pin GPIO header
    - 1 pc 2x3 pin power header
]

#let b2 = [
  = Assembly

  To improve enclosure compatibility, the latest board revisions are provided without pre-soldered pin headers along the north edge of the board. You can either solder on the provided headers or solder jumper wires directly on the pin holes.

  To connect the wires to the pluggable screw terminals, open the terminal screws, strip the wire ends, insert the wires, and screw them tight. The standard color coding for the NMEA 2000 wiring is as follows:

  - GND: black
  - 12V: red
  - CANH: w#strong[H]ite
  - CANL: b#strong[L]ue
]

#let b3 = [
  = Enclosure

  When used on a boat, an enclosure is required for environmental and mechanical protection.

  The enclosure should be fitted either with panel connectors or cable glands to take the mechanical strain of the cables and to protect the board from humidity and condensation.

  The board fits a waterproof 100x68x50~mm plastic enclosure. If more than two or three inputs are to be used, a larger enclosure is recommended. Hat Labs online store stocks a number of suitable enclosures, but these can also be found on any online marketplace.

  The board can be mounted in an enclosure using screws, double-sided tape, hot glue or sticker standoffs.
]

#let b4 = [
  = Powering the SH-ESP32

  The SH-ESP32 can be powered using the NMEA 2000 bus or directly from the boat's 12 or 24~V power supply. In the latter case, a fuse must be used to protect the wiring. The amount of current drawn by the SH-ESP32 is small, less than 0.1~A on a 12~V system. The board itself is protected using a self-resetting fuse.

  = Software and Programming

  SH-ESP32 by itself doesn't do anything useful; you have to upload a program to it first.

  The following section contains useful links for getting started with programming the SH-ESP32.
]

// A strip in reading orientation, panels left to right.
#let strip(panels) = stack(dir: ltr, ..panels.pairs().map(((name, body)) => panel(name, body)))

// Long-edge duplex backs sheet point (x, y) with (210 mm − x, y). With the
// front strip turned counterclockwise, that puts the back strip, as read
// after turning it over, turned clockwise.
#let side(angle, panels) = {
  let s = rotate(angle, reflow: true, strip(panels))
  // Rotated, a strip is as wide on the sheet as it is tall when read.
  grid(columns: (strip-height, strip-height), s, s)
}

#set page(foreground: if guides {
  for k in range(1, panel-count) {
    place(top + left, dy: k * panel-width, line(
      length: 2 * strip-height,
      stroke: (paint: guide-colour, thickness: 0.3pt, dash: "dashed"),
    ))
  }
  place(top + left, dx: strip-height, line(
    angle: 90deg,
    length: strip-length,
    stroke: 0.3pt + guide-colour,
  ))
})

#side(-90deg, (F1: f1, F2: f2, F3: f3, F4: f4))
#pagebreak()
#side(90deg, (B1: b1, B2: b2, B3: b3, B4: b4))

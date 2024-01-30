---
layout: default
title: Hardware revisions
nav_order: 120
---

# Hardware revisions

{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Introduction

This page documents different board revisions and provides links to the schematics. Full design file history is available at the [SH-ESP32-hardware GitHub repository](https://github.com/hatlabs/SH-ESP32-hardware).

## Version 0.3.1

First version sold at [hatlabs.fi](https://hatlabs.fi).

Schematics: [SH-ESP32-0.3.1-schema.pdf](assets/SH-ESP32-0.3.1-schema.pdf)

## Version 1.0.0

Changes to 0.3.1:

- Move bypass capacitors further away from the mounting holes
- Fix the erroneous solder jumper silkscreens for GPIOs 1 and 3
- Improve the silkscreen for the 2x3 power connector header
- Change some components according to component availability

Schematics: [SH-ESP32-1.0.0-schema.pdf](assets/SH-ESP32-1.0.0-schema.pdf)


## Version 2.0.0

Changes to 1.0.0:

- Change the power input buck converter to XL1509 for easier part availability
- Instead of the ISO1050 isolated CAN transceiver, use a separate digital isolator and transceiver
- Use Phoenix MC type 3.81 mm pluggable screw terminals for power input and CAN bus connectors. These connectors are mechanically more durable and easier to use than the JST XH type connectors used earlier.
- Connectors and headers are now pre-soldered to the board

Schematics: [SH-ESP32-2.0.0-schema.pdf](assets/SH-ESP32-2.0.0-schema.pdf)

## Version 2.0.1

- Minor part changes to improve part availability

Schematics: [SH-ESP32-2.0.1-schema.pdf](assets/SH-ESP32-2.0.1-schema.pdf)

## Version 2.0.2

- Minor ESD protection improvements
- Minor part changes according to manufacturer part availability

## Version 2.0.3

- Minor part changes according to manufacturer part availability

Schematics: [SH-ESP32-2.0.3-schema.pdf](assets/SH-ESP32-2.0.3-schema.pdf)

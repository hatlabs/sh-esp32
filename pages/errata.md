---
layout: default
title: Errata
nav_order: 45
---


# Errata

This page lists all known hardware bugs for different SH-ESP32 revisions.

## Silkscreen issues

### Solder jumper labels for GPIOs 1 and 3 

The silkscreen markings for the bottom side solder jumpers for GPIO pins 1 and 3 are incorrect.
The solder jumpers for the TXD0 and RXD0 pins used for USB serial communication are labeled 3 and 34 but should be 1 and 3 instead.

![Jumpers, bottom]({{site.baseurl}}/media/sh-esp32_r0.3.1_bottom_jumpers_errata_1_3.jpg "SH-ESP32 GPIO 1 and 3 silkscreen errata")
*Solder jumper labels 3 and 34 in the encircled region should be labeled 1 and 3 instead.*

Affects boards up to revision 0.3.1.

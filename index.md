---
layout: default
title: Home
nav_order: 1
description: "Sailor Hat with ESP32 is a powerful microcontroller development board for the marine environment."
permalink: /
---

# Introduction

Sailor Hat with ESP32 (SH-ESP32) is a powerful microcontroller development board for the marine environment.

![SH-ESP32 top]({{site.baseurl}}/media/sh-esp32_r2.0.0_top_render.jpg "SH-ESP32 Rev. 2 top view")
<a name="fig_top_view"></a>*SH-ESP32 Rev. 2 top view.*

With SH-ESP32 you can easily create all kinds of sensors and control interfaces for your boat.
Examples include RPM or fuel and water tank level meters, bilge alarms, chain counters, electrical compasses, attitude sensors, and so on.
Control interface examples include automatic engine room blower control, smart light switching, or smart fridge thermostats.
It integrates easily both to [Signal K](https://signalk.org/) as well as NMEA 2000 and can be used as a NMEA 2000 gateway device.

SH-ESP32 can be plugged directly to any 12V or 24V power system.
Special emphasis has been placed on electrical compliance: the board can handle most power surges present on an automotive or marine 12V or 24V power system.
Equally importantly, the inputs and outputs have protection for electrostatic discharges (static electricity), and are designed to not produce electromagnetic emissions (disturb other sensitive devices such as VHF radios or GPS antennas), and to be protected against electromagnetic interference (will not be disturbed by a VHF, SSB, or a radar).

SH-ESP32 is open hardware, licensed under the Creative Commons Attribution-ShareAlike 4.0 International license.
You can create your own SH-ESP32 derivatives as long as you share them under similar terms!

## Getting the hardware

Ready-made CE-certified SH-ESP32 boards can be purchased from [Hat Labs Ltd](https://hatlabs.fi).
All design files are also available at the [SH-ESP32 hardware GitHub repository](https://github.com/hatlabs/sh-esp32-hardware/).

## NMEA 2000 compatibility

SH-ESP32 is open hardware and the provided and suggested software are open source under liberal software and hardware licenses. NMEA 2000 is a proprietary standard by National Marine Electronics Association (NMEA). The licensing and certification processes of NMEA are fundamentally incompatible with open source development, and while several references to NMEA 2000 are made in this documentation, the products of Hat Labs Ltd are not, and will not be certified by NMEA.

However, a lot of effort, both in the lab and in the real-world environment, has been put into ensuring that SH-ESP32 is electrically compatible with NMEA 2000, and that the supplied example software are compatible with NMEA 2000 communication protocol.

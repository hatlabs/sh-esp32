# Introduction

Sailor Hat with ESP32 (SH-ESP32) is a powerful microcontroller development board for marine environments.

With SH-ESP32 you can easily create all kinds of sensors and control interfaces for your boat. Examples include RPM or fuel and water tank level meters, bilge alarms, chain counters, electrical compasses, attitude sensors, and so on. Control interface examples include automatic engine room blower control, smart light switching, or smart fridge thermostats. It integrates easily both to [Signal K](https://signalk.org/) as well as NMEA 2000 and can be used as a NMEA 2000 gateway device.

SH-ESP32 can be plugged directly to any 12V or 24V power system. Special emphasis has been placed on electrical compliance: the board can handle most power surges present on an automotive or marine 12V or 24V power system. Equally importantly, the inputs and outputs have protection for electrostatic discharges (static electricity), and are designed to not produce electromagnetic emissions (disturb other sensitive devices such as VHF radios or GPS antennas), and to be protected against electromagnetic interference (will not be disturbed by a VHF, SSB, or a radar).

SH-ESP32 is open hardware, licensed under the Creative Commons Attribution-ShareAlike 4.0 International license. You can create your own SH-ESP32 derivatives as long as you share them under similar terms!

# Getting the hardware

Ready-made CE-certified SH-ESP32 boards can be purchased from [Hat Labs Ltd](https://hatlabs.fi). All design files are also available at the [SH-ESP32 hardware GitHub repository](https://github.com/hatlabs/sh-esp32-hardware/).

# Assembling the hardware


# Enclosures


# Hardware description

## ESP32 module

## Power supply

## Peripherals

### Buttons and LEDs

### USB

### CAN bus (NMEA 2000)

### I2C

### 1-Wire

### Optocoupler input and output

### GPIO header

### Proto board area

# Software

## Required drivers

## SDKs

## Pinouts of peripherals

## Application frameworks

### SensESP

# Add-on boards
# Acknowledgments

Matti Airas, the Mad Hatter and founder of Hat Labs Ltd, has initiated the project and done most of the initial hardware development and testing. Mark Farnan has done major contributions and hardware design improvements, including all add-on board designs. Karl-Erik Gustafsson has provided a lot of invaluable guidance, especially regarding electromagnetic compatibility design.

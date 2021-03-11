# Introduction

Sailor Hat with ESP32 (SH-ESP32) is a powerful microcontroller development board for marine environments.

With SH-ESP32 you can easily create all kinds of sensors and control interfaces for your boat.
Examples include RPM or fuel and water tank level meters, bilge alarms, chain counters, electrical compasses, attitude sensors, and so on.
Control interface examples include automatic engine room blower control, smart light switching, or smart fridge thermostats.
It integrates easily both to [Signal K](https://signalk.org/) as well as NMEA 2000 and can be used as a NMEA 2000 gateway device.

SH-ESP32 can be plugged directly to any 12V or 24V power system. 
Special emphasis has been placed on electrical compliance: the board can handle most power surges present on an automotive or marine 12V or 24V power system.
Equally importantly, the inputs and outputs have protection for electrostatic discharges (static electricity), and are designed to not produce electromagnetic emissions (disturb other sensitive devices such as VHF radios or GPS antennas), and to be protected against electromagnetic interference (will not be disturbed by a VHF, SSB, or a radar).

SH-ESP32 is open hardware, licensed under the Creative Commons Attribution-ShareAlike 4.0 International license.
You can create your own SH-ESP32 derivatives as long as you share them under similar terms!

# Getting the hardware

Ready-made CE-certified SH-ESP32 boards can be purchased from [Hat Labs Ltd](https://hatlabs.fi).
All design files are also available at the [SH-ESP32 hardware GitHub repository](https://github.com/hatlabs/sh-esp32-hardware/).

# Assembling the hardware

The SH-ESP32 boards sold by Hat Labs are mostly unassembled.
Only the USB connector has been soldered on at delivery.
You need to solder on the remaining connectors, or at least the ones you need.
A set of connectors is provided in the sales package.
Depending on your requirements, you may want to swap them for something else.
For example, the power and CAN bus connectors can be replaced with 2.5 mm pluggable terminal blocks that permit easier disconnection of individual wires and is mechanically sturdier.
Similarly, male headers may be replaced with female ones to allow plugging in devices with compatible male headers.

To assemble the connectors, a soldering iron and some solder is required.
It is highly recommended to use an iron with controllable temperature.
Flux can also be helpful.
SH-ESP32 has ground plane on up to three of the four PCB layers.
They conduct heat efficiently away from the solder joint -- to solder the connectors, use as large solder tip as you can easily work with.
It also helps to set the iron temperature somewhat higher than usually; 370°C or 700°F is a good starting point.

To solder the connectors, place them on the board one by one and use some tape to hold them in place when you turn the PCB around for soldering.
Touch both the pin and the pad with the iron tip and then feed some solder wire to the opposite side of the pin.
The whole process should ideally take only a couple of seconds, although in practice some fumbling is normal.
Try avoiding heating the pins too long, though -- the plastic connector or header body will melt and the pin will become crooked.
Tiny deformation is not dangerous, though, as long as it doesn't prevent you from plugging the connector to the header.
A bit of solder on the iron tip is OK for helping with heat transfer, but if you add a big blob of solder onto the tip, all flux burns off and the solder becomes difficult to work with.
In that case it's better to wipe the tip clean and apply some fresh solder.
For stubborn pins add a generous amount of flux.
It helps the solder flow more easily.

TODO: Add illustration

# Enclosures

Boats can be nasty environments for electronics; there's salt water, high humidity, and often some condensation, too.
It is highly recommended to keep the SH-ESP32 in an enclosure in "production".
The board has been designed to fit in an 100x68x50 mm plastic waterproof enclosure, available either at the Hat Labs web store, or at any online marketplace such as Amazon, Ebay, or AliExpress.

TODO: Add a photo of the standard enclosure

## Mounting the board

There is some slight variation in the location of the plastic standoffs on generic enclosures, so you might have to get creative when mounting the board.
Plastic adhesive standoffs (3 mm hole size, height 6 mm or less, available online) allow you to mount the board easily in any kind of an enclosure.

TODO: Add a photo of the adhesive standoffs.

## Drilling holes

The enclosures don't have any pre-drilled holes for connectors or wire glands on them.
At a very minimum, you need one hole for power or NMEA 2000 input.
Usually you want some more, though, to connect external sensors or wiring.

To drill the holes in the thin plastic, a step drill bit (one that looks like a small metal Christmas tree) is recommended. 
Standard metal drill bits may easily bite too hard and crack the plastic.
If you don't have a step drill bit at hand, use standard metal bits.
Start with a small diameter and increase the diameter with small increments to limit the risk of cracking the case.

Plan your hole placement in advance.
If you only need a couple of holes, placing them on the short side may result in the neatest outcome.
If you need three or more connectors, place them on the long side or on both ends.
Nothing prevents you from adding connectors on the lid, either.
If there is even the slightest possibility of condensation or deck leaks or any other water drops near the planned installation location, try to have the connectors leave the enclosure downwards.
This should prevent any water ingress even if the connectors weren't perfectly tight.

When placing the holes horizontally, make sure that the connector nut will clear both the enclosure corner bumps and the nut of any adjacent connector. Vertically, the connector should be as high as reasonable. This will help the connector clear any headers or components on the PCB.
The hole edge could be 4-5 mm or 3/16" from the lid seam.
When using PG9 cable glands, the hole might have to be even closer to the lid.
Drill carefully!

Suitable hole size for different connectors:

- SMA (WiFi antenna): 6.5-7 mm or 1/4"
- PG7 cable gland and M12 (NMEA 2000) panel connector: 12 mm or 1/2"
- SP13 panel connectors (blue-black plastic connectors): 13-14 mm.
  1/2" probably works with a bit of wiggling.
- PG9 cable gland: 16 mm or 5/8"

TODO: Illustrations

## Soldering the panel connectors

When soldering the internal wires to the panel connectors, always use heat shrink tube on the individual wires.
Always remember to slide the heat shrink on the wires _before_ soldering...
When soldering the panel connectors, the general guidance given in Section FIXME applies.
Usually you can first add solder to the connector pin cavity and then re-melt the solder and insert the wire.

# Hardware description

TODO: Add an image with annotations for the different functional blocks

TODO: Add an image with annotations for the different connectors

TODO: Add an image with annotations for the solder jumpers and 0R resistors

## ESP32 module

- Describe and provide links to ESP-WROOM-32
## Power supply

- Describe the characteristics of the power supply

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

- CH340C driver for Windows and Mac (Linux works as is)

## SDKs

- Espressif
- Arduino Framework

## Pinouts of peripherals

- Describe silkscreen symbols
- List pinouts

## Application frameworks

- Describe options other than SensESP

### SensESP

- Describe SensESP

# Add-on boards

* Describe Proto Board Top Hat
* Describe other planned boards
  * Digital switching
  * Ethernet

# Acknowledgments

Matti Airas, the Mad Hatter and founder of Hat Labs Ltd, has initiated the project and done most of the initial hardware development and testing. Mark Farnan has done major contributions and hardware design improvements, including all add-on board designs. Karl-Erik Gustafsson has provided a lot of invaluable guidance, especially regarding electromagnetic compatibility design.

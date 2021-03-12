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

## Tour around the board

The different functional blocks of SH-ESP32 are shown in [Figure 1](#fig_functional_blocks).
They are described below.

1. **The ESP32-WROOM-32 module**: 
   The ESP32 microcontroller module is the heart of the device.
   It contains the two-core microcontroller with integrated RAM, a flash chip, and a WiFi/Bluetooth antenna (or, in the case of SH-ESP32-ufl, a U.FL connector for the antenna).

2. **Power supply**:
   SH-ESP32 has an integrated switching mode power supply that converts input voltages between 8V and 32V to the 3.3V voltage used on the board. 
   The power supply also includes a self-resetting 500 mA polyfuse, reverse polarity protection, and surge protection.

3. **CAN bus transceiver**:
   SH-ESP32 includes an isolated CAN transceiver that conforms to the NMEA 2000 specification.
   The CAN bus circuitry also includes protection similar to the main power supply and a 5V linear regulator to power the transceiver independently from the NMEA 2000 bus.

4. **Optocoupler input and output**:
   Optocoupler I/O can be used to connect the SH-ESP32 safely to noisy external inputs or outputs such as the alternator signal or relays. 
   
5. **I2C and 1-Wire I/O**:
   SH-ESP32 supports 1-Wire and I2C on separate 2.54 mm headers.
   Additionally, there is an unpopulated footprint for a Qwiic compatible JST SH connector.
   Both interfaces are ESD protected and have noise filtering.

6. **USB interface**:
   SH-ESP32 has a USB 2.0 compatible Micro B connector and interface.
   When connected to a host computer, the board is visible as a USB serial device.
   The USB interface can be used for powering the board, flashing the ESP32 module, and for communicating with the device using a serial protocol.

7. **User interface**:
   There are two buttons and two leds integrated on the board.
   The reset button resets the board.
   The boot button can be used to force the ESP32 into a flashing mode, and otherwise is usable as a generic button input on GPIO0.
   The red LED is hard-wired to the 3.3V power, indicating that the device is powered, while the blue LED is connected to GPIO2 and can be controlled by the program.

![Functional blocks](media/sh-esp32_r0.3.1_top_func_annotated.jpg "Functional blocks of SH-ESP32")
<a name="fig_functional_blocks"></a>*Figure 1. Functional blocks of SH-ESP32.*

## Connectors

[Figure 2](#fig_connectors) illustrates the different connectors on the SH-ESP32.
The connectors are as follows:

1. **Power connector**:
   A JST XH compatible power connector.
   A 2.5 mm terminal block can be fitted on the same footprint.

2. **CAN bus connector**:
   A 4-pin JST XH connector designed to be connected to a standard NMEA 2000 compatible DeviceNet M12 connector on the enclosure.
   This connector can also be replaced with a 2.5 mm terminal block if so desired.

3. **Optocoupler I/O header**:
   Optocoupler input and output can be provided via this interface.

4. **1-Wire header**:
   1-Wire interface fitted with ESD protection and noise filtering as well as low-pass filtering required for longer networks.
   1-Wire is commonly used for temperature sensors and similar simple sensing devices.
   It is a relatively slow interface but allows for long networks.

5. **I2C header**:
   I2C (Inter-Integrated Circuit) is a very popular synchronous serial communication bus commonly used for interfacing with a number of different ICs.
   Maximum bus distances depend on the load, but should be less than 3-4 m, preferably
   much less than that.

6. **USB**:
   This is your standard USB Micro B connector.

7. **Protected Voltage**:
   These header pads can be used to output input voltage that has been reverse polarity and surge protected.
   Observe the polarity: it is opposite of the nearby power input connector.

8. **Voltage link**:
   If you intend to power the board using the NMEA 2000 interface and don't need galvanic connections to external systems, you can connect these pads together to route the power from the CAN bus connector to the main power supply.

9. **Proto board area**:
   This area can be used for your custom modifications.
   
10. **Additional voltage output**:
    Use these pads to get additional 3.3V voltage output for any modifications you need.

11. **GPIO header**:
    The GPIO header provides connections to all GPIO pins available on the ESP32 module.
    Some of the pins are by default used by other peripherals and need to be enabled
    using the solder jumpers.

![Connectors](media/sh-esp32_r0.3.1_top_conx_annotated.jpg "SH-ESP32 connectors")
<a name="fig_connectors"></a>*Figure 2. SH-ESP32 connectors.*

## ESP32 module

ESP32 is a series of low-cost, low-power microcontrollers and microcontroller modules created and developed by Espressif Systems, a Shanghai-based Chinese company. 
The ESP32-WROOM-32 module is built around a powerful dual-core Tensilica Xtensa LX6 microprocessor and features integrated WiFi, dual-mode Bluetooth, and a remarkable amount of peripherals.

The SH-ESP32 features an ESP32-WROOM-32E module with an integrated PCB antenna, while the SH-ESP32-ufl uses ESP32-WROOM-32U that has an U.FL connector for an external antenna.

For more information, visit the [ESP32 Wikipedia article](https://en.wikipedia.org/wiki/ESP32), [Espressif's product pages](https://www.espressif.com/en/products/modules/esp32), or read the [module datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf).

## Power supply

SH-ESP32 is designed to be used on a boat as easily as possible and includes an 8-32 V switching mode power supply with a maximum efficiency of nearly 90%. The power supply has a 3.3 V output with sufficient output current capability for powering both the ESP32 peak power consumption and any reasonable add-ons.

The power supply includes a self-resetting 500 mA polyfuse, reverse polarity protection, and a hefty TVS protection diode that has a breakdown voltage of 36.7-40.6V and maximum peak pulse dissipation capacity in excess of 600W.
Additionally, the power supply includes EMC filtering, designed to keep the conducted emissions of the switching-mode power supply below the regulatory limits.

The switcher IC is Silergy SY8401 that has a wide input range of 4.5-60 V and a maximum output current of 0.8 A.

## Peripherals

### Buttons and LEDs

There are two buttons and two LEDs on the SH-ESP32. The two buttons are labeled Reset and Boot. The Reset button resets the board by pulling the ESP32 Enable pin low.
The Boot button is connected to GPIO0 and can be used during device startup to force the module into a download mode. Otherwise it can be used as a regular button input.

The two LEDs are not explicitly labeled.
The red LED is lit whenever there is 3.3V power on the board.
The blue LED is connected to GPIO2 (the pin commonly used for LED on ESP32 development boards).
It can be controlled by user programs to indicate the state of the device.

### USB

The USB interface can be used to reprogram the ESP32 module and to communicate with the user application. It also powers the board when plugged in. The board can be safely powered using the main power connector and USB simultaneously -- rectifying diodes ensure that only the highest voltage supply is used.

The USB interface is implemented using a low-cost CH340C USB to serial interface chip.
It emulates a standard serial interface with bit rates of up to 2 Mbps.

CH340 chips are natively supported by Linux kernels but require a driver on Mac and Windows.
The driver can be downloaded from the [manufacturer website](http://www.wch-ic.com/downloads/CH341SER_ZIP.html).

### CAN bus (NMEA 2000)

NMEA 2000 is a ubiquitous communications standard used for connecting sensor, control, and display devices on boats and ships.
It is based on the Controller Area Network (CAN bus) which is a vehicle bus standard designed to allow devices to communicate with each other without a host computer.

SH-ESP32 includes an isolated CAN bus interface that allows safe and NMEA 2000 compliant interconnection of devices.
The CAN bus interface can be used to directly output sensor readings to the NMEA 2000 network, or to build NMEA 2000 gateways or similar devices.

The CAN interface uses ESP32's integrated CAN controller and the ISO1050DUB isolated CAN transceiver by Texas Instruments. It features support for high isolation voltages and transients, and bit rates of up to 1 Mbps.

The CAN bus interface can also be used to power the whole device if there are no galvanic connections to other external systems. (FIXME: Needs a more thorough description and illustration.)

### I2C

### 1-Wire

### <a name="opto_io"></a>Optocoupler input and output

The absolute maximum voltage for the optocoupler input is 18V but it can be extended by adding an additional current-limiting resistor in series to the input.
   It is possible to drive small automotive relays using the optocoupler output.
   Additionally
   

### GPIO header

### Proto board area

## Pinouts of peripherals

- Describe silkscreen symbols
- List pinouts

### Customizing GPIO assignments



![Jumpers, top](media/sh-esp32_r0.3.1_top_jumpers_annotated.jpg "SH-ESP32 jumpers on top side")

![Jumpers, bottom](media/sh-esp32_r0.3.1_bottom_jumpers_annotated.jpg "SH-ESP32 jumpers on bottom side")



# Software

## Required drivers

- CH340C driver for Windows and Mac (Linux works as is)

## SDKs

- Espressif
- Arduino Framework

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

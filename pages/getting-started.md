---
layout: default
title: Getting Started
nav_order: 20
---

# Getting started
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

## Assembling the hardware

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

To solder the connectors, place them on the board one by one and use some tape to hold them in place when you turn the PCB around for soldering. Male header pins can be pushed through the tape for even easier manipulation.

Touch both the pin and the pad with the iron tip and then feed some solder wire to the opposite side of the pin, as shown in the figures below.
The whole process should ideally take only a couple of seconds, although in practice some fumbling is normal.
Try avoiding heating the pins too long, though -- the plastic connector or header body will melt and the pin will become crooked.
Tiny deformation is not dangerous, though, as long as it doesn't prevent you from plugging the connector to the header.

![Solder iron tip against pin and pad]({{site.baseurl}}/media/soldering_guide_1.jpg "Solder iron tip against pin and pad"){:width="50%"}\\
<a name="fig_solder_tip_pads"></a>*Heat the pins and the pads with the solder tip.*

![Feed solder wire from the opposite side]({{site.baseurl}}/media/soldering_guide_2.jpg "Feed solder wire from the opposite side"){:width="50%"}\\
<a name="fig_feed_solder"></a>*Feed solder to the pins and the pads, not the iron tip. Although, to be fair, a tiny bit of solder on the tip may help conducting heat...*


A bit of solder on the iron tip is OK for helping with heat transfer, but if you add a big blob of solder onto the tip, all flux burns off and the solder becomes difficult to work with.
In that case it's better to wipe the tip clean and apply some fresh solder.
For stubborn pins add a generous amount of flux.
It helps the solder flow more easily.

The end result should be as shown in the following figure.

![Well-soldered pins]({{site.baseurl}}/media/soldering_guide_3.jpg "Well-soldered pins"){:width="50%"}\\
<a name="fig_well_soldered_pins"></a>*An example of well soldered pins.*

## Enclosures

Boats can be nasty environments for electronics; there's salt water, high humidity, and often some condensation, too.
It is highly recommended to keep the SH-ESP32 in an enclosure in "production".
The board has been designed to fit in a 100x68x50 mm plastic waterproof enclosure as shown in the figure below, available either at the Hat Labs web store, or at any online marketplace such as Amazon, Ebay, or AliExpress.

![Standard enclosure]({{site.baseurl}}/media/enclosure.jpg "Standard enclosure"){:width="50%"}\\
<a name="fig_enclosure"></a>*SH-ESP32 standard enclosure.*

### Mounting the board

There is some slight variation in the location of the plastic standoffs on generic enclosures, so you might have to get creative when mounting the board.
Plastic adhesive standoffs (3 mm hole size, height 6 mm or less, available online) such as the ones shown below, allow you to mount the board easily in any kind of an enclosure.

![Adhesive PCB standoffs]({{site.baseurl}}/media/adhesive_pcb_standoffs.jpg "Adhesive PCB standoffs"){:width="50%"}\\
<a name="fig_standoffs"></a>*Adhesive standoffs.*

### Drilling holes

The enclosures don't have any pre-drilled holes for connectors or wire glands on them.
At a very minimum, you need one hole for power or NMEA 2000 input.
Usually you want some more, though, to connect external sensors or wiring.

To drill the holes in the thin plastic, a step drill bit (one that looks like a small metal Christmas tree), is recommended. 
Standard metal drill bits may easily bite too hard and crack the plastic.
If you don't have a step drill bit at hand, use standard metal bits.
Start with a small diameter and increase the diameter with small increments to limit the risk of cracking the case.

![Step drill bit]({{site.baseurl}}/media/step_drill_bit.jpg "Step drill bit"){:width="50%"}\\
<a name="fig_step_drill_bit"></a>*An example of step drill bits.* 

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

### Soldering the panel connectors

When soldering the internal wires to the panel connectors, always use heat shrink tube on the individual wires.
Always remember to slide the heat shrink on the wires _before_ soldering...
When soldering the panel connectors, the general guidance given in Section FIXME applies.
Usually you can first add solder to the connector pin cavity and then re-melt the solder and insert the wire.

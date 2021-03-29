---
layout: default
title: Software
nav_order: 40
---




# Software

There are a lot of options for languages and environments for writing software for SH-ESP32. If you don't know where to start, using Visual Studio Code and PlatformIO and SensESP are the recommended choices, but depending on your needs and preferences, you might want to try other options as well.

## SDKs

There are multiple Software Development Kits (SDKs) available for the ESP32 environment. All of these are compatible with the SH-ESP32.

[Espressif SDK](https://www.espressif.com/en/products/software/esp-sdk/overview) is the official C++ programming environment.
It has a C style API that does not rely on classes or objects.
It also exposes FreeRTOS, the underlying Real-time Operating System directly.
As the official development environment, Espressif SDK provides the most complete access to ESP32 functionality.

Espressif SDK uses CMake as its build system.

[Arduino Core for ESP32](https://github.com/espressif/arduino-esp32) is an Arduino SDK for the ESP32.
It is also maintained by Espressif and, thanks to the breadth of the Arduino ecosystem and related documentation, is probably the most widely used SDK for ESP32.

The Arduino Core can be used either with [Arduino IDE](https://www.arduino.cc/en/software),  or [PlatformIO](https://platformio.org/).

Arduino IDE is a beginner-friendly software development environment originally developed for the Arduino brand hobbyist developer boards.
It is very easy to start with but the editor is ill-suited for more serious software development, and it also has inherent limits in library and environment management.
Also, it uses its own build system and project layout which is incompatible with other systems.
It is a good choice for very simple single-purpose sketches, but for more complex projects or integrating with e.g. Signal K or other server protocol, look further.

PlatformIO is a cross-platform development environment for different microcontrollers.
It can be used purely on the command line but also integrates well into Visual Studio Code, which is an excellent multi-language code editor and development environment. PlatformIO performs library management and dependency resolution and also includes support for hardware debuggers and more.

If you want to develop the SH-ESP32 using higher-level languages, [MicroPython](https://micropython.org/) is a good choice.
It provides high compatibility with normal Python while running on the FreeRTOS. There are ready-made modules for many ESP32 subsystems and peripherals.

[NodeMCU](https://nodemcu.readthedocs.io/en/dev-esp32/) is a yet another SDK available for the ESP32. NodeMCU is based on lua, which is a lightweight programming language designed primarily for embedded use in applications. NodeMCU was previously popular in ESP8266 development but has since become eclipsed by the more popular programming environments.

[Rust](https://github.com/MabezDev/rust-xtensa) is yet another programming language choice for the Espressif microcontrollers.
Rust is a modern language that has excellent features for systems programming but the ESP32 support is still under heavy development and the documentation is lacking.

## Application frameworks

When you start developing your C or C++ application for integrating onto Signal K or NMEA 2000, it usually pays off to use some existing library or framework as a stepping stone.
As of now (March 2021), the two prime candidates are [SensESP](https://github.com/SignalK/SensESP) and [ESPHome](https://esphome.io). 
SensESP, described in the subsection below, is a set of libraries designed to easily integrate sensor devices into the Signal K system but has a lot of features for general purpose embedded development as well. 
ESPHome is a system designed to control ESP devices using simple configuration files and has good integration to multiple home automation platforms.

### SensESP

[SensESP](https://github.com/SignalK/SensESP) is a sensor development platform for ESP8266 and ESP32 that can be used as a high-level toolkit for creating hardware devices interfacing with Signal K servers. 
It can be easily integrated with NMEA 2000 networks and has a lot of helpful features for asynchronous embedded programming, such as extensive use of the consumer-producer pattern and high level concepts of Sensors, Translations and Consumers (Outputs).

# Add-on boards

There are several add-on boards available or being developed for the SH-ESP32.

Proto Board Top HAT is a add-on board the size of SH-ESP32 that plugs onto it and provides ample area for user customizations. 
It is available for purchase at the [Hat Labs store](https://hatlabs.fi/product/sh-esp32-protoboard-tophat/). 
The design files are available at the [SH-ESP32 hardware repository](https://github.com/hatlabs/SH-ESP32-hardware/tree/main/SH-ESP-HAT-Proto).

Several other hats such as a digital switching [PowerFET HAT](https://github.com/markfarnan/yacht_hardware/tree/main/SH-ESP32-PowerFET) or an [Ethernet HAT](https://github.com/markfarnan/SH-ESP32-Ethernet) are under development.

If you want to develop your own SH-ESP32 hat, a [blank hat template](https://github.com/hatlabs/SH-ESP32-hardware/tree/main/SH-ESP-HAT-Blank) is available at the SH-ESP32 repository.


****It's a work in progress not usable at the moment****


# ChironKlipperTFT

UART compatibility bridge for the Anycubic Chiron TFT running on top of Klipper + Moonraker.

## Features

- Stock Chiron TFT support
- Klipper integration
- Moonraker websocket backend
- Virtual SD support
- Macro launcher support
- Heartbeat emulation
- Firmware restart handling
- AsyncIO architecture
- Marlin protocol emulation

## Supported Hardware

- Anycubic Chiron TFT
- Raspberry Pi
- UART serial connection

## Wiring

Pi TX -> TFT RX
Pi RX -> TFT TX
Pi GND -> TFT GND

115200 baud.

## Installation

```bash
git clone https://github.com/vincent77715/ChironKlipperTFT.git
cd ChironKlipperTFT
./install.sh

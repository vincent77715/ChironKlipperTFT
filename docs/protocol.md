# Chiron TFT Protocol

## Packet Structure

[HEADER][COMMAND][LENGTH][PAYLOAD][CHECKSUM]

## Header

0xA5

## Timing Requirements

Heartbeat must be transmitted every 250ms.

## Failure Modes

- Missing heartbeat causes UI freeze
- Invalid checksum causes ignored packets
- Delayed startup causes splash lock

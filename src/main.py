import asyncio
import yaml

from serial.uart import UARTBridge
from protocol.parser import PacketParser
from moonraker.client import MoonrakerClient
from tft.dispatcher import TFTDispatcher
from tft.heartbeat import heartbeat_task


async def uart_reader(uart, parser, dispatcher):
    while True:
        data = uart.read()

        if data:
            packets = parser.parse(data)

            for command, payload in packets:
                await dispatcher.dispatch(command, payload)

        await asyncio.sleep(0.001)


async def main():

    with open("config/bridge.yaml") as f:
        config = yaml.safe_load(f)

    uart = UARTBridge(
        config["serial"]["port"],
        config["serial"]["baudrate"]
    )

    moonraker = MoonrakerClient(
        config["moonraker"]["url"]
    )

    await moonraker.connect()

    parser = PacketParser()

    dispatcher = TFTDispatcher(moonraker)

    asyncio.create_task(heartbeat_task(uart))

    await uart_reader(uart, parser, dispatcher)


asyncio.run(main())

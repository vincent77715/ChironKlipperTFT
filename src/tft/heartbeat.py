import asyncio

from protocol.packets import build_packet


async def heartbeat_task(uart):
    while True:
        packet = build_packet(0x81)
        uart.write(packet)

        await asyncio.sleep(0.25)

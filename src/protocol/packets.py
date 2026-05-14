from protocol.checksum import checksum


HEADER = 0xA5


def build_packet(command: int, payload: bytes = b""):
    length = len(payload)

    packet = bytes([
        HEADER,
        command,
        length,
    ]) + payload

    packet += bytes([checksum(packet)])

    return packet

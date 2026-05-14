from protocol.checksum import checksum


class PacketParser:
    HEADER = 0xA5

    def parse(self, data: bytes):
        packets = []

        i = 0

        while i < len(data):
            if data[i] != self.HEADER:
                i += 1
                continue

            if i + 4 >= len(data):
                break

            command = data[i + 1]
            length = data[i + 2]

            end = i + 3 + length

            if end >= len(data):
                break

            payload = data[i + 3:end]
            rx_checksum = data[end]

            calc_checksum = checksum(data[i:end])

            if rx_checksum == calc_checksum:
                packets.append((command, payload))

            i = end + 1

        return packets

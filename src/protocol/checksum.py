
def checksum(data: bytes) -> int:
    return sum(data) & 0xFF

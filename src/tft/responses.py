from protocol.packets import build_packet


def build_temperature_packet(hotend, hotend_target, bed, bed_target):

    payload = bytes([
        int(hotend),
        int(hotend_target),
        int(bed),
        int(bed_target),
    ])

    return build_packet(0x82, payload)

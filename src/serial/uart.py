import serial


class UARTBridge:
    def __init__(self, port, baudrate):
        self.serial = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=0,
        )

    def read(self):
        return self.serial.read(1024)

    def write(self, data: bytes):
        self.serial.write(data)

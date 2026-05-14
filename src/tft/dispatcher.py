from protocol.commands import TFTCommand
from moonraker.gcode import run_gcode


class TFTDispatcher:
    def __init__(self, moonraker):
        self.moonraker = moonraker

    async def dispatch(self, command, payload):

        if command == TFTCommand.HOME_ALL:
            await run_gcode(self.moonraker, "G28")

        elif command == TFTCommand.SET_HOTEND_TEMP:
            temp = payload[0]
            await run_gcode(self.moonraker, f"M104 S{temp}")

        elif command == TFTCommand.PRINT_PAUSE:
            await run_gcode(self.moonraker, "PAUSE")

        elif command == TFTCommand.PRINT_RESUME:
            await run_gcode(self.moonraker, "RESUME")

        elif command == TFTCommand.PRINT_STOP:
            await run_gcode(self.moonraker, "CANCEL_PRINT")

        elif command == TFTCommand.LEVELING:
            await run_gcode(self.moonraker, "BED_MESH_CALIBRATE")

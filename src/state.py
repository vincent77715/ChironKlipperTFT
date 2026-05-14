from dataclasses import dataclass
from enum import Enum


class PrinterState(Enum):
    BOOTING = 0
    READY = 1
    PRINTING = 2
    PAUSED = 3
    RESTARTING = 4
    ERROR = 5
    DISCONNECTED = 6


@dataclass
class RuntimeState:
    hotend_current: float = 0
    hotend_target: float = 0
    bed_current: float = 0
    bed_target: float = 0
    progress: int = 0
    filename: str = ""
    printer_state: PrinterState = PrinterState.BOOTING

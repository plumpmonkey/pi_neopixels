from enum import Enum, unique

@unique
class Mode(Enum):
    CYCLE = 1
    RIDER = 2
    RAINBOW = 3
    CLAP = 4
    OFF = 99
    PAUSE = 100
    UNKNOWN = 999

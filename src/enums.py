from enum import Enum

class Anchor(str, Enum):
    TopLeft = "topleft"
    BottomLeft = "bottomleft"
    TopRight = "topright"
    BottomRight = "bottomright"
    MidTop = "midtop"
    MidLeft = "midleft"
    MidBottom = "midbottom"
    MidRight = "midright"
    Center = "center"

class ButtonState(Enum):
    Idle = 0
    Hover = 1
    Press = 2
    Error = 3

    @classmethod
    def _missing_(cls, value):
        return cls.Error

class Align(int, Enum):
    Left = 0
    Center = 1
    Right = 2

from enum import Enum
from pygame import Color

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

class Pallete(Color, Enum):
    Gray1 = "#64646E"
    Gray2 = "#4E4E56"
    Gray3 = "#282835"
    LightGray1 = "#A9A9BA"
    LightGray2 = "#8F8F9E"
    LightGray3 = "#848491"
    LightGray4 = "#747484"
    White = "#FFFFFF"
    Black = "#000000"
    Empty = (0, 0, 0, 0)
    ATBlue = "#3CA4FF"
    ATBlue1 = "#9BD0FF"
    ATBlue2 = "#3CA4FF"
    ATBlue3 = "#0080FF"
    ATBlue4 = "#0048C1"
    ATBlue5 = "#000D2C"


__all__ = ["Anchor", "Align", "ButtonState", "Pallete"]

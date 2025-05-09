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

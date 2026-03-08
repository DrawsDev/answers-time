from time import time

from pygame import Color


def rainbow(speed: float = 50.0, s: float = 100.0, v: float = 100.0) -> Color:
    t = time()
    h = (t * speed) % 360.0
    return Color.from_hsva(h, s, v, 100.0)

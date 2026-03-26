from pygame import Color, Event, Vector2, Vector3

from . import graphics, keyboard, mouse
from .version import Version
from .application import Application
from .scene import Scene


def get_wrapper_version() -> Version:
    return Version.from_text("0.1.0.alpha.official")

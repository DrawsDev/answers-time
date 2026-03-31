from pygame import Color, Event, Vector2, Vector3

from . import graphics, keyboard, mouse
from .version import Version
from .application import Application
from .scene import Scene


def get_pygame_welcome_message() -> str:
    from pygame import ver, SDL
    from platform import python_version
    return f"pygame-ce {ver} (SDL {SDL}, Python {python_version()})"


def get_wrapper_version() -> Version:
    return Version.from_text("0.1.0.alpha.official")

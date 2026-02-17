import sys

import pygame

from .graphics import Graphics
from .keyboard import Keyboard
from .mouse import Mouse
from .scene import SceneManager
from .version import Version
from .window import Window

VERSION = "0.1.0.alpha.official"

pygame.init()
pygame.mixer.init()

class Application:
    def __init__(self, title: str, width: int, height: int) -> None:
        self.keyboard = Keyboard()
        self.mouse = Mouse()
        self.window = Window(title, width, height)
        self.graphics = Graphics(self)
        self.scene = SceneManager(self)
        self._version = None
        self._wrapper_version = Version.from_text(VERSION)

    @property
    def version(self) -> Version:
        return self._version

    @version.setter
    def version(self, value: str) -> None:
        if self._version == None: # yea i'm dumbass
            self._version = Version.from_text(value)

    @property
    def wrapper_version(self) -> Version:
        return self._wrapper_version

    def run(self) -> None:
        while not self.window.is_should_close():
            self.process()
        self.quit()

    def quit(self) -> None:
        self.scene.unload()
        sys.exit(0)
        pygame.quit()

    def process(self) -> None:
        self.window.process()
        self._fullscreen_key_handler()
        self.scene.process(self.window.get_delta())

    def _fullscreen_key_handler(self) -> None:
        if self.keyboard.is_just_pressed("f11") \
        or self.keyboard.is_just_pressed("return") and self.keyboard.is_modifier_active("alt"):
            self.window.toggle_fullscreen()

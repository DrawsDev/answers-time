import sys

import pygame

from .clock import Clock
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
        self.clock = Clock()
        self.window = Window(title, width, height)
        self.graphics = Graphics(self)
        self.scene = SceneManager(self)
        self.keyboard = Keyboard()
        self.mouse = Mouse()
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
        while True:
            self.event()
            self.process()

    def quit(self) -> None:
        self.scene.unload()
        sys.exit(0)
        pygame.quit()

    def event(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()

    def process(self) -> None:
        self.clock.tick()
        self.window.flip()
        self.scene.process(self.clock.delta)
        self._fullscreen_key_handler()

    def _fullscreen_key_handler(self) -> None:
        if self.keyboard.is_just_pressed("f11") \
        or self.keyboard.is_just_pressed("return") and self.keyboard.is_modifier_active("alt"):
            self.window.toggle_fullscreen()
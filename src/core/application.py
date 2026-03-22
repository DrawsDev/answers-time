import os
import sys
from typing import Optional

import pygame

from src.core.clock import Clock
from src.core.graphics import Graphics
from src.core.keyboard import Keyboard
from src.core.mouse import Mouse
from src.core.scene import SceneManager
from src.core.version import Version
from src.core.window import Window

VERSION = "0.1.0.alpha.official"

if sys.platform == "win32":
    os.environ["SDL_WINDOWS_DPI_AWARENESS"] = "system"
os.environ["SDL_VIDEO_CENTERED"] = "1"

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

    def get_wrapper_version(self) -> Version:
        return self._wrapper_version

    def get_version(self) -> Optional[Version]:
        return self._version

    def set_version(self, version: str) -> None:
        if self._version == None: # yea i'm dumbass
            self._version = Version.from_text(version)

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
            self.window.event(event)
            self.scene.event(event)

    def process(self) -> None:
        self.clock.tick()
        self.window.flip()
        self.scene.process(self.clock.delta)
        self._fullscreen_key_handler()

    def _fullscreen_key_handler(self) -> None:
        if (
            self.keyboard.is_just_pressed("f11")
            or self.keyboard.is_just_pressed("return")
            and self.keyboard.is_modifier_active("alt")
        ):
            if self.window.is_fullscreen():
                self.window.set_windowed()
            else:
                self.window.set_fullscreen()

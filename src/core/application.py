import os
import sys
from typing import Optional

import pygame

from .clock import Clock
from .scene import SceneManager
from .version import Version
from .window import Window

if sys.platform == "win32":
    os.environ["SDL_WINDOWS_DPI_AWARENESS"] = "system"
os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()
pygame.mixer.init()


class Application:
    def __init__(self, title: str, width: int, height: int) -> None:
        self.clock = Clock()
        self.window = Window(title, width, height)
        self.scene = SceneManager(self)
        self._version = None

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
        self.scene.process(self.clock.get_delta())

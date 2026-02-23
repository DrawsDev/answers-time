from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from src.core.application import Application
    from src.core.scene import Scene

class SceneManager:
    def __init__(self, app: "Application") -> None:
        self.app = app
        self.scene = None

    def load(self, scene: "Scene", **kwargs) -> None:
        self.unload()
        self.scene = scene(self.app, **kwargs)

    def unload(self, **kwargs) -> None:
        if self.scene:
            self.scene.unload(**kwargs)
            self.scene = None

    def event(self, event: pygame.Event) -> None:
        if self.scene:
            self.scene.event(event)

    def process(self, delta: float) -> None:
        if self.scene:
            self.scene.process(delta)
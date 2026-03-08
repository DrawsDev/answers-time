from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from src.core.application import Application


class Scene:
    def __init__(self, app: "Application", **kwargs) -> None:
        self.app = app
        self.on_enter(**kwargs)

    def unload(self, **kwargs) -> None:
        self.on_exit(**kwargs)
        self.app = None

    def on_enter(self, **kwargs) -> None:
        pass

    def on_exit(self, **kwargs) -> None:
        pass

    def event(self, event: pygame.Event) -> None:
        pass

    def process(self, delta: float) -> None:
        pass


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

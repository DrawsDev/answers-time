from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..application import Application
    from .scene import Scene

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

    def process(self, delta: float) -> None:
        if self.scene:
            self.scene.process(delta)

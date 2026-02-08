from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..application import Application

class Scene:
    def __init__(self, app: "Application", **kwargs) -> None:
        self.app = app
        self.on_enter(**kwargs)

    def unload(self) -> None:
        self.on_exit()
        self.app = None

    def on_enter(self, **kwargs) -> None:
        pass

    def on_exit(self) -> None:
        pass

    def process(self, delta: float) -> None:
        pass

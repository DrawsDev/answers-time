import pygame
from typing import Tuple
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.scene.ui import *

class Frame(Primitive):
    def __init__(
        self,
        app: Application,
        color: pygame.Color = "black",
        size: Tuple[int, int] = (100, 100), 
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
        z_index: int = 0
    ) -> None:
        super().__init__(app, size, position, anchor, z_index)
        self._color = color
        self._update_image()

    @property
    def color(self) -> pygame.Color:
        return self._color

    @color.setter
    def color(self, value: pygame.Color) -> None:
        if self._color != value:
            self._color = value
            self._update_image()

    def _update_image(self) -> None:
        super()._update_image()
        self.image.fill(self._color)

__all__ = ["Frame"]

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
        color: pygame.Color = "Black",
        size: Tuple[int, int] = (100, 100), 
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
        z_index: int = 0,
        border_width: int = 0,
        border_radius: int = -1
    ) -> None:
        super().__init__(app, size, position, anchor, z_index)
        self._color = color
        self._border_width = border_width
        self._border_radius = border_radius
        self._update_image()

    @property
    def color(self) -> pygame.Color:
        return self._color

    @color.setter
    def color(self, value: pygame.Color) -> None:
        if self._color != value:
            self._color = value
            self._update_image()

    @property
    def border_width(self) -> int:
        return self._border_width
    
    @border_width.setter
    def border_width(self, value: int) -> None:
        if value >= 0:
            self._border_width = value
            self._update_image()

    @property
    def border_radius(self) -> int:
        return self._border_radius
    
    @border_radius.setter
    def border_radius(self, value: int) -> None:
        if value >= -1:
            self._border_radius = value
            self._update_image()

    def _update_image(self) -> None:
        super()._update_image()
        pygame.draw.rect(self.image, self.color, ((0, 0), self.rect.size), self.border_width, self.border_radius)

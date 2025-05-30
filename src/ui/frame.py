import pygame
from typing import Tuple
from src.enums import Anchor
from src.core.game import Game
from src.ui.base.ui_object import UIObject

class Frame(UIObject):
    def __init__(
        self,
        game: Game,
        color: pygame.Color = "black",
        size: Tuple[int, int] = (100, 100), 
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft
    ) -> None:
        super().__init__(game, size, position, anchor)
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

from pygame import Surface, Color
from typing import Tuple, Optional
from src.core.game import Game
from src.core.utility import clamp
from src.ui.base.ui_object import UIObject

class Frame(UIObject):
    def __init__(self, 
                 game: Game, 
                 size: Tuple[int, int] = (100, 100), 
                 position: Tuple[int, int] = (0, 0)
                 ):
        super().__init__(game, size, position)

        self._alpha = 255
        self._color = "BLACK"
        self._update_image()

    @property
    def color(self) -> Color:
        return self._color

    @property
    def transparency(self) -> Optional[int]:
        return self._alpha

    @color.setter
    def color(self, value: Color) -> None:
        self._color = value
        self._update_image()

    @transparency.setter
    def transparency(self, value: int) -> None:
        self._alpha = clamp(value, 0, 255)
        self._update_image()

    def _update_image(self) -> None:
        self.image = Surface(self._size)
        self.image.fill(self._color)
        self.image.set_alpha(self._alpha)
        self._update_rect()

__all__ = ["Frame"]

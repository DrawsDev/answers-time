import pygame
from typing import Tuple
from src.core.game import Game
from src.ui.base.ui_object import UIObject

class UIImage(UIObject):
    def __init__(self, 
                 game: Game,
                 path: str,
                 position: Tuple[int, int] = [0, 0]
                 ):
        super().__init__(game, position=position)

        self._image_path = path
        self._load_image()

    @property
    def image_path(self) -> str:
        return self._image_path

    @image_path.setter
    def image_path(self, value: str) -> None:
        self._image_path = value
        self._load_image()

    def _load_image(self) -> None:
        self.image = pygame.image.load(self._image_path)
        self.image.set_colorkey("Black")
        self._update_rect()

__all__ = ["UIImage"]

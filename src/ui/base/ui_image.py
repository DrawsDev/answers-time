import pygame
from typing import Tuple
from src.core.game import Game
from src.core.utility import path
from src.ui.base.ui_object import UIObject

class UIImage(UIObject):
    def __init__(self, 
                 game: Game,
                 relative_path: str,
                 position: Tuple[int, int] = [0, 0]
                 ):
        super().__init__(game, position=position)

        self._path = relative_path
        self._load_image(relative_path)

    @property
    def image_path(self) -> str:
        return self._path

    @image_path.setter
    def image_path(self, relative_path: str) -> None:
        self._load_image(relative_path)

    def _load_image(self, relative_path: str) -> None:
        self.image = pygame.image.load(path(relative_path))
        self.image.set_colorkey("BLACK")
        self._update_rect()

__all__ = ["UIImage"]

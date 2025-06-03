import pygame
from typing import Tuple
from src.enums import Anchor
from src.core.game import Game
from src.ui.base.ui_object import UIObject

class UIImage(UIObject):
    def __init__(
        self, 
        game: Game,
        path: pygame.Surface,
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
        z_index: int = 0,
        scale_factor: float = 1.0
    ) -> None:
        super().__init__(game, (0, 0), position, anchor, z_index)
        self._image_copy = None
        self._image_path = path
        self._image_scale_factor = scale_factor
        self._load_image()

    @property
    def image_path(self) -> str:
        return self._image_path

    @image_path.setter
    def image_path(self, value: str) -> None:
        self._image_path = value
        self._load_image()

    def scale_by(self, factor: float = 1.0) -> None:
        if factor >= 0:
            self.image = pygame.transform.scale_by(self._image_copy, factor)
            self._image_scale_factor = factor
            self._update_rect()

    def _load_image(self) -> None:
        self.image = pygame.image.load(self._image_path)
        self.image.set_colorkey("black")
        self._image_copy = self.image.copy()
        self.scale_by(self._image_scale_factor)
        self._update_rect()

__all__ = ["UIImage"]

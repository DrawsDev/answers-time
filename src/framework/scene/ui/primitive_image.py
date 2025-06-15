import pygame
from typing import Tuple, Optional
from src.framework.enums import *
from src.framework.application import Application
from src.framework.scene.ui import Primitive

class PrimitiveImage(Primitive):
    def __init__(
        self, 
        app: Application,
        path: Optional[str] = None,
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
        z_index: int = 0,
        scale_factor: float = 1.0
    ) -> None:
        super().__init__(app, (0, 0), position, anchor, z_index)
        self._image_copy = None
        self._image_path = path
        self._image_scale_factor = scale_factor
        self._load_image()

    @property
    def image_path(self) -> Optional[str]:
        return self._image_path

    @image_path.setter
    def image_path(self, value: Optional[str]) -> None:
        self._image_path = value
        self._load_image()

    def scale_by(self, factor: float = 1.0) -> None:
        if factor >= 0 and self._image_path:
            self.image = pygame.transform.scale_by(self._image_copy, factor)
            self._image_scale_factor = factor
            self._update_rect()

    def _load_image(self) -> None:
        if self._image_path is not None:
            self.image = pygame.image.load(self._image_path)
            self.image.set_colorkey("black")
            self._image_copy = self.image.copy()
            self.scale_by(self._image_scale_factor)
            self._update_rect()

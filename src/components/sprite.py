import pygame
from typing import Tuple
from src.enums import Anchor

class Sprite(pygame.sprite.Sprite):
    def __init__(self,
                 image: pygame.Surface,
                 position: Tuple[int, int] = [0, 0],
                 anchor: Anchor = Anchor.TopLeft
                 ) -> None:
        super().__init__()
        self._position = position
        self._anchor = anchor
        self._anchor_offset = [0, 0]
        self._update_image(image)
    
    @property
    def position(self) -> Tuple[int, int]:
        return self._position
    
    @position.setter
    def position(self, value: Tuple[int, int]) -> None:
        self._position = value
        self._update_rect()

    @property
    def anchor(self) -> str:
        return self._anchor
    
    @anchor.setter
    def anchor(self, value: Anchor) -> None:
        self._anchor = value
        self._update_rect()

    @property
    def anchor_offset(self) -> str:
        return self._anchor_offset
    
    @anchor_offset.setter
    def anchor_offset(self, value: Tuple[int, int]) -> None:
        self._anchor_offset = value
        self._update_rect()

    def _update_rect(self) -> None:
        x = self._position[0] - self._anchor_offset[0]
        y = self._position[1] - self._anchor_offset[1]
        self.rect = self.image.get_rect(**{self._anchor: [x, y]})
    
    def _update_image(self, image: pygame.Surface) -> None:
        self.image = image
        self._update_rect()

__all__ = ["Sprite"]

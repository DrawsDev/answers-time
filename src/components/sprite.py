import pygame
from pygame.math import Vector2
from enum import Enum

class Anchor(str, Enum):
    TopLeft = "topleft"
    BottomLeft = "bottomleft"
    TopRight = "topright"
    BottomRight = "bottomright"
    MidTop = "midtop"
    MidLeft = "midleft"
    MidBottom = "midbottom"
    MidRight = "midright"
    Center = "center"

class Sprite(pygame.sprite.Sprite):
    def __init__(self,
                 image: pygame.Surface,
                 position: pygame.math.Vector2 = (0, 0),
                 anchor: Anchor = Anchor.TopLeft
                 ) -> None:
        super().__init__()
        self._position = position
        self._anchor = anchor
        self._anchor_offset = Vector2()
        self._update_image(image)
    
    @property
    def position(self) -> Vector2:
        return self._position
    
    @position.setter
    def position(self, value: Vector2) -> None:
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
    def anchor_offset(self, value: Vector2) -> None:
        self._anchor_offset = value
        self._update_rect()

    def _update_rect(self) -> None:
        self.rect = self.image.get_rect(**{self._anchor: self._position - self._anchor_offset})
    
    def _update_image(self, image: pygame.Surface) -> None:
        self.image = image
        self._update_rect()

__all__ = ["Sprite", "Anchor"]

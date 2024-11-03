import pygame
from pygame.math import Vector2

class Sprite(pygame.sprite.Sprite):
    def __init__(self,
                 image: pygame.Surface,
                 position: Vector2 = (0, 0),
                 anchor: str = "topleft"
                 ) -> None:
        super().__init__()
        self._position = position
        self._anchor = anchor
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
    
    @position.setter
    def anchor(self, value: str) -> None:
        self._anchor = value
        self._update_rect()

    def _update_rect(self) -> None:
        self.rect = self.image.get_rect(**{self._anchor: self._position})
    
    def _update_image(self, image: pygame.Surface) -> None:
        self.image = image
        self._update_rect()


import pygame

from src.core.graphics import Drawable

class Sprite(pygame.sprite.Sprite, Drawable):
    def __init__(self, surface: pygame.Surface) -> None:
        super().__init__()
        self._anchor = "center"
        self._position = pygame.Vector2(0, 0)
        self._update_image(surface)

    @property
    def anchor(self) -> str:
        return self._anchor

    @anchor.setter
    def anchor(self, value: str) -> None:
        self._anchor = value
        self._update_rect()

    @property
    def position(self) -> pygame.Vector2:
        return self._position

    @position.setter
    def position(self, value: pygame.Vector2) -> None:
        self._position = value
        self._update_rect()

    def _update_image(self, surface: pygame.Surface) -> None:
        self.image = surface
        self._update_rect()
    
    def _update_rect(self) -> None:
        self.rect = self.image.get_frect(**{self._anchor: self._position})

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect)

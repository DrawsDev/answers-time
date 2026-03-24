from typing import Optional

import pygame


class Sprite:
    def __init__(self) -> None:
        super().__init__()
        self._surface = None
        self._rect = pygame.FRect()
        self._anchor = "center"
        self._offset = pygame.Vector2()
        self._position = pygame.Vector2()

    @property
    def surface(self) -> Optional[pygame.Surface]:
        return self._surface
    
    @surface.setter
    def surface(self, value: Optional[pygame.Surface]) -> None:
        if self._surface != value:
            self._surface = value
            self._update_rect()

    @property
    def rect(self) -> pygame.FRect:
        return self._rect

    @property
    def anchor(self) -> str:
        return self._anchor

    @anchor.setter
    def anchor(self, value: str) -> None:
        self._anchor = value
        self._update_rect()

    @property
    def offset(self) -> pygame.Vector2:
        return self._offset
    
    @offset.setter
    def offset(self, value: pygame.Vector2):
        self._offset = value
        self._update_rect()

    @property
    def position(self) -> pygame.Vector2:
        return self._position

    @position.setter
    def position(self, value: pygame.Vector2) -> None:
        self._position = value
        self._update_rect()

    def _update_rect(self) -> None:
        if self._surface:
            self._rect = self._surface.get_frect(**{self._anchor: self._position})
        else:
            setattr(self._rect, self._anchor, self._position)

    def draw(self, surface: pygame.Surface) -> None:
        if self._surface:
            surface.blit(self._surface, self._rect)

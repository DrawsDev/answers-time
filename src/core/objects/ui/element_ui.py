from typing import Tuple

import pygame

from src.core.graphics import Drawable


class ElementUI(Drawable):
    def __init__(self) -> None:
        self._anchor = "topleft"
        self._position = pygame.Vector2()
        self._rect = pygame.FRect()
        self._hovered = False
        self._mouse_filter = 0

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
    
    @property
    def rect(self) -> pygame.FRect:
        return self._rect

    @property
    def mouse_filter(self) -> int:
        return self._mouse_filter
    
    @mouse_filter.setter
    def mouse_filter(self, value: int) -> None:
        self._mouse_filter = value

    @property
    def hovered(self) -> bool:
        return self._hovered
    
    @hovered.setter
    def hovered(self, value: bool) -> None:
        if self._hovered != value:
            self._hovered = value
            self._update_surface()

    def _update_rect(self) -> None:
        setattr(self._rect, self._anchor, self._position)

    def _update_surface(self) -> None:
        pass

    def has_point(self, point: Tuple[int, int]) -> bool:
        if self._mouse_filter == 1:
            return False
        return self._rect.collidepoint(point)

    def adjust(self) -> pygame.FRect:
        return self._rect

    def draw(self, surface: pygame.Surface) -> None:
        pass

    def event(self, event: pygame.Event) -> None:
        pass

    def process(self, delta: float) -> None:
        if self._mouse_filter == 0:
            point = pygame.mouse.get_pos()
            self.hovered = self._rect.collidepoint(point)
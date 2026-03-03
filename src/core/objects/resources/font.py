from typing import Optional

import pygame
import pygame.freetype

from src.core.objects.gui import Element


class Font:
    def __init__(self, parent: Optional[Element] = None) -> None:
        self._parent = parent
        self._font = pygame.freetype.Font(None, 24)

    @property
    def filepath(self) -> Optional[str]:
        self._font.path

    @filepath.setter
    def filepath(self, value: Optional[str]) -> None:
        self._font = pygame.freetype.Font(value, self._font.size)
        self._update_parent_surface()

    @property
    def antialias(self) -> bool:
        return self._font.antialiased

    @antialias.setter
    def antialias(self, value: bool) -> None:
        self._font.antialiased = value
        self._update_parent_surface()

    @property
    def size(self) -> float:
        return self._font.size

    @size.setter
    def size(self, value: float) -> None:
        if value > 0:
            self._font.size = value
            self._update_parent_surface()

    def _update_parent_surface(self) -> None:
        if self._parent:
            self._parent._update_surface()

    def render(self, text: str, color: pygame.Color) -> pygame.Surface:
        surface, _ = self._font.render(text, color)
        return surface

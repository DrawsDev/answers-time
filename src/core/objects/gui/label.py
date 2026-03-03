import pygame

from src.core.objects.gui import Element
from src.core.objects.resources import Font


class Label(Element):
    def __init__(self) -> None:
        super().__init__()
        self._offset = pygame.Vector2()
        self._text = ""
        self._font = Font(self)
        self._update_surface()

    @property
    def offset(self) -> pygame.Vector2:
        return self._offset
    
    @offset.setter
    def offset(self, value: pygame.Vector2) -> None:
        self._offset = value
        self._update_rect()

    @property
    def text(self) -> str:
        return self._text
    
    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        self._update_surface()

    @property
    def font(self) -> Font:
        return self._font

    def _update_surface(self) -> None:
        self._surface = self._font.render(self._text, "white")
        self._update_rect()

    def _update_rect(self) -> None:
        position = self._position + self._offset
        self._rect = self._surface.get_frect(**{self._anchor: position})

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self._surface, self._rect)

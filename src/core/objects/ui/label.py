import pygame
import pygame.freetype

from src.core.graphics import Drawable

class Label(Drawable):
    def __init__(self) -> None:
        self._text = ""
        self._font = pygame.freetype.Font(None, 24)
        self._font_color = "white"
        self._position = pygame.Vector2()
        self._offset = pygame.Vector2()
        self._anchor = "topleft"
        self._update_surface()

    @property
    def position(self) -> pygame.Vector2:
        return self._position

    @position.setter
    def position(self, value: pygame.Vector2):
        self._position = value
        self._update_rect()

    @property
    def offset(self) -> pygame.Vector2:
        return self._offset
    
    @offset.setter
    def offset(self, value: pygame.Vector2) -> None:
        self._offset = value
        self._update_rect()

    @property
    def anchor(self) -> str:
        return self._anchor
    
    @anchor.setter
    def anchor(self, value: str) -> None:
        self._anchor = value
        self._update_rect()

    @property
    def text(self) -> str:
        return self._text
    
    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        self._update_surface()

    @property
    def font_filepath(self) -> str:
        return self._font.path

    @font_filepath.setter
    def font_filepath(self, value: str) -> None:
        self._font = pygame.freetype.Font(value, self._font.size)
        self._update_surface()

    @property
    def font_size(self) -> int:
        return self._font.size
    
    @font_size.setter
    def font_size(self, value: int) -> None:
        if value > 0:
            self._font.size = value
            self._update_surface()

    @property
    def font_color(self) -> str:
        return self._font_color
    
    @font_color.setter
    def font_color(self, value: str) -> None:
        self._font_color = value
        self._update_surface()

    def _update_surface(self) -> None:
        self._surface, _ = self._font.render(self._text, self._font_color)
        self._update_rect()

    def _update_rect(self) -> None:
        position = self._position + self._offset
        self._rect = self._surface.get_frect(**{self._anchor: position})

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self._surface, self._rect)
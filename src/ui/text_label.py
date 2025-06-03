import os
import pygame
from typing import Tuple, Optional
from src.enums import Align, Anchor
from src.core.game import Game
from src.ui.base.ui_object import UIObject

class TextLabel(UIObject):
    def __init__(
        self, 
        game: Game, 
        text: str = "TextLabel", 
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
        z_index: int = 0,
        font_path: Optional[str] = None,
        font_size: int = 20,
        font_align: Align = Align.Center,
        text_color: pygame.Color = "white",
        text_wraplength: int = 200,
        text_background_color: Optional[pygame.Color] = None,
        text_background_padding: int = 0

    ) -> None:
        super().__init__(game, (0, 0), position, anchor, z_index)
        self._text = text
        self._text_wraplength = text_wraplength
        self._text_color = text_color
        self._text_background_color = text_background_color
        self._text_background_padding = text_background_padding
        self._font = pygame.Font(font_path, font_size)
        self._font_path = font_path
        self._font.align = font_align
        self._update_image()
    
    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        self._update_image()

    @property
    def text_color(self) -> pygame.Color:
        return self._text_color

    @text_color.setter
    def text_color(self, value: pygame.Color) -> None:
        self._text_color = value
        self._update_image()

    @property
    def text_wraplength(self) -> int:
        return self._text_wraplength

    @text_wraplength.setter
    def text_wraplength(self, value: int) -> None:
        if value >= 0:
            self._text_wraplength = value
            self._update_image()
    
    @property
    def font(self) -> pygame.Font:
        return self._font

    @property
    def font_size(self) -> int:
        return self._font.get_point_size()

    @font_size.setter
    def font_size(self, value: int):
        if value >= 0:
            align = self._font.align
            self._font = pygame.Font(self._font_path, value)
            self._font.align = align
            self._update_image()

    @property
    def font_path(self) -> Optional[str]:
        return self._font_path

    @font_path.setter
    def font_path(self, value: Optional[str]) -> None:
        if value != None and not os.path.exists(value):
            value = None
        size = self._font.get_point_size()
        align = self._font.align
        self._font_path = value
        self._font = pygame.Font(value, size)
        self._font.align = align
        self._update_image()

    @property
    def font_align(self) -> Align:
        return self._font.align

    @font_align.setter
    def font_align(self, value: Align) -> None:
        self._font.align = value
        self._update_image()

    @property
    def text_background_color(self) -> Optional[pygame.Color]:
        return self._text_background_color

    @text_background_color.setter
    def text_background_color(self, value: Optional[pygame.Color]) -> None:
        self._text_background_color = value
        self._update_image()

    @property
    def text_background_padding(self) -> int:
        return self._text_background_padding
    
    @text_background_padding.setter
    def text_background_padding(self, value: int) -> None:
        if value >= 0:
            self._text_background_padding = value
            self._update_image()

    def _update_image(self) -> None:
        text_surface = self._font.render(self._text, True, self._text_color, None, self._text_wraplength)
        self.image = self._create_background_surface(text_surface.get_size())
        self.image.blit(text_surface, [self._text_background_padding, self._text_background_padding])
        self._size = self.image.get_size()
        self._update_rect()       

    def _create_background_surface(self, text_surface_size: Tuple[int, int]) -> pygame.Surface:
        padding = self._text_background_padding + self._text_background_padding
        surface = pygame.Surface([text_surface_size[0] + padding, text_surface_size[1] + padding], pygame.SRCALPHA)
        if self._text_background_color: surface.fill(self._text_background_color)
        return surface

__all__ = ["TextLabel"]

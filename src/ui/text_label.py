import pygame
from typing import Tuple, Optional
from src.enums import TextAlign
from src.core.game import Game
from src.core.utility import path
from src.ui.base.ui_object import UIObject

class TextLabel(UIObject):
    def __init__(self, 
                 game: Game, 
                 text: str = "TextLabel", 
                 position: Tuple[int, int] = (0, 0)
                 ):
        super().__init__(game, (0, 0), position)
        self._text = text
        self._text_align = TextAlign.Center
        self._text_wraplength = 200
        self._text_color = "White"
        self._text_antialias = True
        self._text_fontpath = None
        self._text_fontsize = 20
        self._text_background_color = None
        self._text_background_padding = 5
        self._font = pygame.Font(self._text_fontpath, self._text_fontsize)

        self.text = text
    
    @property
    def text(self) -> str:
        return self._text

    @property
    def text_align(self) -> TextAlign:
        return self._text_align

    @property
    def text_wraplength(self) -> int:
        return self._text_wraplength

    @property
    def text_color(self) -> pygame.Color:
        return self._text_color

    @property
    def text_antialias(self) -> bool:
        return self._text_antialias

    @property
    def text_fontpath(self) -> str:
        return self._text_fontpath
    
    @property
    def text_fontsize(self) -> int:
        return self._text_fontsize

    @property
    def font(self) -> pygame.Font:
        return self._font

    @property
    def text_background_color(self) -> Optional[pygame.Color]:
        return self._text_background_color

    @property
    def text_background_padding(self) -> int:
        return self._text_background_padding

    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        self._update_image()

    @text_align.setter
    def text_align(self, value: TextAlign) -> None:
        self._text_align = value
        self._font.align = value
        self._update_image()

    @text_wraplength.setter
    def text_wraplength(self, value: int) -> None:
        if value >= 0:
            self._text_wraplength = value
            self._update_image()

    @text_color.setter
    def text_color(self, value: pygame.Color) -> None:
        self._text_color = value
        self._update_image()

    @text_antialias.setter
    def text_antialias(self, value: bool) -> None:
        self._text_antialias = value
        self._update_image()

    @text_fontpath.setter
    def text_fontpath(self, value: Optional[str]) -> None:
        self._text_fontpath = value
        self._font = pygame.Font(value, self._text_fontsize)
        self._update_image()

    @text_fontsize.setter
    def text_fontsize(self, value: int) -> None:
        if value >= 0:
            self._text_fontsize = value
            self._font = pygame.Font(self._text_fontpath, value)
            self._update_image()

    @text_background_color.setter
    def text_background_color(self, value: Optional[pygame.Color]) -> None:
        self._text_background_color = value
        self._update_image()
    
    @text_background_padding.setter
    def text_background_padding(self, value: int) -> None:
        if value >= 0:
            self._text_background_padding = value
            self._update_image()

    def _update_image(self) -> None:
        text_surface = self._font.render(self._text, self._text_antialias, self._text_color, None, self._text_wraplength)
        self.image = self._create_background_surface(text_surface.get_size())
        self.image.blit(text_surface, [self._text_background_padding, self._text_background_padding])
        self._update_rect()       

    def _create_background_surface(self, text_surface_size: Tuple[int, int]) -> pygame.Surface:
        padding = self._text_background_padding + self._text_background_padding
        surface = pygame.Surface([text_surface_size[0] + padding, text_surface_size[1] + padding], pygame.SRCALPHA)
        if self._text_background_color: surface.fill(self._text_background_color)
        return surface

__all__ = ["TextLabel"]

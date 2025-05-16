import os
import pygame
from typing import Tuple
from src.core.game import Game
from src.ui.base.object import UIObject

class Label(UIObject):
    def __init__(self, 
                 game: Game, 
                 text: str = "Label", 
                 position: Tuple[int, int] = [0, 0]
                 ):
        super().__init__(game, [0, 0], position)

        self._text = text
        self._fontpath = None
        self._fontsize = 20
        self._wraplength = 200
        self._antialias = True
        self._align = pygame.FONT_LEFT
        self._color = "WHITE"
        self._background_color = "BLACK"
        self._background_padding = 5
        self._font = pygame.Font(self._fontpath, self._fontsize)

        self.text = text
    
    @property
    def font(self) -> pygame.Font:
        return self._font

    @property
    def fontpath(self) -> str:
        return self._fontpath

    @property
    def fontsize(self) -> int:
        return self._fontsize

    @property
    def wraplength(self) -> int:
        return self._wraplength
    
    @property
    def text(self) -> str:
        return self._text

    @property
    def color(self) -> pygame.Color:
        return self._color

    @property
    def background_color(self) -> pygame.Color:
        return self._background_color

    @property
    def background_padding(self) -> int:
        return self._background_padding

    @property
    def align(self) -> int:
        return self._align

    @property
    def antialias(self) -> bool:
        return self._antialias

    @fontpath.setter
    def fontpath(self, value: str = None) -> None:
        if not value is None and os.path.exists(value) and os.path.splitext(value)[1] == ".ttf":
            self._fontpath = value
            self._font = pygame.Font(value, self._fontsize)
            self._update_image()

    @fontsize.setter
    def fontsize(self, value: int) -> None:
        if value >= 0:
            self._fontsize = value
            self._font = pygame.Font(self._fontpath, value)
            self._update_image()

    @wraplength.setter
    def wraplength(self, value: int) -> None:
        if value >= 0:
            self._wraplength = value
            self._update_image()
    
    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        self._update_image()

    @color.setter
    def color(self, value: pygame.Color) -> None:
        self._color = value
        self._update_image()

    @background_color.setter
    def background_color(self, value: pygame.Color) -> None:
        self._background_color = value
        self._update_image()
    
    @background_padding.setter
    def background_padding(self, value: int) -> None:
        if value >= 0:
            self._background_padding = value
            self._update_image()

    @align.setter
    def align(self, value: int) -> None:
        if value in [pygame.FONT_LEFT, pygame.FONT_CENTER, pygame.FONT_RIGHT]:
            self._align = value
            self._font.align = value
            self._update_image()

    @antialias.setter
    def antialias(self, value: bool) -> None:
        self._antialias = value
        self._update_image()

    def _update_image(self) -> None:
        render = self._font.render(self._text, self._antialias, self._color, None, self._wraplength)
        self.image = self._get_background_surface(render.get_size())
        self.image.blit(render, [self._background_padding, self._background_padding])
        self._update_rect()       

    def _get_background_surface(self, size: Tuple[int, int]) -> pygame.Surface:
        padding = self._background_padding + self._background_padding
        surface = pygame.Surface([size[0] + padding, size[1] + padding])
        surface.fill(self._background_color)
        return surface

__all__ = ["Label"]

import os
import sys
import pygame
from typing import List
from src.components.sprite import Sprite

TTF = ".ttf"

class FontParams:
    def __init__(self,                 
                 fontpath: str = None, 
                 size: int = 20,
                 color: pygame.Color = (0, 0, 0), 
                 align: int = 0, 
                 alias: bool = True,
                 wraplength: int = 0) -> None:
        self._fontpath = fontpath
        self._size = size
        self._color = color
        self._align = align
        self._alias = alias
        self._wraplength = wraplength
    
    @property
    def fontpath(self) -> str:
        return self._fontpath
    
    @fontpath.setter
    def fontpath(self, path: str = None) -> None:
        if path is None:
            self._fontpath = path
        elif os.path.isfile(path) and os.path.splitext(path)[1] == TTF:
            self._fontpath = path

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int) -> None:
        self._size = value

    @property
    def color(self) -> tuple:
        return self._color
    
    @color.setter
    def color(self, value: pygame.Color) -> None:
        self._color = value
    
    @property
    def align(self) -> int:
        return self._align
    
    @align.setter
    def align(self, value: int) -> None:
        if value in (pygame.FONT_LEFT, pygame.FONT_CENTER, pygame.FONT_RIGHT):
            self._align = value

    @property
    def wraplength(self) -> int:
        return self._wraplength
    
    @wraplength.setter
    def wraplength(self, value: int) -> None:
        if value >= 0:
            self._wraplength = value

    def render_text(self, text: str) -> pygame.Surface:
        return self.get_font().render(text, self._alias, self._color, wraplength=self._wraplength)
    
    def get_font_size(self, text: str) -> List[int]:
        """
        Вернёт (ширину, высоту) изображения текста при заданных настройках шрифта.
        
        Отрисовки не произойдёт.
        """
        return self.get_font().size(text)   
     
    def get_font(self) -> pygame.font.Font:
        font = pygame.font.Font(self._fontpath, self._size)
        font.align = self._align
        return font

default = FontParams()

class Label(Sprite):
    def __init__(self, 
                 text: str = "Label", 
                 fontparams: FontParams = default,
                 position: pygame.Vector2 = (0, 0), 
                 anchor: str = "topleft") -> None:
        self._text = text
        self._fontparams = fontparams
        super().__init__(self._fontparams.render_text(text), position, anchor)

    @property
    def text(self) -> str:
        return self._text
    
    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        self._update_image(self._fontparams.render_text(value))

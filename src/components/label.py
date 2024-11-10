import pygame
from typing import List
from src.components.sprite import Sprite

class FontParams:
    def __init__(self,                 
                 fontpath: str = None, 
                 size: int = 20,
                 color: tuple = (0, 0, 0), 
                 align: int = 0, 
                 alias: bool = True,
                 wraplength: int = 0) -> None:
        self._fontpath = fontpath
        self._size = size
        self._color = color
        self._align = align
        self._alias = alias
        self._wraplength = wraplength
    
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

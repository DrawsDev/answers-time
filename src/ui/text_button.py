import pygame
from typing import Tuple
from src.enums import TextAlign
from src.core.game import Game
from src.ui.base.ui_button import UIButton

class TextButton(UIButton):
    def __init__(self, 
                 game: Game, 
                 text: str = "TextButton",
                 size: Tuple[int, int] = [100, 50],
                 position: Tuple[int, int] = [0, 0]):
        self._text = text
        self._font_wraplength = 200
        self._font_antialias = True
        self._font_align = TextAlign.Left
        self._font_color = "WHITE"
        self._font_path = None
        self._font_size = 20
        self._font = pygame.Font(self._font_path, self._font_size)
        super().__init__(game, size, position)

    @property
    def text(self) -> str:
        return self._text

    @property
    def font(self) -> pygame.Font:
        return self._font

    @property
    def text_align(self) -> TextAlign:
        return self._font_align

    @property
    def text_wraplength(self) -> int:
        return self._font_wraplength

    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        self._update_image()

    @text_align.setter
    def text_align(self, value: TextAlign) -> None:
        self._font_align = value
        self._font.align = self._font_align
        self._update_image()

    @text_wraplength.setter
    def text_wraplength(self, value: int) -> None:
        self._font_wraplength = value if value > 0 else 0
        self._update_image()

    def _update_image(self) -> None:
        super()._update_image()
        text_surface = self._font.render(self._text, self._font_antialias, self._font_color, None, self._font_wraplength)
        text_rect = text_surface.get_rect(**{"center": [self._button_size[0] / 2, self._button_size[1] / 2]})
        self.image.blit(text_surface, text_rect)
        self._update_rect()

__all__ = ["TextButton"]

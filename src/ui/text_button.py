import os
import pygame
from typing import Tuple, Optional
from src.enums import Align
from src.core.game import Game
from src.ui.base.ui_button import UIButton

class TextButton(UIButton):
    def __init__(
        self, 
        game: Game, 
        text: str = "TextButton",
        size: Tuple[int, int] = (100, 50),
        position: Tuple[int, int] = (0, 0)
    ):
        self._button_icon = None
        self._text = text
        self._text_color = "White"
        self._font = pygame.Font()
        self._font_path = None
        super().__init__(game, size, position)

    @property
    def button_icon(self) -> pygame.Surface:
        return self._button_icon

    @button_icon.setter
    def button_icon(self, value: pygame.Surface) -> None:
        self._button_icon = value
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
    def font(self) -> pygame.Font:
        return self._font

    @property
    def font_size(self) -> int:
        return self._font.get_point_size()

    @font_size.setter
    def font_size(self, value: int) -> None:
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

    def _update_image(self):
        super()._update_image()
        
        offset = 0
        if self._button_icon:
            offset = 5 + self._button_icon.get_width() + 5
            icon_rect = self._button_icon.get_rect(midleft=(5, self._size[1] / 2))
            self.image.blit(self._button_icon, icon_rect)

        text_surface = self._font.render(self._text, True, self._text_color, None, self._size[0] - offset)
        text_x = offset if self._font.align == Align.Left else (self._size[0] - text_surface.get_width() + offset) / 2
        text_rect = text_surface.get_rect(midleft=(text_x, self._size[1] / 2))
        
        self.image.blit(text_surface, text_rect)

__all__ = ["TextButton"]

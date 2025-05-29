import os
import pygame
from typing import Tuple, Optional
from src.enums import Align, Anchor
from src.core.game import Game
from src.core.utility import wrap_text
from src.ui.base.ui_button import UIButton

class TextButton(UIButton):
    def __init__(
        self, 
        game: Game, 
        text: str = "TextButton",
        size: Tuple[int, int] = (100, 50),
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
        font_path: Optional[str] = None,
        font_size: int = 20,
        font_align: Align = Align.Center,
        text_color: pygame.Color = "white",
        button_color: pygame.Color = "azure2",
        button_hover_color: pygame.Color = "azure3",
        button_press_color: pygame.Color = "azure4",
        button_icon: Optional[pygame.Surface] = None
    ) -> None:
        self._button_icon = button_icon
        self._text = text
        self._text_color = text_color
        self._font = pygame.Font(font_path, font_size)
        self._font_path = font_path
        self._font.align = font_align
        super().__init__(game, size, position, anchor, button_color, button_hover_color, button_press_color)

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

        # Автоматический подбор размера шрифта, разбиение текста по линиям и отрисовка
        if self._font.size(self._text)[0] > self._size[0] - offset:
            font_size, lines = wrap_text(self._text, self._font_path, self._size[0] - offset, self._size[1], self._font.get_point_size())
            font = pygame.Font(self._font_path, font_size)
            font.align = self._font.align

            y_offset = 0
            line_height = font.get_linesize()

            for index, line in enumerate(lines):
                text_surface = font.render(line, True, self._text_color, None)
                
                if self._font.align == Align.Left:
                    text_x = offset
                elif self._font.align == Align.Center:
                    text_x = (self._size[0] - text_surface.get_width() + offset) / 2
                elif self._font.align == Align.Right:
                    text_x = self._size[0] - text_surface.get_width()
                
                text_y = (self._size[1] + y_offset - line_height * (len(lines) - 1 - index)) / 2
                text_rect = text_surface.get_rect(midleft=(text_x, text_y))
                self.image.blit(text_surface, text_rect)
                y_offset += line_height
        # Стандартная отрисовка одной линии
        else:
            text_surface = self._font.render(self._text, True, self._text_color, None) #self._size[0] - offset
            text_x = offset if self._font.align == Align.Left else (self._size[0] - text_surface.get_width() + offset) / 2
            text_y = self._size[1] / 2
            text_rect = text_surface.get_rect(midleft=(text_x, text_y))
            self.image.blit(text_surface, text_rect)

__all__ = ["TextButton"]

import pygame
from typing import Tuple, Optional
from src.enums import Anchor, TextAlign
from src.core.game import Game
from src.ui.base.ui_button import UIButton

class TextButton(UIButton):
    def __init__(self, 
                 game: Game, 
                 text: str = "TextButton",
                 size: Tuple[int, int] = (100, 50),
                 position: Tuple[int, int] = (0, 0)):
        self._text = text
        self._text_anchor = Anchor.Center
        self._text_align = TextAlign.Center
        self._text_wraplength = 200
        self._text_color = "White"
        self._text_antialias = True
        self._text_fontpath = None
        self._text_fontsize = 20
        self._font = pygame.Font(self._text_fontpath, self._text_fontsize)
        super().__init__(game, size, position)

    @property
    def text(self) -> str:
        return self._text

    @property
    def text_anchor(self) -> Anchor:
        return self._text_anchor

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

    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        self._update_image()

    @text_anchor.setter
    def text_anchor(self, value: Anchor) -> None:
        self._text_anchor = value
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

    def _update_image(self) -> None:
        super()._update_image()
        text_surface = self._font.render(self._text, self._text_antialias, self._text_color, None, self._text_wraplength)
        text_rect = text_surface.get_rect(**{self._text_anchor: [self._button_size[0] / 2, self._button_size[1] / 2]})
        self.image.blit(text_surface, text_rect)
        self._update_rect()

__all__ = ["TextButton"]

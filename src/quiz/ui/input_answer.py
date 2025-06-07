import pygame
from typing import Tuple
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.base.ui_button import UIObject
from src.ui.text_box import TextBox
from src.ui.layout import Layout

GAP = 4

class InputAnswer(UIObject):
    def __init__(        
        self, 
        game: Game,
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
    ) -> None:
        super().__init__(game, (200, 90), position, anchor, 1)
        self._create_text_box()
        self._layout: Layout = Layout(True)
        self._layout.insert_child(self.textbox)
        self._update_image()

    def update(self, delta: float) -> None:
        super().update(delta)
        if self._layout.enabled:
            self._layout.update(delta)
 
    def draw(self, surface: pygame.Surface) -> None:
        super().draw(surface)
        if self._layout.enabled:
            self._layout.draw(surface)

    def _create_text_box(self) -> None:
        self.textbox = TextBox(
            game=self.game,
            text="",
            placeholder="Введите ответ",
            size=(300, 40),
            position=self.rect.center,
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white"
        )

__all__ = ["InputAnswer"]

import pygame
from typing import Tuple
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import asset_path
from src.ui.base.ui_button import UIButton
from src.ui.text_label import TextLabel

GAP = 4

class QuizButton(UIButton):
    def __init__(
        self, 
        game: Game,
        position: Tuple[int, int] = (0, 0), 
        anchor = Anchor.TopLeft, 
        z_index = 0,
        title: str = "",
        filename: str = ""
    ) -> None:
        super().__init__(game, (320, 80), position, anchor, z_index, Pallete.Gray2, Pallete.Gray1, Pallete.Gray3)
        self._create_text_label(title)
        self._create_filename_label(filename)
        self._update_image()

    def update(self, delta):
        super().update(delta)
        self.text.update(delta)
    
    def draw(self, surface):
        super().draw(surface)
        self.text.draw(surface)

    def _create_text_label(self, text: str) -> None:
        self.text = TextLabel(
            game=self.game,
            text=text,
            position=(0, 0),
            anchor=Anchor.MidLeft,
            z_index=-1,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.White,
            text_wraplength=self.rect.width - 40
        )

    def _create_filename_label(self, text: str) -> None:
        self.filename = TextLabel(
            game=self.game,
            text=text,
            position=(0, 0),
            anchor=Anchor.MidRight,
            z_index=-1,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=10,
            font_align=Align.Right,
            text_color=Pallete.LightGray2,
            text_wraplength=self.rect.width - 40
        )

    def _update_image(self):
        super()._update_image()
        self.image.fill(Pallete.ATBlue, (0, 0, 40, 80))
        if hasattr(self, "text"):
            self.image.blit(self.filename.image, self.filename.image.get_rect(bottomright=(self.rect.width - GAP, self.rect.height - GAP / 2)))
            self.image.blit(self.text.image, self.text.image.get_rect(midleft=(40 + GAP / 2, self.rect.height / 2)))

__all__ = ["QuizButton"]

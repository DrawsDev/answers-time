import pygame
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.layout import Layout

class UIExitWarn:
    def __init__(self, game: Game):
        self.game = game
        self.layout = Layout(False)
        self.pos = (game.surface.get_width() / 2, game.surface.get_height() / 2)
        self._create_warn_1_label()
        self._create_warn_2_label()
        self._create_no_button()
        self._create_yes_button()
        self.layout.insert_child(self.warn_1, self.warn_2, self.no, self.yes)

    def _create_warn_1_label(self) -> None:
        self.warn_1 = TextLabel(
            game=self.game,
            text="Вы уверены, что хотите выйти?",
            position=(self.pos[0], self.pos[1] - 20),
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.game.surface.get_width()
        )
    
    def _create_warn_2_label(self) -> None:
        self.warn_2 = TextLabel(
            game=self.game,
            text="Все несохранённые изменения будут потеряны.",
            position=(self.pos[0], self.pos[1]),
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="red",
            text_wraplength=self.game.surface.get_width()
        )
    
    def _create_no_button(self) -> None:
        self.no = TextButton(
            game=self.game,
            text="Нет",
            size=(130, 40),
            position=(self.pos[0] - 2, self.pos[1] + 20),
            anchor=Anchor.TopRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "test2.png")
        )
    
    def _create_yes_button(self) -> None:
        self.yes = TextButton(
            game=self.game,
            text="Да",
            size=(130, 40),
            position=(self.pos[0] + 3, self.pos[1] + 20),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "test2.png")
        )

__all__ = ["UIExitWarn"]

import pygame
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.layout import Layout
from src.ui.text_box import TextBox

class UIQuizInfo:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.layout = Layout(False)
        self.pos = (game.surface.get_width() / 2, game.surface.get_height() / 2)
        self._create_title_label()
        self._create_description_label()
        self._create_author_label()
        self._create_back_button()
        self._create_rule_button()
        self._create_title_input()
        self._create_description_input()
        self._create_author_input()
        self.layout.insert_child(
            self.title, 
            self.description, 
            self.author, self.back, 
            self.rule, 
            self.title_input, 
            self.description_input, 
            self.author_input
        )

    def _create_title_label(self) -> None:
        self.title = TextLabel(
            game=self.game,
            text="Название теста:",
            position=(self.pos[0] - 40, self.pos[1] - 75),
            anchor=Anchor.MidRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color="white",
            text_wraplength=self.game.surface.get_width()
        )

    def _create_description_label(self) -> None:
        self.description = TextLabel(
            game=self.game,
            text="Описание теста:",
            position=(self.pos[0] - 40, self.pos[1] - 30),
            anchor=Anchor.MidRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color="white",
            text_wraplength=self.game.surface.get_width()
        )

    def _create_author_label(self) -> None:
        self.author = TextLabel(
            game=self.game,
            text="Автор теста:",
            position=(self.pos[0] - 40, self.pos[1] + 15),
            anchor=Anchor.MidRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color="white",
            text_wraplength=self.game.surface.get_width()
        )

    def _create_title_input(self) -> None:
        self.title_input = TextBox(
            game=self.game,
            text="",
            placeholder="Введите название",
            size=(200, 40),
            position=(self.pos[0] - 20, self.pos[1] - 75),
            anchor=Anchor.MidLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color="white"
        )

    def _create_description_input(self) -> None:
        self.description_input = TextBox(
            game=self.game,
            text="",
            placeholder="Введите описание",
            size=(200, 40),
            position=(self.pos[0] - 20, self.pos[1] - 30),
            anchor=Anchor.MidLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color="white"
        )

    def _create_author_input(self) -> None:
        self.author_input = TextBox(
            game=self.game,
            text="",
            placeholder="Введите автора",
            size=(200, 40),
            position=(self.pos[0] - 20, self.pos[1] + 15),
            anchor=Anchor.MidLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color="white"
        )

    def _create_back_button(self) -> None:
        self.back = TextButton(
            game=self.game,
            text="Назад",
            size=(130, 40),
            position=(self.game.surface.get_width() / 2, self.game.surface.get_height()),
            anchor=Anchor.MidBottom,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "back.png")
        )

    def _create_rule_button(self) -> None:
        self.rule = TextButton(
            game=self.game,
            text="Правила",
            size=(130, 40),
            position=(self.pos[0], self.pos[1] + 40),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "settings.png")
        )

__all__ = ["UIQuizInfo"]    

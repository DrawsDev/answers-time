import pygame
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.layout import Layout

class UIEditor:
    def __init__(self, game: Game):
        self.game = game
        self.layout = Layout(True)
        self._create_menu_button()
        self.layout.insert_child(self.menu)

    def _create_menu_button(self) -> None:
        self.menu = TextButton(
            game=self.game,
            text="",
            size=(34, 34),
            position=(5, 5),
            anchor=Anchor.TopLeft,
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "tutorial.png")
        )

__all__ = ["UIEditor"]

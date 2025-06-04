import pygame
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.layout import Layout

GAP = 4

class UIEditor:
    def __init__(self, game: Game):
        self.game = game
        self._enabled = True
        self._layout = Layout(True)
        self._create_menu_button()
        self._create_question_settings_button()
        self._create_new_question_button()
        self._create_delete_question_button()
        self._layout.insert_child(
            self.menu,
            self.settings,
            self.new,
            self.delete
        )

    @property
    def enabled(self) -> bool:
        return self._enabled
    
    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value
        self._layout.enabled = value

    def update(self, delta: float) -> None:
        if self._enabled:
            self._layout.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        if self._enabled:
            self._layout.draw(surface)

    def _create_menu_button(self) -> None:
        self.menu = TextButton(
            game=self.game,
            text="",
            size=(34, 34),
            position=(GAP, GAP),
            anchor=Anchor.TopLeft,
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "menu.png")
        )
    
    def _create_question_settings_button(self) -> None:
        self.settings = TextButton(
            game=self.game,
            text="",
            size=(34, 34),
            position=(GAP, self.menu.rect.bottom + GAP),
            anchor=Anchor.TopLeft,
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "settings.png")
        )    
    
    def _create_new_question_button(self) -> None:
        self.new = TextButton(
            game=self.game,
            text="",
            size=(34, 34),
            position=(GAP, self.settings.rect.bottom + GAP),
            anchor=Anchor.TopLeft,
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "add.png")
        )
    
    def _create_delete_question_button(self) -> None:
        self.delete = TextButton(
            game=self.game,
            text="",
            size=(34, 34),
            position=(GAP, self.new.rect.bottom + GAP),
            anchor=Anchor.TopLeft,
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "delete.png")
        )

__all__ = ["UIEditor"]

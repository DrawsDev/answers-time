import pygame
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.layout import Layout

GAP = 4

class UIResult:
    def __init__(self, game: Game) -> None:
        self.game = game
        self._enabled = False
        self._layout = Layout(False)
        self._create_rating_label()
        self._create_info_label()
        self._create_back_button()
        self._layout.insert_child(
            self.rating,
            self.info,
            self.back
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

    def _create_rating_label(self) -> TextLabel:
        self.rating = TextLabel(
            game=self.game,
            text="5",
            position=(self.game.surface.get_width() / 2, self.game.surface.get_height() / 2 - 20),
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=55,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.game.surface.get_width()
        )

    def _create_info_label(self) -> TextLabel:
        self.info = TextLabel(
            game=self.game,
            text="Правильных ответов: 0 из 0",
            position=(self.rating.rect.centerx, self.rating.rect.bottom + 10),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.game.surface.get_width()
        )

    def _create_back_button(self) -> None:
        self.back = TextButton(
            game=self.game,
            text="Выйти",
            size=(130, 40),
            position=(self.game.surface.get_width() / 2, self.game.surface.get_height() - GAP),
            anchor=Anchor.MidBottom,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset("back.png")
        )

__all__ = ["UIResult"]

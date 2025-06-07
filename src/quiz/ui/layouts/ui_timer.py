import pygame
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.layout import Layout

GAP = 4

class UITimer:
    def __init__(self, game: Game) -> None:
        self.game = game
        self._enabled = True
        self._layout = Layout(True)
        self._create_timer_label()
        self._layout.insert_child(
            self.timer
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

    def _create_timer_label(self) -> TextLabel:
        self.timer = TextLabel(
            game=self.game,
            text="Оставшееся время: 0 с",
            position=(self.game.surface.get_width() - GAP, GAP),
            anchor=Anchor.TopRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Right,
            text_color="white",
            text_wraplength=self.game.surface.get_width()
        )

__all__ = ["UITimer"]

import pygame
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.frame import Frame
from src.ui.layout import Layout

GAP = 4

class UITip:
    def __init__(self, game: Game) -> None:
        self.game = game
        self._enabled = False
        self._layout = Layout(False)
        self._create_text_label()
        self._create_title_line()
        self._create_title_label()
        self._create_back_button()
        self._layout.insert_child(
            self.text,
            self.title,
            self.title_line,
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

    def set_tip(self, text: str) -> None:
        if self.text.text != text:
            self.text.text = text

    def _create_title_label(self) -> TextLabel:
        self.title = TextLabel(
            game=self.game,
            text="Подсказка",
            position=(self.title_line.rect.centerx, self.title_line.rect.top),
            anchor=Anchor.MidBottom,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.game.surface.get_width()
        )
    
    def _create_title_line(self) -> Frame:
        self.title_line = Frame(
            game=self.game,
            color="white",
            size=(self.game.surface.get_width() / 2, 2),
            position=(self.text.rect.centerx, self.text.rect.top - GAP),
            anchor=Anchor.MidBottom
        )

    def _create_text_label(self) -> TextLabel:
        self.text = TextLabel(
            game=self.game,
            text="Текст подсказки",
            position=(self.game.surface.get_width() / 2, self.game.surface.get_height() / 2),
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.game.surface.get_width()
        )

    def _create_back_button(self) -> None:
        self.back = TextButton(
            game=self.game,
            text="Назад",
            size=(130, 40),
            position=(self.game.surface.get_width() / 2, self.game.surface.get_height() - GAP),
            anchor=Anchor.MidBottom,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#282835",
            button_icon=load_asset(SPRITES, "back.png")
        )

__all__ = ["UITip"]

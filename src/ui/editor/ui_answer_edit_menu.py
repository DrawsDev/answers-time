import pygame
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.image_label import ImageLabel
from src.ui.layout import Layout
from src.ui.scroll_frame import ScrollFrame
from src.ui.frame import Frame
from src.experimental.text_box import TextBox

GAP = 4

class UIAnswerEditMenu:
    def __init__(self, game: Game) -> None:
        self.game = game
        self._enabled = True
        self._layout = Layout(False)
        self._create_title_label()
        self._create_title_line()
        self._create_back_button()
        self._create_text_textbox()
        self._create_objective_button()
        self._layout.insert_child(
            self.title,
            self.title_line,
            self.back,
            self.text
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

    def _create_title_label(self) -> None:
        self.title = TextLabel(
            game=self.game,
            text="Настройка ответа",
            position=(self.game.surface.get_width() / 2, 0),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.game.surface.get_width()
        )
    
    def _create_title_line(self) -> None:
        self.title_line = Frame(
            game=self.game,
            color="white",
            size=(self.game.surface.get_width() - 10, 2),
            position=(self.title.rect.centerx, self.title.rect.bottom),
            anchor=Anchor.MidTop
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
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "back.png")
        )

    def _create_text_textbox(self) -> None:
        self.text = TextBox(
            game=self.game,
            text="",
            placeholder="Введите текст ответа",
            size=(300, 80),
            position=(self.game.surface.get_width() / 2, self.game.surface.get_height() / 2),
            anchor=Anchor.Center,
            z_index=1,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color="white"
        )

    def _create_objective_button(self) -> None:
        self.objective = TextButton(
            game=self.game,
            text="Выбор одного правильного ответа",
            size=(260, 40),
            position=(self.game.surface.get_width() / 2, self.game.surface.get_height() / 2 - 120),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "editor_objective.png")
        )

__all__ = ["UIAnswerEditMenu"]

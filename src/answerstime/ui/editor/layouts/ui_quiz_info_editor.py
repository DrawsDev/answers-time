import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *

GAP = 4

class UIQuizInfoEditor:
    def __init__(self, app: Application) -> None:
        self.app = app
        self._enabled = False
        self._layout = Layout(False)
        self.pos = (app.surface.get_width() / 2, app.surface.get_height() / 2)
        self._create_title_label()
        self._create_title_line()
        self._create_quiz_title_label()
        self._create_quiz_description_label()
        self._create_quiz_author_label()
        self._create_quiz_rules_button()
        self._create_quiz_title_input()
        self._create_quiz_description_input()
        self._create_quiz_author_input()
        self._create_back_button()
        self._layout.insert_child(
            self.title,
            self.title_line,
            self.title_label,
            self.title_input,
            self.description_label,
            self.description_input,
            self.author_label,
            self.author_input,
            self.rules,
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

    def _create_title_label(self) -> TextLabel:
        self.title = TextLabel(
            app=self.app,
            text="Информация о тесте",
            position=(self.app.surface.get_width() / 2, 0),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            text_wraplength=self.app.surface.get_width()
        )
    
    def _create_title_line(self) -> Frame:
        self.title_line = Frame(
            app=self.app,
            color=Pallete.White,
            size=(self.app.surface.get_width() - 10, 2),
            position=(self.title.rect.centerx, self.title.rect.bottom),
            anchor=Anchor.MidTop
        )

    def _create_back_button(self) -> None:
        self.back = TextButton(
            app=self.app,
            text="Назад",
            size=(130, 40),
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() - GAP),
            anchor=Anchor.MidBottom,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "back.png")
        )

    def _create_quiz_title_label(self) -> None:
        self.title_label = TextLabel(
            app=self.app,
            text="Название теста:",
            position=(self.pos[0] - 40, self.pos[1] - 75),
            anchor=Anchor.MidRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.White,
            text_wraplength=self.app.surface.get_width()
        )

    def _create_quiz_description_label(self) -> None:
        self.description_label = TextLabel(
            app=self.app,
            text="Описание теста:",
            position=(self.pos[0] - 40, self.pos[1] - 30),
            anchor=Anchor.MidRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.White,
            text_wraplength=self.app.surface.get_width()
        )

    def _create_quiz_author_label(self) -> None:
        self.author_label = TextLabel(
            app=self.app,
            text="Автор теста:",
            position=(self.pos[0] - 40, self.pos[1] + 15),
            anchor=Anchor.MidRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.White,
            text_wraplength=self.app.surface.get_width()
        )

    def _create_quiz_title_input(self) -> None:
        self.title_input = TextBox(
            app=self.app,
            text="",
            placeholder="Введите название",
            size=(200, 40),
            position=(self.pos[0] - 20, self.pos[1] - 75),
            anchor=Anchor.MidLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.White
        )

    def _create_quiz_description_input(self) -> None:
        self.description_input = TextBox(
            app=self.app,
            text="",
            placeholder="Введите описание",
            size=(200, 40),
            position=(self.pos[0] - 20, self.pos[1] - 30),
            anchor=Anchor.MidLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.White
        )

    def _create_quiz_author_input(self) -> None:
        self.author_input = TextBox(
            app=self.app,
            text="",
            placeholder="Введите автора",
            size=(200, 40),
            position=(self.pos[0] - 20, self.pos[1] + 15),
            anchor=Anchor.MidLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.White
        )

    def _create_quiz_rules_button(self) -> None:
        self.rules = TextButton(
            app=self.app,
            text="Правила",
            size=(130, 40),
            position=(self.pos[0], self.pos[1] + 40),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "settings.png")
        )

__all__ = ["UIQuizInfoEditor"]    

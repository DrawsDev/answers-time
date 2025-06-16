import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *

GAP = 4

class UINewQuestion:
    def __init__(self, app: Application) -> None:
        self.app = app
        self._enabled = True
        self._layout = Layout(False)
        self._create_title_label()
        self._create_title_line()
        self._create_back_button()
        self._create_objective_button()
        self._create_subjective_button()
        self._create_input_button()
        self._create_sequence_button()
        self._create_matching_button()
        self._layout.insert_child(
            self.title,
            self.title_line,
            self.back,
            self.objective,
            self.subjective,
            self.input,
            self.sequence,
            self.matching
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
            text="Выбор типа нового вопроса",
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

    def _create_objective_button(self) -> None:
        self.objective = TextButton(
            app=self.app,
            text="Выбор одного правильного ответа",
            size=(260, 40),
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() / 2 - 120),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "editor_objective.png")
        )

    def _create_subjective_button(self) -> None:
        self.subjective = TextButton(
            app=self.app,
            text="Выбор нескольких правильных ответов",
            size=(260, 40),
            position=(self.objective.rect.centerx, self.objective.rect.bottom + GAP),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "editor_subjective.png")
        )

    def _create_input_button(self) -> None:
        self.input = TextButton(
            app=self.app,
            text="Ввод правильного ответа с помощью клавиатуры",
            size=(260, 40),
            position=(self.subjective.rect.centerx, self.subjective.rect.bottom + GAP),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "editor_input.png")
        )

    def _create_sequence_button(self) -> None:
        self.sequence = TextButton(
            app=self.app,
            text="Установление правильной последовательности",
            size=(260, 40),
            position=(self.input.rect.centerx, self.input.rect.bottom + GAP),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "editor_sequence.png")
        )

    def _create_matching_button(self) -> None:
        self.matching = TextButton(
            app=self.app,
            text="Определение соответствия между вариантами",
            size=(260, 40),
            position=(self.sequence.rect.centerx, self.sequence.rect.bottom + GAP),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "editor_matching.png")
        )

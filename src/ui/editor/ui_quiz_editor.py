import pygame
from typing import List
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.callback import CallbackType
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.image_label import ImageLabel
from src.ui.layout import Layout
from src.ui.scroll_frame import ScrollFrame
from src.ui.frame import Frame
from src.experimental.text_box import TextBox
from src.quiz.question import Question
from src.editor.ui.new_answer_button import NewAnswerButton
from src.editor.ui.answer_object import AnswerObject

GAP = 4

class UIQuizEditor:
    def __init__(self, game: Game) -> None:
        self.game = game
        self._enabled = True
        self._layout = Layout(False)
        self._answers = []
        self._create_question_number_label()
        self._create_question_type_label()
        self._create_prev_button()
        self._create_next_button()
        self._create_question_title_input_box()
        self._layout.insert_child(
            self.question_number,
            self.question_type,
            self.prev,
            self.next,
            self.question_title,
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

    def create_answers(self, question: Question, edit_callback: CallbackType, delete_callback: CallbackType, new_callback: CallbackType) -> None:
        x = self.question_title.rect.centerx
        y = self.question_title.rect.bottom + GAP
        a = (Anchor.TopRight, Anchor.TopLeft, Anchor.TopRight, Anchor.TopLeft)
        p = ((x - GAP / 2, y), (x + GAP / 2, y), (x - GAP / 2, y + 90 + GAP), (x + GAP / 2, y + 90 + GAP))
        
        self._layout.remove_child(self._answers)
        self._answers.clear()

        for index, option in enumerate(question.options):
            if index > 3:
                continue
            button = AnswerObject(self.game, p[index], a[index])
            button.text.text = option
            button.edit.pressed_callback.set((edit_callback, (index,)))
            button.delete.pressed_callback.set((delete_callback, (index,)))
            self._answers.append(button)

        if len(question.options) < 4:
            for i in range(len(question.options), 4):
                button = NewAnswerButton(self.game, p[i], a[i])
                button.pressed_callback.set(new_callback)
                self._answers.append(button)
        
        self._layout.insert_child(self._answers)

    def _create_prev_button(self) -> TextLabel:
        self.prev = TextButton(
            game=self.game,
            text="",
            size=(34, 34),
            position=(self.question_number.rect.left, GAP),
            anchor=Anchor.TopRight,
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "editor_prev.png")
        )

    def _create_next_button(self) -> TextLabel:
        self.next = TextButton(
            game=self.game,
            text="",
            size=(34, 34),
            position=(self.question_number.rect.right, GAP),
            anchor=Anchor.TopLeft,
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "editor_next.png")
        )

    def _create_question_number_label(self) -> TextLabel:
        self.question_number = TextLabel(
            game=self.game,
            text="Вопрос 1",
            position=(self.game.surface.get_width() / 2, 11),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=160
        )

    def _create_question_type_label(self) -> TextLabel:
        self.question_type = TextLabel(
            game=self.game,
            text="Тип вопроса",
            position=(self.question_number.rect.centerx, self.question_number.rect.bottom + GAP),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=160
        )

    def _create_question_title_input_box(self) -> TextBox:
        self.question_title = TextBox(
            game=self.game,
            text="",
            placeholder="Введите текст вопроса",
            size=(500, 80),
            position=(self.question_type.rect.centerx, self.question_type.rect.bottom + GAP),
            anchor=Anchor.MidTop,
            z_index=1,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color="white"
        )

__all__ = ["UIQuizEditor"]

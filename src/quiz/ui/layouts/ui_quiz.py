import pygame
from typing import List
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.callback import CallbackType
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.layout import Layout
from src.experimental.text_box import TextBox
from src.quiz.ui.xbjective_answer import XobjectiveAnswer
from src.quiz.ui.input_answer import InputAnswer
from src.quiz.ui.sequence_answer import SequenceAnswer
from src.quiz.ui.matching_answer import MatchingAnswer
from src.quiz.quiz import Quiz

GAP = 4

class UIQuiz:
    def __init__(self, game: Game) -> None:
        self.game = game
        self._enabled = False
        self._layout = Layout(False)
        self._answers = []
        self._create_complete_button()
        self._create_question_number_label()
        self._create_question_title_label()
        self._create_answer_button()
        self._create_tip_button()
        self._create_skip_button()
        self._layout.insert_child(
            self.complete,
            self.question_number,
            self.question_title,
            self.answer,
            self.tip,
            self.skip
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

    def create_answers(self, quiz: Quiz, change_correct_callback: CallbackType) -> None:
        question = quiz.questions[quiz.question_index]
        recived = quiz.answers_recived
        
        x = self.question_title.rect.centerx
        y = self.question_title.rect.bottom + GAP
        if len(question.options) == 1:
            a = (Anchor.MidTop,)
            p = ((x, y),)
        elif len(question.options) == 2:
            a = (Anchor.TopRight, Anchor.TopLeft)
            p = ((x - GAP / 2, y), (x + GAP / 2, y))
        elif len(question.options) == 3:
            a = (Anchor.TopRight, Anchor.TopLeft, Anchor.MidTop)
            p = ((x - GAP / 2, y), (x + GAP / 2, y), (x, y + 90 + GAP))
        elif len(question.options) == 4:
            a = (Anchor.TopRight, Anchor.TopLeft, Anchor.TopRight, Anchor.TopLeft)
            p = ((x - GAP / 2, y), (x + GAP / 2, y), (x - GAP / 2, y + 90 + GAP), (x + GAP / 2, y + 90 + GAP))
        
        self._layout.remove_child(self._answers)
        self._answers.clear()

        if question.type == 0 or question.type == 1:
            for index, option in enumerate(question.shuffle_options):
                if index > 3:
                    continue
                button = XobjectiveAnswer(self.game, p[index], a[index])
                button.text.text = option
                button.is_right.pressed_callback.set((change_correct_callback, (index,)))
                button.change_correct_state(index in recived)
                self._answers.append(button)
        elif question.type == 2:
            button = InputAnswer(self.game, p[0], a[0])
            button.textbox.text = "" if len(recived) < 1 else str(recived[0])
            button.textbox.focus_lost_callback.set(change_correct_callback)
            self._answers.append(button)
        elif question.type == 3:
            for index, option in enumerate(question.shuffle_options):
                if index > 3:
                    continue
                button = SequenceAnswer(self.game, p[index], a[index])
                button.text.text = option
                button.move.pressed_callback.set((change_correct_callback, (index,)))
                button.change_number(index + 1)
                self._answers.append(button)
        elif question.type == 4:
            pos = ((x - 75 - GAP, y), (x, y), (x + 75 + GAP, y))
            anc = (Anchor.TopRight, Anchor.MidTop, Anchor.TopLeft)

            for index, option in enumerate(question.shuffle_options):
                if index > 2:
                    continue
                button = MatchingAnswer(self.game, pos[index], anc[index])
                button.text_1.text = option
                button.text_2.text = question.shuffle_answers[index]
                button.change_number(index + 1, 0)
                button.change_number(index + 1, 1)
                button.move_1.pressed_callback.set((change_correct_callback, (index, 0)))
                button.move_2.pressed_callback.set((change_correct_callback, (index, 1)))
                self._answers.append(button)
        
        self._layout.insert_child(self._answers)

    def _create_input_answer(self, callback: CallbackType) -> None:
        x = self.question_title.rect.centerx
        y = self.question_title.rect.bottom + 40 + GAP
        textbox = TextBox(
            game=self.game,
            text="",
            placeholder="Введите ваш ответ",
            size=(300, 80),
            position=(x, y),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color="white"
        )
        textbox.focus_lost_callback.set((callback, (textbox.text,)))
        self._answers.append(textbox)

    def _create_complete_button(self) -> None:
        self.complete = TextButton(
            game=self.game,
            text="",
            size=(34, 34),
            position=(GAP, GAP),
            anchor=Anchor.TopLeft,
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "exit.png")
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
            text_wraplength=self.game.surface.get_width()
        )

    def _create_question_title_label(self) -> TextLabel:
        self.question_title = TextLabel(
            game=self.game,
            text="Текст вопроса",
            position=(self.game.surface.get_width() / 2, 42),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.game.surface.get_width()
        )

    def _create_answer_button(self) -> None:
        self.answer = TextButton(
            game=self.game,
            text="Ответить",
            size=(130, 40),
            position=(self.game.surface.get_width() / 2, self.game.surface.get_height() - GAP),
            anchor=Anchor.MidBottom,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000"
        )

    def _create_tip_button(self) -> None:
        self.tip = TextButton(
            game=self.game,
            text="Подсказка",
            size=(130, 40),
            position=(self.answer.rect.left - GAP, self.answer.rect.centery),
            anchor=Anchor.MidRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000"
        )

    def _create_skip_button(self) -> None:
        self.skip = TextButton(
            game=self.game,
            text="Пропустить",
            size=(130, 40),
            position=(self.answer.rect.right + GAP, self.answer.rect.centery),
            anchor=Anchor.MidLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000"
        )

__all__ = ["UIQuiz"]

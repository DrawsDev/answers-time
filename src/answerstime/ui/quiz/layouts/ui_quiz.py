import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.callback import CallbackType
from src.framework.utility import *
from src.framework.scene.ui import *
from src.answerstime.ui.quiz import *
from src.answerstime.quiz import Quiz

GAP = 4

class UIQuiz:
    def __init__(self, app: Application) -> None:
        self.app = app
        self._enabled = False
        self._layout = Layout(False)
        self._answers = []
        self._create_complete_button()
        self._create_question_number_label()
        self._create_question_title_frame()
        self._create_question_title_label()
        self._create_answer_button()
        self._create_tip_button()
        self._create_skip_button()
        self._layout.insert_child(
            self.complete,
            self.question_number,
            self.question_frame,
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
        
        x = self.question_frame.rect.centerx
        y = self.question_frame.rect.bottom + GAP
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
                button = XobjectiveAnswer(self.app, p[index], a[index])
                button.text.text = option
                button.is_right.pressed_callback.set((change_correct_callback, (index,)))
                button.change_correct_state(index in recived)
                self._answers.append(button)
        elif question.type == 2:
            button = InputAnswer(self.app, p[0], a[0])
            button.textbox.text = "" if len(recived) < 1 else str(recived[0])
            button.textbox.focus_lost_callback.set(change_correct_callback)
            self._answers.append(button)
        elif question.type == 3:
            for index, option in enumerate(question.shuffle_options):
                if index > 3:
                    continue
                button = SequenceAnswer(self.app, p[index], a[index])
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
                button = MatchingAnswer(self.app, pos[index], anc[index])
                button.text_1.text = option
                button.text_2.text = question.shuffle_answers[index]
                button.change_number(index + 1, 0)
                button.change_number(index + 1, 1)
                button.move_1.pressed_callback.set((change_correct_callback, (index, 0)))
                button.move_2.pressed_callback.set((change_correct_callback, (index, 1)))
                self._answers.append(button)
        
        self._layout.insert_child(self._answers)

    def _create_complete_button(self) -> None:
        self.complete = TextButton(
            app=self.app,
            text="Закончить",
            size=(120, 40),
            position=(GAP, GAP),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_icon=load_asset(SPRITES, "exit.png"),
            button_border_radius=6
        )

    def _create_question_number_label(self) -> TextLabel:
        self.question_number = TextLabel(
            app=self.app,
            text="Вопрос 0 из 0",
            position=(self.app.surface.get_width() / 2, 11),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            text_wraplength=self.app.surface.get_width()
        )

    def _create_question_title_frame(self) -> None:
        self.question_frame = Frame(
            app=self.app,
            color=Pallete.ATBlue3,
            size=(404, 76),
            position=(self.app.surface.get_width() / 2, self.complete.rect.bottom + GAP),
            anchor=Anchor.MidTop,
            z_index=-1,
            border_width=4,
            border_radius=6
        )

    def _create_question_title_label(self) -> None:
        self.question_title = TextLabel(
            app=self.app,
            text="Текст вопроса",
            position=(self.question_frame.rect.centerx, self.question_frame.rect.y + self.question_frame.rect.height / 2),
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            text_wraplength=self.question_frame.rect.width - GAP
        )

    def _create_answer_button(self) -> None:
        self.answer = TextButton(
            app=self.app,
            text="Ответить",
            size=(130, 40),
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() - GAP),
            anchor=Anchor.MidBottom,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_border_radius=6
        )

    def _create_tip_button(self) -> None:
        self.tip = TextButton(
            app=self.app,
            text="Подсказка",
            size=(130, 40),
            position=(self.answer.rect.left - GAP, self.answer.rect.centery),
            anchor=Anchor.MidRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_border_radius=6
        )

    def _create_skip_button(self) -> None:
        self.skip = TextButton(
            app=self.app,
            text="Пропустить",
            size=(130, 40),
            position=(self.answer.rect.right + GAP, self.answer.rect.centery),
            anchor=Anchor.MidLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_border_radius=6
        )

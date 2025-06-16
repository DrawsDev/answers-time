import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.callback import CallbackType
from src.framework.utility import *
from src.framework.scene.ui import *
from src.answerstime.ui.editor import *
from src.answerstime.question import Question

GAP = 4

class UIQuizEditor:
    def __init__(self, app: Application) -> None:
        self.app = app
        self._enabled = True
        self._layout = Layout(False)
        self._answers = []
        self._create_menu_button()
        self._create_question_settings_button()
        self._create_new_question_button()
        self._create_delete_question_button()
        self._create_question_number_label()
        self._create_question_type_label()
        self._create_prev_button()
        self._create_next_button()
        self._create_question_title_input_box()
        self._layout.insert_child(
            self.menu,
            self.settings,
            self.new,
            self.delete,
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

    def create_answers(self, question: Question, edit_callback: CallbackType, delete_callback: CallbackType, move_callback: CallbackType, change_correct_callback: CallbackType, new_callback: CallbackType) -> None:
        x = self.question_title.rect.centerx
        y = self.question_title.rect.bottom + GAP
        a = (Anchor.TopRight, Anchor.TopLeft, Anchor.TopRight, Anchor.TopLeft)
        p = ((x - GAP / 2, y), (x + GAP / 2, y), (x - GAP / 2, y + 90 + GAP), (x + GAP / 2, y + 90 + GAP))
        
        self._layout.remove_child(self._answers)
        self._answers.clear()

        if question.type in (0, 1):
            for index, option in enumerate(question.options):
                if index > 3:
                    continue
                button = XbjectiveAnswer(self.app, p[index], a[index])
                button.text.text = option
                button.edit.pressed_callback.set((edit_callback, (index,)))
                button.delete.pressed_callback.set((delete_callback, (index,)))
                button.move.pressed_callback.set((move_callback, (index,)))
                button.is_right.pressed_callback.set((change_correct_callback, (index,)))
                button.change_correct_state(index in question.answers)
                self._answers.append(button)

            if len(question.options) < 4:
                for i in range(len(question.options), 4):
                    button = NewAnswerButton(self.app, (200, 90), p[i], a[i])
                    button.pressed_callback.set(new_callback)
                    self._answers.append(button)
        elif question.type == 2:
            for index, option in enumerate(question.options):
                if index > 3:
                    continue
                button = InputAnswer(self.app, p[index], a[index])
                button.text.text = option
                button.edit.pressed_callback.set((edit_callback, (index,)))
                button.delete.pressed_callback.set((delete_callback, (index,)))
                self._answers.append(button)

            if len(question.options) < 4:
                for i in range(len(question.options), 4):
                    button = NewAnswerButton(self.app, (200, 90), p[i], a[i])
                    button.pressed_callback.set(new_callback)
                    self._answers.append(button)
        elif question.type == 3:
            for index, option in enumerate(question.options):
                if index > 3:
                    continue
                button = SequenceAnswer(self.app, p[index], a[index])
                button.text.text = option
                button.change_number(index + 1)
                button.delete.pressed_callback.set((delete_callback, (index,)))
                button.edit.pressed_callback.set((edit_callback, (index,)))
                button.move.pressed_callback.set((move_callback, (index,)))
                self._answers.append(button)

            if len(question.options) < 4:
                for i in range(len(question.options), 4):
                    button = NewAnswerButton(self.app, (200, 90), p[i], a[i])
                    button.pressed_callback.set(new_callback)
                    self._answers.append(button)
        elif question.type == 4:
            pos = ((x - 75 - GAP, y), (x, y), (x + 75 + GAP, y))
            anc = (Anchor.TopRight, Anchor.MidTop, Anchor.TopLeft)

            for index, option in enumerate(question.options):
                if index > 2:
                    continue
                button = MatchingAnswer(self.app, pos[index], anc[index])
                button.text_1.text = option
                button.text_2.text = question.answers[index]
                button.change_number(index + 1, 0)
                button.change_number(index + 1, 1)
                button.delete.pressed_callback.set((delete_callback, (index,)))
                button.edit.pressed_callback.set((edit_callback, (index,)))
                button.move.pressed_callback.set((move_callback, (index,)))
                self._answers.append(button)

            if len(question.options) < 3:
                for i in range(len(question.options), 3):
                    button = NewAnswerButton(self.app, (150, 185), pos[i], anc[i])
                    button.pressed_callback.set(new_callback)
                    self._answers.append(button)            

        self._layout.insert_child(self._answers)

    def _create_menu_button(self) -> None:
        self.menu = TextButton(
            app=self.app,
            text="",
            size=(34, 34),
            position=(GAP, GAP),
            anchor=Anchor.TopLeft,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "menu.png")
        )
    
    def _create_question_settings_button(self) -> None:
        self.settings = TextButton(
            app=self.app,
            text="",
            size=(34, 34),
            position=(GAP, self.menu.rect.bottom + GAP),
            anchor=Anchor.TopLeft,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "settings.png")
        )    
    
    def _create_new_question_button(self) -> None:
        self.new = TextButton(
            app=self.app,
            text="",
            size=(34, 34),
            position=(GAP, self.settings.rect.bottom + GAP),
            anchor=Anchor.TopLeft,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "add.png")
        )
    
    def _create_delete_question_button(self) -> None:
        self.delete = TextButton(
            app=self.app,
            text="",
            size=(34, 34),
            position=(GAP, self.new.rect.bottom + GAP),
            anchor=Anchor.TopLeft,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "delete.png")
        )

    def _create_prev_button(self) -> TextLabel:
        self.prev = TextButton(
            app=self.app,
            text="",
            size=(34, 34),
            position=(self.question_number.rect.left, GAP),
            anchor=Anchor.TopRight,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "editor_prev.png")
        )

    def _create_next_button(self) -> TextLabel:
        self.next = TextButton(
            app=self.app,
            text="",
            size=(34, 34),
            position=(self.question_number.rect.right, GAP),
            anchor=Anchor.TopLeft,
            button_color=Pallete.Gray2,
            button_hover_color=Pallete.Gray1,
            button_press_color=Pallete.Gray3,
            button_icon=load_asset(SPRITES, "editor_next.png")
        )

    def _create_question_number_label(self) -> TextLabel:
        self.question_number = TextLabel(
            app=self.app,
            text="Вопрос 1",
            position=(self.app.surface.get_width() / 2, 11),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            text_wraplength=160
        )

    def _create_question_type_label(self) -> TextLabel:
        self.question_type = TextLabel(
            app=self.app,
            text="Тип вопроса",
            position=(self.question_number.rect.centerx, self.question_number.rect.bottom + GAP),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            text_wraplength=160
        )

    def _create_question_title_input_box(self) -> TextBox:
        self.question_title = TextBox(
            app=self.app,
            text="",
            placeholder="Введите текст вопроса",
            size=(500, 80),
            position=(self.question_type.rect.centerx, self.question_type.rect.bottom + GAP),
            anchor=Anchor.MidTop,
            z_index=1,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.White,
            line_length=10
        )

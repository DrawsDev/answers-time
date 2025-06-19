import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene import Scene
from src.framework.scene.ui import *
from src.answerstime.ui import Background

GAP = 4

class Tutorial(Scene):
    def __init__(self, app: Application):
        self.app = app
        self._create_complete_button()
        self._create_question_number_label()
        self._create_question_type_label()
        self._create_question_title_frame()
        self._create_question_title_label()
        self._create_answer_button()
        self._create_tip_button()
        self._create_skip_button()
        self._create_timer_button()
        self.background = Background(load_asset(SPRITES, "quiz_background.png"), 0, 10)
        self.ui_group = pygame.sprite.Group()
        self.label = TextLabel(app, anchor=Anchor.Center, text_wraplength=350)
        self.label.position = [self.app.surface.get_width() / 2, self.app.surface.get_height() / 2]
        self.label.font_align = Align.Center
        self.label2 = TextLabel(
            app,
            text="[Нажмите любую кнопку, чтобы продолжить]",
            anchor=Anchor.MidTop, 
            font_size=16,
            text_color=Pallete.ATBlue2,
            text_wraplength=350, 
            position=[self.app.surface.get_width() / 2, self.app.surface.get_height() / 2],
            font_align=Align.Center
        )
        self.ui_group.add(self.label, self.label2)
        self.dialogues = [
            "Привет, давай вкратце познакомимся с интерфейсом тестирования.",
            "Сверху по центру располагаются номер вопроса и его тип.",
            "Сразу под ними - текст вопроса.",
            "Далее идут варианты ответов, которые различаются в зависимости от типа вопроса.",
            "Например, в вопросе, где нужно выбрать вариант ответа, необходимо навестись на ответ и нажать на появившуюся кнопку с галочкой.",
            "В самом низу расположены три основные кнопки:",
            '"Ответить" - нажимается в том случае, когда выбран или введён ответ, установлена последовательность и так далее, чтобы ответить на вопрос и перейти к следующему.',
            '"Подсказка" - нажимается тогда, когда требуется подсказка к ответу, но не всегда текст подсказки может быть установлен.',
            '"Пропустить" - нажимается в том случае, когда нет уверенности в правильности ответа на текущий вопрос.',
            "Все пропущенные вопросы выводятся в конце, после ответа на остальные непропущенные вопросы.",
            'Если есть необходимость преждевременно закончить тестирование, для этого слева сверху есть кнопка "Закончить".',
            "Тесты чаще всего ограничиваются по времени. Счет оставшегося времени можно увидеть справа сверху.",
            "Как только время истекает, тестирование прекращается.",
            "Надеюсь, теперь у тебя появилось лучшее представление о том, как проходятся тесты. Успехов!"
        ]
        self.dialogue_index = 0
        self.label.text = self.dialogues[self.dialogue_index]
        self.label2.position = self.label.rect.midbottom

    def update(self, delta):
        self.background.update(delta)
        self.ui_group.update(delta)
        if self.app.input.is_anything_pressed():
            if self.dialogue_index >= len(self.dialogues) - 1:
                self.app.change_scene("Menu")
            else:
                self.dialogue_index += 1
                self.label.text = self.dialogues[self.dialogue_index]
                self.label2.position = self.label.rect.midbottom
                if self.dialogue_index == 1:
                    self.ui_group.add(self.question_number, self.question_type)
                elif self.dialogue_index == 2:
                    self.ui_group.add(self.question_frame, self.question_title)
                elif self.dialogue_index == 3:
                    pass
                elif self.dialogue_index == 4:
                    pass
                elif self.dialogue_index == 5:
                    pass
                elif self.dialogue_index == 6:
                    self.ui_group.add(self.answer)
                elif self.dialogue_index == 7:
                    self.ui_group.add(self.tip)
                elif self.dialogue_index == 8:
                    self.ui_group.add(self.skip)
                elif self.dialogue_index == 9:
                    pass
                elif self.dialogue_index == 10:
                    self.ui_group.add(self.complete)
                elif self.dialogue_index == 11:
                    self.ui_group.add(self.timer)

    def draw(self, surface):
        surface.fill(Pallete.ATBlue5)
        self.background.draw(surface)
        self.ui_group.draw(surface)

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
            text="Вопрос 1 из 10",
            position=(self.app.surface.get_width() / 2, 2),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            text_wraplength=self.app.surface.get_width()
        )

    def _create_question_type_label(self) -> TextLabel:
        self.question_type = TextLabel(
            app=self.app,
            text="Выберите один правильный ответ",
            position=(self.app.surface.get_width() / 2, self.question_number.rect.bottom),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.ATBlue2,
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

    def _create_timer_button(self) -> None:
        self.timer = TextButton(
            app=self.app,
            text="10:00",
            size=(120, 40),
            position=(self.app.surface.get_width() - GAP, GAP),
            anchor=Anchor.TopRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue3,
            button_press_color=Pallete.ATBlue3,
            button_icon=load_asset(SPRITES, "timer.png"),
            button_border_radius=6
        )

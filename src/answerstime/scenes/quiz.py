import time
import copy
import pygame
from typing import Union
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene import Scene
from src.framework.scene.ui import *
from src.answerstime.ui.quiz.layouts import *
from src.answerstime.ui import Background
from src.answerstime.quiz import Quiz as QuizObject
from src.answerstime.utility import *

class Quiz(Scene):
    def __init__(self, app: Application) -> None:
        self.app = app
        self.quiz: QuizObject = None
        self.background = Background(load_asset(SPRITES, "quiz_background.png"), 0, 10)
        self.ui_quiz = UIQuiz(app)
        self.ui_result = UIResult(app)
        self.ui_timer = UITimer(app)
        self.ui_tip = UITip(app)
        self.ui_registration = UIRegistration(app)
        self.warning = Warning(app, "Вы уверены, что хотите прервать тестирование?", "")
        self.notification = Notification(app)

    def on_enter(self, **kwargs):
        filename = kwargs.get("filename")
        if not filename:
            self._quit_quiz()
        
        quiz: QuizObject = create_quiz_from_file(asset_path(QUIZZES, filename))
        if len(quiz.questions) <= 0:
            self._quit_quiz()
        
        self._open_registration(quiz)
        self.ui_quiz.complete.pressed_callback.set(self._complete_quiz)
        self.ui_quiz.tip.pressed_callback.set(self._open_tip)
        self.ui_quiz.skip.pressed_callback.set(self._skip_question)
        self.ui_quiz.answer.pressed_callback.set(self._next_question)
        self.ui_result.back.pressed_callback.set(self._quit_quiz)
        self.warning.confirm_callback.set(self._show_result)
        self.warning.deny_callback.set(self._back_to_quiz)
        self.ui_tip.back.pressed_callback.set(self._back_to_quiz)

        # Окно регистрации
        self.ui_registration.back.pressed_callback.set(self._quit_quiz)
        self.ui_registration.start.pressed_callback.set((self._try_start_quiz, (quiz,)))

    def update(self, delta: float) -> None:
        self.background.update(delta)
        self.ui_quiz.update(delta)
        self.ui_result.update(delta)
        self.ui_tip.update(delta)
        self.ui_timer.update(delta)
        self.ui_registration.update(delta)
        self.warning.update(delta)
        self.notification.update(delta)
        if self.quiz:
            t = time.strftime("%H:%M:%S", time.gmtime(self.quiz.time_left))
            self.ui_timer.timer.text = str(t)
            if self.quiz.time_left <= 0:
                self._show_result()
    
    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(Pallete.ATBlue5)
        self.background.draw(surface)
        self.ui_quiz.draw(surface)
        self.ui_result.draw(surface)
        self.ui_tip.draw(surface)
        self.ui_registration.draw(surface)
        self.warning.draw(surface)
        self.notification.draw(surface)
        self.ui_timer.draw(surface)

    def _open_registration(self, quiz: QuizObject) -> None:
        self.notification.enabled = False
        self.notification.confirm_callback.set((self._open_registration, (quiz,)))
        self.ui_registration.enabled = True

    def _try_start_quiz(self, quiz: QuizObject) -> None:
        if len(self.ui_registration.name_input.text.replace(" ", "")) <= 0:
            self.notification.enabled = True
            self.notification.text = "Введено пустое имя."
            self.ui_registration.enabled = False
            self.ui_registration.name_input.text = ""
        else:
            self._start_quiz(quiz)
            self.quiz.tester_name = self.ui_registration.name_input.text
            self.ui_registration.enabled = False

    def _show_result(self) -> None:
        self.quiz.stop()
        self.warning.enabled = False
        self.ui_quiz.enabled = False
        self.ui_tip.enabled = False
        self.ui_result.enabled = True
        self.ui_result.grade.text = f"{self.quiz.get_grade()}%"
        self.ui_result.info.text = f"Отвеченных вопросов: {self.quiz.number_of_correct_answers} из {len(self.quiz.questions)}" 
        self.ui_result.info2.text = f"Правильных ответов: {self.quiz.number_of_correct_answers}"
        self.ui_result.info3.text = f"Неправильных ответов: {self.quiz.number_of_incorrect_answers}"
        self.ui_result.info4.text = f"Время выполнения тестирования: {time.strftime('%H:%M:%S', time.gmtime(self.quiz.end_time - self.quiz.start_time))}"
        self.ui_timer.enabled = False

    def _update_ui_question_info(self) -> None:
        question = self.quiz.questions[self.quiz.question_index]
        question_type_texts = ["Выберите один правильный ответ", "Выберите несколько правильных ответов", "Введите ответ при помощи клавиатуры", "Установите правильную последовательность", "Установите правильное соответствие"]
        self.ui_quiz.question_number.text = f"Вопрос {self.quiz.get_question_number()} из {len(self.quiz.questions)}"
        self.ui_quiz.question_type.text = question_type_texts[question.type]
        self.ui_quiz.question_title.text = question.title

        if self.quiz.question_index == len(self.quiz.questions) - 1:
            self.ui_quiz.answer.text = "Завершить"
        else:
            self.ui_quiz.answer.text = "Ответить"
        
        self.ui_quiz.create_answers(self.quiz, self._answer)

    def _answer(self, answer: Union[int, str], a = None) -> None:
        self.quiz.answer(answer, a)
        self._update_ui_question_info()

    def _next_question(self) -> None:
        if not self.quiz.is_answered():
            self._open_no_answered_info()
            return
        self.quiz.next_question()
        if not self.quiz.ended:
            self._update_ui_question_info()
        else:
            self._show_result()

    def _skip_question(self) -> None:
        self.quiz.skip_question()
        self._update_ui_question_info()

    def _open_tip(self) -> None:
        self.ui_quiz.enabled = False
        self.ui_tip.enabled = True
        self.ui_tip.set_tip(self.quiz.questions[self.quiz.question_index].tip)

    def _open_no_answered_info(self) -> None:
        self.ui_quiz.enabled = False
        self.notification.enabled = True
        self.notification.text = "Не указан вариант ответа."
        self.notification.confirm_callback.set(self._back_to_quiz)

    def _back_to_quiz(self) -> None:
        self.ui_quiz.enabled = True
        self.ui_tip.enabled = False
        self.warning.enabled = False
        self.notification.enabled = False

    def _complete_quiz(self) -> None:
        self.ui_quiz.enabled = False
        self.warning.enabled = True
        self.warning.warn2 = f"Отвеченных вопросов: {len(self.quiz.answered_questions)} из {len(self.quiz.questions)}"

    def _start_quiz(self, quiz: QuizObject) -> None:
        self.quiz = copy.deepcopy(quiz)
        self.quiz.start()
        self.ui_quiz.enabled = True
        self.ui_timer.enabled = True
        self._update_ui_question_info()

    def _quit_quiz(self) -> None:
        self.app.change_scene("Menu")

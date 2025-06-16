import time
import copy
import pygame
from typing import Union
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene import Scene
from src.framework.scene.ui import *
from src.answerstime.ui.quiz.layouts import *
from src.answerstime.quiz import Quiz as QuizObject
from src.answerstime.utility import *

class Quiz(Scene):
    def __init__(self, app: Application) -> None:
        self.app = app
        self.quiz: QuizObject = None
        self.ui_quiz = UIQuiz(app)
        self.ui_result = UIResult(app)
        self.ui_timer = UITimer(app)
        self.ui_tip = UITip(app)
        self.warn = WarnFrame(app, "Вы уверены, что хотите прервать тестирование?", "")
        self.info = InfoFrame(app, "Не указан вариант ответа.")

    def on_enter(self, **kwargs):
        filename = kwargs.get("filename")
        if not filename:
            self._quit_quiz()
        
        quiz = create_quiz_from_file(asset_path(QUIZZES, filename))
        if len(quiz.questions) <= 0:
            self._quit_quiz()
        
        self._start_quiz(quiz)
        self.ui_quiz.complete.pressed_callback.set(self._complete_quiz)
        self.ui_quiz.tip.pressed_callback.set(self._open_tip)
        self.ui_quiz.skip.pressed_callback.set(self._skip_question)
        self.ui_quiz.answer.pressed_callback.set(self._next_question)
        self.ui_result.back.pressed_callback.set(self._quit_quiz)
        self.warn.confirm_callback.set(self._show_result)
        self.warn.deny_callback.set(self._back_to_quiz)
        self.ui_tip.back.pressed_callback.set(self._back_to_quiz)

    def update(self, delta: float) -> None:
        self.ui_quiz.update(delta)
        self.ui_result.update(delta)
        self.ui_tip.update(delta)
        self.ui_timer.update(delta)
        self.warn.update(delta)
        self.info.update(delta)
        if self.quiz:
            t = time.strftime("%H:%M:%S", time.gmtime(self.quiz.time_left))
            self.ui_timer.timer.text = f"Оставшееся время: {t}"
            if self.quiz.time_left <= 0:
                self.quiz.stop()
                self._show_result()
    
    def draw(self, surface: pygame.Surface) -> None:
        surface.fill("gray")
        self.ui_quiz.draw(surface)
        self.ui_result.draw(surface)
        self.ui_tip.draw(surface)
        self.warn.draw(surface)
        self.info.draw(surface)
        self.ui_timer.draw(surface)

    def _show_result(self) -> None:
        self.warn.enabled = False
        self.ui_quiz.enabled = False
        self.ui_tip.enabled = False
        self.ui_result.enabled = True
        self.ui_result.rating.text = f"{self.quiz.get_grade()}%"
        self.ui_result.info.text = f"Правильных ответов: {self.quiz.number_of_correct_answers} из {len(self.quiz.questions)}"        
        self.ui_timer.enabled = False

    def _update_ui_question_info(self) -> None:
        question = self.quiz.questions[self.quiz.question_index]
        self.ui_quiz.question_number.text = f"Вопрос {self.quiz.get_question_number()}"
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
        self.info.enabled = True
        self.info.confirm_callback.set(self._back_to_quiz)

    def _back_to_quiz(self) -> None:
        self.ui_quiz.enabled = True
        self.ui_tip.enabled = False
        self.warn.enabled = False
        self.info.enabled = False

    def _complete_quiz(self) -> None:
        self.ui_quiz.enabled = False
        self.warn.enabled = True
        self.warn.warn2 = f"Отвеченных вопросов: {len(self.quiz.answered_questions)} из {len(self.quiz.questions)}"

    def _start_quiz(self, quiz: Quiz) -> None:
        self.quiz = copy.deepcopy(quiz)
        self.quiz.start()
        self.ui_quiz.enabled = True
        self._update_ui_question_info()

    def _quit_quiz(self) -> None:
        self.app.change_scene("Menu")

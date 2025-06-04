import copy
import pygame
from typing import Union
from src.settings import *
from src.core.game import Game
from src.core.utility import asset_path
from src.components.scene import Scene
from src.quiz.utility import *
from src.quiz.ui.ui_quiz import UIQuiz
from src.quiz.ui.ui_result import UIResult
from src.ui.warn_frame import WarnFrame

class Quiz(Scene):
    def __init__(self, game: Game) -> None:
        self.game = game
        self.quiz = None
        self.ui_quiz = UIQuiz(game)
        self.ui_result = UIResult(game)
        self.warn = WarnFrame(game, "Вы хотите прервать тестирование?", "")

    def on_enter(self, **kwargs):
        filename = kwargs.get("filename")
        if not filename:
            self._quit_quiz()
        
        quiz = create_quiz_from_file(asset_path(QUIZZES, filename))
        if len(quiz.questions) <= 0:
            self._quit_quiz()
        
        self._start_quiz(quiz)
        self.ui_quiz.complete.pressed_callback.set(self._complete_quiz)
        self.ui_quiz.answer.pressed_callback.set(self._next_question)
        self.ui_result.back.pressed_callback.set(self._quit_quiz)
        self.warn.confirm_callback.set(self._show_result)
        self.warn.deny_callback.set(self._back_to_quiz)

    def update(self, delta: float) -> None:
        self.ui_quiz.update(delta)
        self.ui_result.update(delta)
        self.warn.update(delta)
    
    def draw(self, surface: pygame.Surface) -> None:
        surface.fill("gray")
        self.ui_quiz.draw(surface)
        self.ui_result.draw(surface)
        self.warn.draw(surface)

    def _show_result(self) -> None:
        self.warn.enabled = False
        self.ui_quiz.enabled = False
        self.ui_result.enabled = True
        self.ui_result.rating.text = f"{self.quiz.get_grade()}%"
        self.ui_result.info.text = f"Правильных ответов: {self.quiz.number_of_correct_answers} из {len(self.quiz.questions)}"        

    def _update_ui_question_info(self) -> None:
        question = self.quiz.questions[self.quiz.question_index]
        self.ui_quiz.question_number.text = f"Вопрос {self.quiz.question_index + 1}"
        self.ui_quiz.question_title.text = question.title

        if self.quiz.question_index == len(self.quiz.questions) - 1:
            self.ui_quiz.answer.text = "Завершить"
        else:
            self.ui_quiz.answer.text = "Ответить"
        
        self.ui_quiz.create_answers(question, self._answer)

    def _answer(self, answer: Union[int, str]) -> None:
        if type(answer) == str:
            answer = self.ui_quiz._answers[0].text
        self.quiz.answer(answer)

    def _next_question(self) -> None:
        self.quiz.next_question()
        if not self.quiz.ended:
            self._update_ui_question_info()
        else:
            self._show_result()

    def _back_to_quiz(self) -> None:
        self.ui_quiz.enabled = True
        self.warn.enabled = False

    def _complete_quiz(self) -> None:
        self.ui_quiz.enabled = False
        self.warn.enabled = True
        self.warn.warn2 = f"Отвеченных вопросов: {len(self.quiz.answered_questions)} из {len(self.quiz.questions)}"

    def _start_quiz(self, quiz: Quiz) -> None:
        self.quiz = copy.deepcopy(quiz)
        self.ui_quiz.enabled = True
        self._update_ui_question_info()

    def _quit_quiz(self) -> None:
        self.game.change_scene("Menu")

__all__ = ["Quiz"]

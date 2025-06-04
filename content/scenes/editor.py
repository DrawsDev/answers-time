import time
import json
import pygame
from typing import Dict
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.components.scene import Scene
from src.ui.debug_frame import DebugFrame
from src.ui.editor.ui_menu import UIMenu
from src.ui.editor.ui_editor import UIEditor
from src.ui.editor.ui_quiz_info import UIQuizInfo
from src.ui.explorer_frame import ExplorerFrame
from src.ui.warn_frame import WarnFrame
from src.ui.editor.ui_select_import_type import UISelectImportType
from src.ui.editor.ui_quiz_editor import UIQuizEditor
from src.ui.editor.ui_new_question import UINewQuestion
from src.ui.editor.ui_select_quiz_to_import import UISelectQuizToImport
from src.ui.editor.ui_answer_edit_menu import UIAnswerEditMenu
from src.quiz.quiz import *
from src.quiz.utility import *

class Editor(Scene):
    def __init__(self, game: Game) -> None:
        self.game = game
        self.current_question = -1
        self.quiz = Quiz()
        self.debug_frame = DebugFrame(game)
        self.explorer = ExplorerFrame(game, 1)
        self.warn = WarnFrame(game, "Вы уверены, что хотите выйти?", "Все несохранённые изменения будут потеряны.")
        self.ui_editor = UIEditor(game)
        self.ui_new_question = UINewQuestion(game)
        self.ui_select_import_type = UISelectImportType(game)
        self.ui_quiz_editor = UIQuizEditor(game)
        self.ui_select_quiz_to_import = UISelectQuizToImport(game)
        self.ui_answer_edit_menu = UIAnswerEditMenu(game)

        self.ui_menu = UIMenu(game)
        self.ui_quiz_info = UIQuizInfo(game)
        
    def on_enter(self, **kwargs) -> None:
        title = kwargs.get("title")
        filename = kwargs.get("filename")

        if title:
            self._create_quiz_with_title(title, False)
        elif filename:
            self._create_quiz_from_file(asset_path(QUIZZES, filename), False)
            self.ui_quiz_editor.enabled = True
        else:
            self._create_quiz_with_title("Новый тест", False)

        self.ui_menu.back.pressed_callback.set(self._open_quiz_editor)
        self.ui_menu.save.pressed_callback.set((self._save_quiz, (filename,)))
        self.ui_menu.info.pressed_callback.set(self._open_quiz_info)
        self.ui_menu.exit.pressed_callback.set(self._try_to_exit_editor)
        self.ui_menu.imp.pressed_callback.set(self._open_import_select_menu)
        self.ui_quiz_info.back.pressed_callback.set(self._open_menu)

        # Кнопки и поля в редакторе
        self.ui_editor.menu.pressed_callback.set(self._open_menu)
        self.ui_editor.new.pressed_callback.set(self._open_new_question)
        self.ui_editor.delete.pressed_callback.set(self._remove_current_question)
        self.ui_quiz_editor.prev.pressed_callback.set((self._move_to_next_question, (-1,)))
        self.ui_quiz_editor.next.pressed_callback.set((self._move_to_next_question, (1,)))
        self.ui_quiz_editor.question_title.focus_lost_callback.set(self._update_question_info)
        # Выбор типа нового вопроса
        self.ui_new_question.back.pressed_callback.set(self._open_quiz_editor)
        self.ui_new_question.objective.pressed_callback.set((self._create_new_question, (0,)))
        self.ui_new_question.subjective.pressed_callback.set((self._create_new_question, (1,)))
        self.ui_new_question.input.pressed_callback.set((self._create_new_question, (2,)))
        self.ui_new_question.sequence.pressed_callback.set((self._create_new_question, (3,)))
        self.ui_new_question.matching.pressed_callback.set((self._create_new_question, (4,)))
        # Настройка теста
        self.ui_quiz_info.title_input.focus_lost_callback.set(self._update_quiz_info)
        self.ui_quiz_info.description_input.focus_lost_callback.set(self._update_quiz_info)
        self.ui_quiz_info.author_input.focus_lost_callback.set(self._update_quiz_info)
        # Выбор типа импорта
        self.ui_select_import_type.back.pressed_callback.set(self._open_menu)
        self.ui_select_import_type.from_file.pressed_callback.set(self._open_import_explorer)
        self.ui_select_import_type.from_exists_quiz.pressed_callback.set(self._open_select_quiz_menu)
        # Импорт из существующего теста
        self.ui_select_quiz_to_import.back.pressed_callback.set(self._open_ui_select_quiz_to_import)
        # Проводник для импорта из файла системы
        self.explorer.close_callback.set((self._create_quiz_from_file, ("explorer", True)))
        self.explorer._cancel.pressed_callback.set(self._open_import_select_menu)
        # Настройка ответа
        self.ui_answer_edit_menu.back.pressed_callback.set(self._open_quiz_editor)

    def update(self, delta: float) -> None:
        self.debug_frame.update(delta)
        self.ui_menu.layout.update(delta)
        self.ui_quiz_info.layout.update(delta)
        self.warn.update(delta)
        self.explorer.update(delta)
        self.ui_editor.update(delta)
        self.ui_select_import_type.update(delta)
        self.ui_quiz_editor.update(delta)
        self.ui_new_question.update(delta)
        self.ui_select_quiz_to_import.update(delta)
        self.ui_answer_edit_menu.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill("gray")
        self.ui_menu.layout.draw(surface)
        self.ui_quiz_info.layout.draw(surface)
        self.warn.draw(surface)
        self.explorer.draw(surface)
        self.ui_editor.draw(surface)
        self.ui_select_import_type.draw(surface)
        self.ui_quiz_editor.draw(surface)
        self.ui_new_question.draw(surface)
        self.ui_select_quiz_to_import.draw(surface)
        self.ui_answer_edit_menu.draw(surface)
        self.debug_frame.draw(surface)

    def _remove_current_question(self) -> None:
        if len(self.quiz.questions) > 1:
            self.quiz.questions.pop(self.current_question)
            if self.current_question > 0:
                self.current_question -= 1
            self._update_ui_because_new_question()

    def _move_to_next_question(self, direction: int = 0) -> None:
        if direction != 0:
            self.current_question += direction
            if self.current_question < 0:
                self.current_question = len(self.quiz.questions) - 1
            if self.current_question > len(self.quiz.questions) - 1:
                self.current_question = 0
            self._update_ui_because_new_question()

    def _create_new_question(self, question_type: int = 0) -> None:
        self.quiz.questions.append(Question("Текст вопроса", question_type))
        self.current_question = len(self.quiz.questions) - 1
        self._update_ui_because_new_question()
        self._open_quiz_editor()

    def _update_quiz_info(self) -> None:
        text = self.ui_quiz_info.title_input.text
        description = self.ui_quiz_info.description_input.text
        author = self.ui_quiz_info.author_input.text 
        if len(text) > 0:
            self.quiz.title = text
        self.quiz.description = description
        self.quiz.author = author     

    def _update_question_info(self) -> None:
        title = self.ui_quiz_editor.question_title.text
        if len(title) > 0:
            self.quiz.questions[self.current_question].title = title

    def _update_ui_because_new_question(self) -> None:
        self.ui_quiz_editor.question_number.text = f"Вопрос {self.current_question + 1}"
        self.ui_quiz_editor.question_title.text = self.quiz.questions[self.current_question].title
        self.ui_quiz_editor.create_answers(self.quiz.questions[self.current_question], self._open_answer_edit_menu, self._delete_answer, self._create_new_answer)

        question_types = ("Один ответ", "Несколько ответов", "Свободный ответ", "Последовательность", "Соответствие")
        self.ui_quiz_editor.question_type.text = question_types[self.quiz.questions[self.current_question].type]

    def _update_ui_because_new_quiz(self) -> None:
        self.ui_quiz_info.title_input.text = self.quiz.title
        self.ui_quiz_info.description_input.text = self.quiz.description
        self.ui_quiz_info.author_input.text = self.quiz.author
        self._update_ui_because_new_question()

    def _delete_answer(self, answer_index: int) -> None:
        question = self.quiz.questions[self.current_question]
        if question.type in (0, 2):
            if len(question.options) > 1:
                self.quiz.questions[self.current_question].options.pop(answer_index)
                self._update_ui_because_new_question()
        elif question.type == 1:
            if len(question.options) > 2:
                self.quiz.questions[self.current_question].options.pop(answer_index)
                self._update_ui_because_new_question()

    def _create_new_answer(self) -> None:
        self.quiz.questions[self.current_question].options.append("Новый ответ")
        self._update_ui_because_new_question()

    def _create_quiz_with_title(self, title: str, menu: bool = False) -> None:
        self.quiz = Quiz(title)
        self._create_new_question(0)
        self._update_ui_because_new_quiz()
        if menu:
            self._open_menu()

    def _create_quiz_from_file(self, filepath: str, menu: bool = False) -> None:
        if filepath == "explorer": filepath = self.explorer._path
        self.quiz = create_quiz_from_file(filepath)
        self.current_question = 0
        self._update_ui_because_new_quiz()
        if menu:
            self._open_menu()

    def _save_quiz(self, filename: str = None) -> None:
        if filename:
            path = asset_path(QUIZZES, filename)
        else:
            filename = self.quiz.title.replace("\n", " ")
            filename = filename[:255]
            path = asset_path(QUIZZES, f"{filename}.json")
        with open(path, "w", encoding="utf-8") as file:
            json.dump(self.quiz.dump(), file, ensure_ascii=False)

    def _try_to_exit_editor(self) -> None:
        self.ui_editor.enabled = False
        self.ui_menu.layout.enabled = False
        self.ui_quiz_info.layout.enabled = False
        self.warn.enabled = True
        self.warn.confirm_callback.set(self._exit_editor)
        self.warn.deny_callback.set(self._open_menu)

    def _exit_editor(self) -> None:
        self.game.change_scene("Menu")
    
    def _open_quiz_editor(self) -> None:
        self.ui_editor.enabled = True
        self.ui_quiz_editor.enabled = True
        self.ui_new_question.enabled = False
        self.ui_menu.layout.enabled = False
        self.ui_answer_edit_menu.enabled = False

    def _open_menu(self) -> None:
        self.ui_menu.layout.enabled = True
        self.ui_editor.enabled = False
        self.ui_quiz_info.layout.enabled = False
        self.warn.enabled = False
        self.explorer.enabled = False
        self.ui_select_import_type.enabled = False
        self.ui_select_quiz_to_import.enabled = False
        self.ui_quiz_editor.enabled = False

    def _open_new_question(self) -> None:
        self.ui_editor.enabled = False
        self.ui_quiz_editor.enabled = False
        self.ui_new_question.enabled = True

    def _open_quiz_info(self) -> None:
        self.ui_editor.enabled = False
        self.ui_menu.layout.enabled = False
        self.ui_quiz_info.layout.enabled = True

    def _open_import_select_menu(self) -> None:
        self.ui_menu.layout.enabled = False
        self.ui_select_import_type.enabled = True
        self.ui_select_quiz_to_import.enabled = False
        self.explorer.enabled = False

    def _open_select_quiz_menu(self) -> None:
        self.ui_select_import_type.enabled = False
        self.ui_select_quiz_to_import.enabled = True
        self.ui_select_quiz_to_import.create_buttons(self._create_quiz_from_file)

    def _open_ui_select_quiz_to_import(self) -> None:
        self.ui_select_import_type.enabled = False
        self.ui_select_quiz_to_import.enabled = True

    def _open_import_explorer(self) -> None:
        self.ui_select_import_type.enabled = False
        self.explorer.enabled = True

    def _update_question_option(self, answer_index: int) -> None:
        self.quiz.questions[self.current_question].options[answer_index] = self.ui_answer_edit_menu.text.text
        self._update_ui_because_new_question()

    def _open_answer_edit_menu(self, answer_index: int) -> None:
        self.ui_editor.enabled = False
        self.ui_quiz_editor.enabled = False
        self.ui_answer_edit_menu.enabled = True

        question = self.quiz.questions[self.current_question]
        if question.type in (0, 1, 2):
            self.ui_answer_edit_menu.text.focus_lost_callback.set((self._update_question_option, (answer_index,)))

        self.ui_answer_edit_menu.text.text = question.options[answer_index]

__all__ = ["Editor"]

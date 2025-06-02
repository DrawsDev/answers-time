import json
import pygame
from typing import Dict, List, Any
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.components.scene import Scene
from src.ui.debug_frame import DebugFrame
from src.ui.editor.ui_menu import UIMenu
from src.ui.editor.ui_editor import UIEditor
from src.ui.editor.ui_exit_warn import UIExitWarn
from src.ui.editor.ui_quiz_info import UIQuizInfo

class Question:
    def __init__(self):
        self.title = "Текст вопроса"

class Quiz:
    def __init__(
        self,
        title: str = "Quiz title",
        description: str = "",
        author: str = "",
        questions: List[Question] = []
    ) -> None:
        self.title = title
        self.description = description
        self.author = author
        self.questions = questions
    
    def dump(self) -> Dict[str, Any]:
        return {
            "Title": self.title, 
            "Description": self.description, 
            "Author": self.author, 
            "Questions": self.questions
        }

class Editor(Scene):
    def __init__(self, game: Game) -> None:
        self.game = game
        self.debug_frame = DebugFrame(game)
        self.quiz = Quiz()

        self.ui_editor = UIEditor(game)
        self.ui_menu = UIMenu(game)
        self.ui_exit_warn = UIExitWarn(game)
        self.ui_quiz_info = UIQuizInfo(game)

    def on_enter(self, **kwargs) -> None:
        # def create_new_question() -> None:
        #     self.main_layout.remove(self.no_questions_button)
        #     self.question_layout.enabled = True
        #     self.questions.append(Question())
        #     self.current_question = len(self.questions) - 1
        #     self.question_number.text = f"Вопрос {self.current_question + 1}"

        def create_test(title: str) -> None:
            self.quiz = Quiz(title)

        def load_test(filename: str) -> None:
            with open(asset_path(QUIZZES, filename), "r", encoding="UTF8") as file:
                dump: Dict = json.load(file)
                title = dump.get("Title", "New quiz")
                description = dump.get("Description", "")
                author = dump.get("Author", "")
                questions = dump.get("Questions", [])
                self.quiz = Quiz(title, description, author, questions)

        def save_test(filename: str) -> None:
            with open(asset_path(QUIZZES, filename), "w", encoding="UTF8") as file:
                json.dump(self.quiz.dump(), file)

        title = kwargs.get("title")
        filename = kwargs.get("filename", "TEST.json")

        if title:
            create_test(title)
        elif filename:
            load_test(filename)

        def open_menu() -> None:
            self.ui_editor.layout.enabled = False
            self.ui_menu.layout.enabled = True
            self.ui_exit_warn.layout.enabled = False
            self.ui_quiz_info.layout.enabled = False
        
        def back_to_editor() -> None:
            self.ui_editor.layout.enabled = True
            self.ui_menu.layout.enabled = False
            self.ui_exit_warn.layout.enabled = False
            self.ui_quiz_info.layout.enabled = False

        def try_exit_editor() -> None:
            self.ui_editor.layout.enabled = False
            self.ui_menu.layout.enabled = False
            self.ui_exit_warn.layout.enabled = True
            self.ui_quiz_info.layout.enabled = False

        def open_quiz_info() -> None:
            self.ui_editor.layout.enabled = False
            self.ui_menu.layout.enabled = False
            self.ui_exit_warn.layout.enabled = False
            self.ui_quiz_info.layout.enabled = True            

        def exit_editor() -> None:
            self.game.change_scene("Menu")

        self.ui_editor.menu.pressed_callback = open_menu
        self.ui_menu.back.pressed_callback = back_to_editor
        self.ui_menu.save.pressed_callback = (save_test, (filename,))
        self.ui_menu.info.pressed_callback = open_quiz_info
        self.ui_menu.exit.pressed_callback = try_exit_editor
        self.ui_exit_warn.no.pressed_callback = open_menu
        self.ui_exit_warn.yes.pressed_callback = exit_editor
        self.ui_quiz_info.back.pressed_callback = open_menu

        self.ui_quiz_info.title_input.text = self.quiz.title
        self.ui_quiz_info.description_input.text = self.quiz.description
        self.ui_quiz_info.author_input.text = self.quiz.author

        def update_quiz_title() -> None:
            text = self.ui_quiz_info.title_input.text
            if len(text) > 0:
                self.quiz.title = text
        def update_quiz_description() -> None:
            self.quiz.description = self.ui_quiz_info.description_input.text
        def update_quiz_author() -> None:
            self.quiz.author = self.ui_quiz_info.author_input.text

        self.ui_quiz_info.title_input.focus_lost_callback = update_quiz_title
        self.ui_quiz_info.description_input.focus_lost_callback = update_quiz_description
        self.ui_quiz_info.author_input.focus_lost_callback = update_quiz_author

    def update(self, delta: float) -> None:
        self.debug_frame.update(delta)
        self.ui_menu.layout.update(delta)
        self.ui_editor.layout.update(delta)
        self.ui_exit_warn.layout.update(delta)
        self.ui_quiz_info.layout.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill("gray")
        self.ui_menu.layout.draw(surface)
        self.ui_editor.layout.draw(surface)
        self.ui_exit_warn.layout.draw(surface)
        self.ui_quiz_info.layout.draw(surface)
        self.debug_frame.draw(surface)

__all__ = ["Editor"]

import json
import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.utility import *
from src.framework.application import Application
from src.framework.scene import Scene
from src.framework.scene.ui import *
from src.answerstime.ui.editor.layouts import *
from src.answerstime.ui import Background
from src.answerstime.quiz import Quiz
from src.answerstime.question import Question
from src.answerstime.utility import *

QUESTION_TEXT = "Текст вопроса"
ANSWER_TEXT = "Текст ответа"

class Editor(Scene):
    def __init__(self, app: Application) -> None:
        self.app = app
        self.current_question = -1
        self.quiz = Quiz()
        self.background = Background(load_asset(SPRITES, "quiz_background.png"), 0, 10)
        self.debug_frame = DebugFrame(app)
        self.explorer = ExplorerFrame(app)
        self.warning = Warning(app)
        self.ui_menu = UIMenu(app)
        self.ui_quiz_editor = UIQuizEditor(app)
        self.ui_quiz_info_editor = UIQuizInfoEditor(app)
        self.ui_quiz_rules_editor = UIQuizRulesEditor(app)
        self.ui_new_question = UINewQuestion(app)        
        self.ui_question_settings = UIQuestionSettings(app)        
        self.ui_answer_edit_menu = UIAnswerEditMenu(app)
        self.ui_select_import_type = UISelectImportType(app)
        self.ui_select_quiz_to_import = UISelectQuizToImport(app)
        self.ui_select_export_type = UISelectExportType(app)
        
    def on_enter(self, **kwargs) -> None:
        title = kwargs.get("title")
        filename = kwargs.get("filename")

        if title:
            self._create_quiz_with_title(title)
        elif filename:
            self._create_quiz_from_file(asset_path(QUIZZES, filename))
            self.ui_quiz_editor.enabled = True
        else:
            self._create_quiz_with_title("Новый тест")

        # Меню
        self.ui_menu.back.pressed_callback.set(self._open_quiz_editor)
        self.ui_menu.save.pressed_callback.set((self._save_quiz, (filename,)))
        self.ui_menu.info.pressed_callback.set(self._open_quiz_info)
        self.ui_menu.exit.pressed_callback.set(self._try_to_exit_editor)
        self.ui_menu.imp.pressed_callback.set(self._open_import_select_menu)
        self.ui_menu.exp.pressed_callback.set(self._open_select_export_type_menu)

        # Кнопки и поля в редакторе
        self.ui_quiz_editor.menu.pressed_callback.set(self._open_menu)
        self.ui_quiz_editor.settings.pressed_callback.set(self._open_question_settings)
        self.ui_quiz_editor.new.pressed_callback.set(self._open_new_question)
        self.ui_quiz_editor.delete.pressed_callback.set(self._try_remove_current_question)
        self.ui_quiz_editor.prev.pressed_callback.set((self._move_to_next_question, (-1,)))
        self.ui_quiz_editor.next.pressed_callback.set((self._move_to_next_question, (1,)))
        self.ui_quiz_editor.question_title.focus_lost_callback.set(self._update_question_info)
        # Настройка информации о тесте
        self.ui_quiz_info_editor.title_input.focus_lost_callback.set(self._update_quiz_info)
        self.ui_quiz_info_editor.description_input.focus_lost_callback.set(self._update_quiz_info)
        self.ui_quiz_info_editor.author_input.focus_lost_callback.set(self._update_quiz_info)
        self.ui_quiz_info_editor.rules.pressed_callback.set(self._open_quiz_rules_editor)
        self.ui_quiz_info_editor.back.pressed_callback.set(self._open_menu)
        # Настройка правил теста
        self.ui_quiz_rules_editor.back.pressed_callback.set(self._open_quiz_info)
        # Выбор типа нового вопроса
        self.ui_new_question.back.pressed_callback.set(self._open_quiz_editor)
        self.ui_new_question.objective.pressed_callback.set((self._create_new_question, (0,)))
        self.ui_new_question.subjective.pressed_callback.set((self._create_new_question, (1,)))
        self.ui_new_question.input.pressed_callback.set((self._create_new_question, (2,)))
        self.ui_new_question.sequence.pressed_callback.set((self._create_new_question, (3,)))
        self.ui_new_question.matching.pressed_callback.set((self._create_new_question, (4,)))
        
        # Настройка вопроса
        self.ui_question_settings.back.pressed_callback.set(self._open_quiz_editor)
        self.ui_question_settings.tip_textbox.focus_lost_callback.set(self._update_question_tip)
       
        # Настройка ответа
        self.ui_answer_edit_menu.back.pressed_callback.set(self._open_quiz_editor)
        # Выбор типа импорта
        self.ui_select_import_type.back.pressed_callback.set(self._open_menu)
        self.ui_select_import_type.from_file.pressed_callback.set(self._open_import_explorer)
        self.ui_select_import_type.from_exists_quiz.pressed_callback.set(self._open_select_quiz_menu)
        # Импорт из существующего теста
        self.ui_select_quiz_to_import.back.pressed_callback.set(self._open_import_select_menu)

        # Меню выбора типа экспорта
        self.ui_select_export_type.back.pressed_callback.set(self._open_menu)
        self.ui_select_export_type.export_quiz_file.pressed_callback.set(self._open_export_explorer)

    def update(self, delta: float) -> None:
        self.debug_frame.update()
        self.background.update(delta)
        self.explorer.update(delta)
        self.warning.update(delta)
        self.ui_menu.update(delta)
        self.ui_quiz_editor.update(delta)
        self.ui_quiz_info_editor.update(delta)
        self.ui_quiz_rules_editor.update(delta)
        self.ui_new_question.update(delta)
        self.ui_question_settings.update(delta)
        self.ui_answer_edit_menu.update(delta)
        self.ui_select_import_type.update(delta)
        self.ui_select_quiz_to_import.update(delta)
        self.ui_select_export_type.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(Pallete.ATBlue5)
        self.background.draw(surface)
        self.ui_select_quiz_to_import.draw(surface)
        self.ui_select_import_type.draw(surface)
        self.ui_answer_edit_menu.draw(surface)
        self.ui_question_settings.draw(surface)
        self.ui_new_question.draw(surface)
        self.ui_quiz_rules_editor.draw(surface)
        self.ui_quiz_info_editor.draw(surface)
        self.ui_quiz_editor.draw(surface)
        self.ui_select_export_type.draw(surface)
        self.ui_menu.draw(surface)
        self.warning.draw(surface)
        self.explorer.draw(surface)
        self.debug_frame.draw(surface)

    def _update_quiz_editor_ui(self) -> None:
        index = self.current_question
        question = self.quiz.questions[index]
        question_types = ("Один ответ", "Несколько ответов", "Текстовый ответ", "Последовательность", "Соответствие")
        
        self.ui_quiz_editor.question_number.text = f"Вопрос {index + 1}"
        self.ui_quiz_editor.question_type.text = question_types[question.type]
        self.ui_quiz_editor.question_title.text = question.title
        self.ui_quiz_editor.create_answers(
            question, 
            self._open_answer_edit_menu, 
            self._try_remove_answer, 
            self._move_answer, 
            self._change_answer_correct_state, 
            self._create_new_answer
        )

    def _update_quiz_info_ui(self) -> None:
        self.ui_quiz_info_editor.title_input.text = self.quiz.title
        self.ui_quiz_info_editor.description_input.text = self.quiz.description
        self.ui_quiz_info_editor.author_input.text = self.quiz.author
        self._update_quiz_editor_ui()

    def _update_quiz_info(self, text: str) -> None:
        text = self.ui_quiz_info_editor.title_input.text
        description = self.ui_quiz_info_editor.description_input.text
        author = self.ui_quiz_info_editor.author_input.text 
        
        if len(text) > 0: 
            self.quiz.title = text
        self.quiz.description = description
        self.quiz.author = author   

    def _update_question_info(self, text: str) -> None:
        if len(text) > 0:
            self.quiz.questions[self.current_question].title = text

    def _create_new_question(self, question_type: int = 0) -> None:
        if question_type == 0:
            self.quiz.questions.append(Question(QUESTION_TEXT, question_type, [ANSWER_TEXT], []))
        elif question_type == 1:
            self.quiz.questions.append(Question(QUESTION_TEXT, question_type, [ANSWER_TEXT, ANSWER_TEXT], []))
        elif question_type == 2:
            self.quiz.questions.append(Question(QUESTION_TEXT, question_type, [ANSWER_TEXT], [0]))
        elif question_type == 3:
            self.quiz.questions.append(Question(QUESTION_TEXT, question_type, [ANSWER_TEXT, ANSWER_TEXT], [0, 1]))
        elif question_type == 4:
            self.quiz.questions.append(Question(QUESTION_TEXT, question_type, [ANSWER_TEXT, ANSWER_TEXT], [ANSWER_TEXT, ANSWER_TEXT]))
        self.current_question = len(self.quiz.questions) - 1
        self._update_quiz_editor_ui()
        self._open_quiz_editor()

    def _try_remove_current_question(self) -> None:
        if len(self.quiz.questions) > 1:
            self.ui_quiz_editor.enabled = False
            self.warning.enabled = True
            self.warning.warn1 = "Вы уверены, что хотите удалить вопрос?"
            self.warning.warn2 = "Данное действие невозможно будет отменить."
            self.warning.confirm_callback.set(self._remove_current_question)
            self.warning.deny_callback.set(self._open_quiz_editor)

    def _remove_current_question(self) -> None:
        if len(self.quiz.questions) > 1:
            self.quiz.questions.pop(self.current_question)
            if self.current_question > 0:
                self.current_question -= 1
            self._update_quiz_editor_ui()
            self._open_quiz_editor()

    def _update_question_option(self, answer_index: int, text: str) -> None:
        question = self.quiz.questions[self.current_question]
        question.options[answer_index] = text

        if question.type == 4:
            question.answers[answer_index] = text

        self._update_quiz_editor_ui()

    def _create_new_answer(self) -> None:
        question = self.quiz.questions[self.current_question]
        number_of_options = len(question.options)
        if question.type == 0 and number_of_options < 4:
            question.options.append(ANSWER_TEXT)
        elif question.type == 1 and number_of_options < 4:
            question.options.append(ANSWER_TEXT)
        elif question.type == 2 and number_of_options < 4:
            question.options.append(ANSWER_TEXT)
            question.answers.append(number_of_options - 1)
        elif question.type == 3 and number_of_options < 4:
            question.options.append(ANSWER_TEXT)
            question.answers.append(number_of_options - 1)
        elif question.type == 4 and number_of_options < 3:
            question.options.append(ANSWER_TEXT)
            question.answers.append(ANSWER_TEXT)
        self._update_quiz_editor_ui()

    def _try_remove_answer(self, answer_index: int) -> None:
        question = self.quiz.questions[self.current_question]
        number_of_options = len(question.options)
        if (question.type == 0 and number_of_options > 1) \
        or (question.type == 1 and number_of_options > 2) \
        or (question.type == 2 and number_of_options > 1) \
        or (question.type == 3 and number_of_options > 2) \
        or (question.type == 4 and number_of_options > 2):
            self.ui_quiz_editor.enabled = False
            self.warning.enabled = True
            self.warning.warn1 = "Вы уверены, что хотите удалить ответ?"
            self.warning.warn2 = "Данное действие невозможно будет отменить."
            self.warning.confirm_callback.set((self._remove_answer, (answer_index,)))
            self.warning.deny_callback.set(self._open_quiz_editor)

    def _remove_answer(self, answer_index: int) -> None:
        question = self.quiz.questions[self.current_question]
        number_of_options = len(question.options)
        if question.type == 0 and number_of_options > 1:
            new_options = question.options[:answer_index] + question.options[answer_index + 1:]
            new_answers = []
            for i in question.answers:
                if i > answer_index:
                    new_answers.append(i - 1)
                elif i < answer_index:
                    new_answers.append(i)
            question.options = new_options
            question.answers = new_answers
        elif question.type == 1 and number_of_options > 2:
            new_options = question.options[:answer_index] + question.options[answer_index + 1:]
            new_answers = []
            for i in question.answers:
                if i > answer_index:
                    new_answers.append(i - 1)
                elif i < answer_index:
                    new_answers.append(i)
            question.options = new_options
            question.answers = new_answers
        elif question.type == 2 and number_of_options > 1:
            question.options.pop(answer_index)
            question.answers.pop(answer_index)
        elif question.type == 3 and number_of_options > 2:
            question.options.pop(answer_index)
            question.answers.pop(answer_index)
        elif question.type == 4 and number_of_options > 2:
            question.options.pop(answer_index)
            question.answers.pop(answer_index)
        self._update_quiz_editor_ui()
        self._open_quiz_editor()

    def _move_answer(self, answer_index: int) -> None:
        question = self.quiz.questions[self.current_question]

        if question.type in (0, 1):
            if answer_index == 0:
                new_options = question.options[1:] + [question.options[0]]
                new_answers = []
                for i in question.answers:
                    if i == 0:
                        new_answers.append(len(question.options) - 1)
                    else:
                        new_answers.append(i - 1)
            else:
                new_options = question.options.copy()
                new_options[answer_index], new_options[answer_index - 1] = new_options[answer_index - 1], new_options[answer_index]
                new_answers = []
                for i in question.answers:
                    if i == answer_index:
                        new_answers.append(i - 1)
                    elif i == answer_index - 1:
                        new_answers.append(i + 1)
                    else:
                        new_answers.append(i)

            question.options = new_options
            question.answers = new_answers
        elif question.type == 3:
            if answer_index == 0:
                new_options = question.options[1:] + [question.options[0]]
            else:
                new_options = question.options.copy()
                new_options[answer_index], new_options[answer_index - 1] = new_options[answer_index - 1], new_options[answer_index]

            question.options = new_options
        elif question.type == 4:
            pass
        self._update_quiz_editor_ui()

    def _change_answer_correct_state(self, answer_index: int) -> None:
        question = self.quiz.questions[self.current_question]
        if question.type == 0:
            if answer_index in question.answers:
                question.answers.remove(answer_index)
            else:
                question.answers.clear()
                question.answers.append(answer_index)
            self._update_quiz_editor_ui()
        elif question.type == 1:
            if answer_index in question.answers:
                question.answers.remove(answer_index)
            else:
                question.answers.append(answer_index)
                question.answers.sort()
            self._update_quiz_editor_ui()            

    def _move_to_next_question(self, direction: int = 0) -> None:
        if direction != 0:
            self.current_question += direction
            if self.current_question < 0:
                self.current_question = len(self.quiz.questions) - 1
            if self.current_question > len(self.quiz.questions) - 1:
                self.current_question = 0
            self._update_quiz_editor_ui()

    def _create_quiz_with_title(self, title: str) -> None:
        self.quiz = Quiz(title)
        self.current_question = 0
        self._create_new_question(0)
        self._update_quiz_info_ui()
        self._open_quiz_editor()

    def _create_quiz_from_file(self, filepath: str) -> None:
        self.quiz = create_quiz_from_file(filepath)
        self.current_question = 0
        self._update_quiz_info_ui()
        self._open_quiz_editor()

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
        self.ui_menu.enabled = False
        self.ui_quiz_info_editor.enabled = False
        self.warning.enabled = True
        self.warning.warn1 = "Вы уверены, что хотите выйти?"
        self.warning.warn2 = "Все несохранённые изменения будут потеряны."
        self.warning.confirm_callback.set(self._exit_editor)
        self.warning.deny_callback.set(self._open_menu)

    def _exit_editor(self) -> None:
        self.app.change_scene("Menu")
    
    def _open_quiz_editor(self) -> None:
        self.ui_quiz_editor.enabled = True
        self.ui_new_question.enabled = False
        self.ui_menu.enabled = False
        self.ui_answer_edit_menu.enabled = False
        self.ui_select_quiz_to_import.enabled = False
        self.ui_question_settings.enabled = False
        self.warning.enabled = False

    def _open_menu(self) -> None:
        self.ui_menu.enabled = True
        self.ui_quiz_editor.enabled = False
        self.ui_quiz_info_editor.enabled = False
        self.warning.enabled = False
        self.ui_select_import_type.enabled = False
        self.ui_select_quiz_to_import.enabled = False
        self.ui_quiz_rules_editor.enabled = False
        self.ui_select_export_type.enabled = False

    def _open_new_question(self) -> None:
        self.ui_quiz_editor.enabled = False
        self.ui_new_question.enabled = True

    def _open_quiz_info(self) -> None:
        self.ui_menu.enabled = False
        self.ui_quiz_info_editor.enabled = True
        self.ui_quiz_rules_editor.enabled = False

    def _open_import_select_menu(self) -> None:
        self.ui_menu.enabled = False
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

    ###########################################
    #               Меню Импорт               #
    ###########################################

    def _create_quiz_from_selected_file(self, path: str, filename: str) -> None:
        self.quiz = create_quiz_from_file(os.path.join(path, filename))
        self.current_question = 0
        self._update_quiz_info_ui()
        self._open_quiz_editor()

    def _open_import_explorer(self) -> None:
        self.ui_select_import_type.enabled = False
        self.explorer.open(0)
        self.explorer.cancel_callback.set(self._open_import_select_menu)
        self.explorer.confirm_callback.set(self._create_quiz_from_selected_file)

    ###########################################

    def _open_answer_edit_menu(self, answer_index: int) -> None:
        self.ui_quiz_editor.enabled = False
        self.ui_answer_edit_menu.enabled = True

        question = self.quiz.questions[self.current_question]
        
        if question.type in (0, 1, 2, 3):
            self.ui_answer_edit_menu.change_state(0)
            self.ui_answer_edit_menu.text_1.focus_lost_callback.set((self._update_question_option, (answer_index,)))
            self.ui_answer_edit_menu.text_1.text = question.options[answer_index]
        elif question.type == 4:
            self.ui_answer_edit_menu.change_state(1)
            self.ui_answer_edit_menu.text_1.focus_lost_callback.set((self._update_question_option, (answer_index,)))
            self.ui_answer_edit_menu.text_2.focus_lost_callback.set((self._update_question_option, (answer_index,)))
            self.ui_answer_edit_menu.text_1.text = question.options[answer_index]
            self.ui_answer_edit_menu.text_2.text = question.answers[answer_index]

    def _open_quiz_rules_editor(self) -> None:
        self.ui_quiz_info_editor.enabled = False
        self.ui_quiz_rules_editor.enabled = True

    def _open_question_settings(self) -> None:
        self.ui_quiz_editor.enabled = False
        self.ui_question_settings.enabled = True
        self.ui_question_settings.tip_textbox.text = self.quiz.questions[self.current_question].tip

    ###########################################
    #              Меню экспорта              #
    ###########################################

    def _open_select_export_type_menu(self) -> None:
        self.ui_menu.enabled = False
        self.ui_select_export_type.enabled = True
        self.warning.enabled = False

    def _open_export_explorer(self) -> None:
        self.ui_select_export_type.enabled = False
        self.explorer.open(1)
        self.explorer.cancel_callback.set(self._open_select_export_type_menu)
        self.explorer.confirm_callback.set(self._try_export_quiz_file)

    def _try_export_quiz_file(self, destination_path: str) -> None:
        filename = self.explorer.file_textbox.text + ".json"
        if os.path.exists(os.path.join(destination_path, filename)):
            self.warning.enabled = True
            self.warning.warn1 = f"«{filename}» уже существует."
            self.warning.warn2 = "Вы хотите заменить его?"
            self.warning.deny_callback.set(self._open_select_export_type_menu)
            self.warning.confirm_callback.set((self._export_quiz_file, (filename, destination_path)))
        else:
            self._export_quiz_file(filename, destination_path)

    def _export_quiz_file(self, filename: str, destination_path: str) -> None:
        save_quiz_to_file(self.quiz, os.path.join(destination_path, filename))
        self._open_menu()

    ###########################################

    def _update_question_tip(self, text: str) -> None:
        question = self.quiz.questions[self.current_question]
        if len(text) > 0:
            question.tip = text

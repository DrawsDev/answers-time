import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.utility import *
from src.framework.application import Application
from src.framework.scene import Scene
from src.framework.scene.ui import DebugFrame
from src.answerstime.ui.menu.layouts import *

class Menu(Scene):
    def __init__(self, app: Application):
        self.app = app
        self.debug_frame = DebugFrame(app)
        self.ui_menu = UIMenu(app)
        self.ui_start_menu = UIStartMenu(app)
        self.ui_quiz_select_menu = UIQuizSelectMenu(app)
        self.ui_editor_menu = UIEditorMenu(app)
        self.ui_new_quiz_menu = UINewQuizMenu(app)
        self.ui_settings_menu = UISettingsMenu(app)
        self.ui_about_menu = UIAboutMenu(app)
        self.ui_editor_quiz_info_menu = UIEditorQuizInfoMenu(app)
 
    def on_enter(self, **kwargs):
        def go_to_editor_with_new_quiz() -> None:
            title = self.ui_new_quiz_menu.name_input.text
            if len(title) > 0:
                self.app.change_scene("Editor", title=title)
        def go_to_editor_with_exists_quiz(filename: str) -> None:
            self.app.change_scene("Editor", filename=filename)
        def go_to_tutorial() -> None:
            self.app.change_scene("Tutorial")
        def go_to_quiz(filename: str) -> None:
            self.app.change_scene("Quiz", filename=filename)
        def quit() -> None:
            self.app.quit()
        def open_menu() -> None:
            self.ui_menu.layout.enabled = True
            self.ui_start_menu.layout.enabled = False
            self.ui_quiz_select_menu.enabled = False
            self.ui_editor_menu.enabled = False
            self.ui_new_quiz_menu.layout.enabled = False
            self.ui_settings_menu.layout.enabled = False
            self.ui_about_menu.layout.enabled = False
            self.ui_about_menu.scroll_frame.enabled = False
        def open_start_menu() -> None:
            self.ui_menu.layout.enabled = True
            self.ui_start_menu.layout.enabled = not self.ui_start_menu.layout.enabled
            self.ui_quiz_select_menu.enabled = False
            self.ui_editor_menu.enabled = False
            self.ui_new_quiz_menu.layout.enabled = False
            self.ui_settings_menu.layout.enabled = False
            self.ui_about_menu.layout.enabled = False
        def open_quiz_select_menu() -> None:
            self.ui_menu.layout.enabled = False
            self.ui_start_menu.layout.enabled = False
            self.ui_quiz_select_menu.enabled = True
            self.ui_editor_menu.enabled = False
            self.ui_new_quiz_menu.layout.enabled = False
            self.ui_settings_menu.layout.enabled = False
            self.ui_about_menu.layout.enabled = False
            self.ui_quiz_select_menu.create_buttons(go_to_quiz)
        def open_editor_menu() -> None:
            self.ui_menu.layout.enabled = False
            self.ui_start_menu.layout.enabled = False
            self.ui_quiz_select_menu.enabled = False
            self.ui_editor_menu.enabled = True
            self.ui_new_quiz_menu.layout.enabled = False
            self.ui_settings_menu.layout.enabled = False
            self.ui_about_menu.layout.enabled = False
            self.ui_editor_menu.create_buttons(go_to_editor_with_exists_quiz)
        def open_settings_menu() -> None:
            self.ui_menu.layout.enabled = False
            self.ui_start_menu.layout.enabled = False
            self.ui_quiz_select_menu.enabled = False
            self.ui_editor_menu.enabled = False
            self.ui_new_quiz_menu.layout.enabled = False
            self.ui_settings_menu.layout.enabled = True
            self.ui_about_menu.layout.enabled = False
        def open_about_menu() -> None:
            self.ui_menu.layout.enabled = False
            self.ui_start_menu.layout.enabled = False
            self.ui_quiz_select_menu.enabled = False
            self.ui_editor_menu.enabled = False
            self.ui_new_quiz_menu.layout.enabled = False
            self.ui_settings_menu.layout.enabled = False
            self.ui_about_menu.layout.enabled = True
            self.ui_about_menu.scroll_frame.reset_scrolling()
            self.ui_about_menu.scroll_frame.enabled = True
        def open_new_quiz_menu() -> None:
            self.ui_menu.layout.enabled = False
            self.ui_start_menu.layout.enabled = False
            self.ui_quiz_select_menu.enabled = False
            self.ui_editor_menu.enabled = False
            self.ui_new_quiz_menu.layout.enabled = True
            self.ui_settings_menu.layout.enabled = False
            self.ui_about_menu.layout.enabled = False
        def open_import() -> None:
            self.ui_editor_menu.explorer.enabled = True
        # Меню
        self.ui_menu.start.pressed_callback = open_start_menu
        self.ui_menu.editor.pressed_callback = open_editor_menu
        self.ui_menu.settings.pressed_callback = open_settings_menu
        self.ui_menu.about.pressed_callback = open_about_menu
        self.ui_menu.exit.pressed_callback = quit
        # Меню запуска тестов
        self.ui_start_menu.tutorial.pressed_callback = go_to_tutorial
        self.ui_start_menu.select.pressed_callback = open_quiz_select_menu
        # Меню выбора теста
        self.ui_quiz_select_menu.back.pressed_callback.set(open_start_menu)
        # Меню редактора
        self.ui_editor_menu.back.pressed_callback = open_menu
        self.ui_editor_menu.new.pressed_callback = open_new_quiz_menu
        self.ui_editor_menu.imp.pressed_callback = open_import
        self.ui_editor_menu.explorer.close_callback.set((self.ui_editor_menu.create_buttons, (go_to_editor_with_exists_quiz,)))
        # Меню создания нового теста
        self.ui_new_quiz_menu.create.pressed_callback = go_to_editor_with_new_quiz
        self.ui_new_quiz_menu.back.pressed_callback = open_editor_menu
        # Меню настроек
        self.ui_settings_menu.back.pressed_callback = open_menu
        # Меню о программе
        self.ui_about_menu.back.pressed_callback = open_menu
        self.ui_about_menu.github.pressed_callback = (open_url, ("https://github.com/DrawsDev/answers-time",))
        self.ui_about_menu.itch.pressed_callback = (open_url, ("https://drawsdev.itch.io/answers-time",))
        # Меню о тесте
        self.ui_editor_quiz_info_menu.back.pressed_callback = open_editor_menu

    def update(self, delta: float) -> None:
        self.debug_frame.update()
        self.ui_menu.layout.update(delta)
        self.ui_start_menu.layout.update(delta)
        self.ui_quiz_select_menu.update(delta)
        self.ui_editor_menu.update(delta)
        self.ui_new_quiz_menu.layout.update(delta)
        self.ui_settings_menu.layout.update(delta)
        self.ui_about_menu.layout.update(delta)
        self.ui_editor_quiz_info_menu.layout.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill("gray")
        self.ui_menu.layout.draw(surface)
        self.ui_start_menu.layout.draw(surface)
        self.ui_quiz_select_menu.draw(surface)
        self.ui_editor_menu.draw(surface)
        self.ui_new_quiz_menu.layout.draw(surface)
        self.ui_settings_menu.layout.draw(surface)
        self.ui_about_menu.layout.draw(surface)
        self.ui_editor_quiz_info_menu.layout.draw(surface)
        self.debug_frame.draw(surface)

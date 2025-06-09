import pygame
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import open_url
from src.components.scene import Scene
from src.ui.debug_frame import DebugFrame
from src.ui.navigation import UINavigation
from src.menu.ui.layouts.ui_menu import UIMenu
from src.menu.ui.layouts.ui_start_menu import UIStartMenu
from src.menu.ui.layouts.ui_quiz_select_menu import UIQuizSelectMenu
from src.menu.ui.layouts.ui_editor_menu import UIEditorMenu
from src.menu.ui.layouts.ui_new_quiz_menu import UINewQuizMenu
from src.menu.ui.layouts.ui_settings_menu import UISettingsMenu
from src.menu.ui.layouts.ui_about_menu import UIAboutMenu
from src.menu.ui.layouts.ui_editor_quiz_info_menu import UIEditorQuizInfoMenu

class Menu(Scene):
    def __init__(self, game: Game):
        self.game = game
        self.debug_frame = DebugFrame(game)
        self.navigation = UINavigation(game)
        self.ui_menu = UIMenu(game)
        self.ui_start_menu = UIStartMenu(game)
        self.ui_quiz_select_menu = UIQuizSelectMenu(game)
        self.ui_editor_menu = UIEditorMenu(game)
        self.ui_new_quiz_menu = UINewQuizMenu(game)
        self.ui_settings_menu = UISettingsMenu(game)
        self.ui_about_menu = UIAboutMenu(game)
        self.ui_editor_quiz_info_menu = UIEditorQuizInfoMenu(game)
 
    def on_enter(self, **kwargs):
        def go_to_editor_with_new_quiz() -> None:
            title = self.ui_new_quiz_menu.name_input.text
            if len(title) > 0:
                self.game.change_scene("Editor", title=title)
        def go_to_editor_with_exists_quiz(filename: str) -> None:
            self.game.change_scene("Editor", filename=filename)
        def go_to_tutorial() -> None:
            self.game.change_scene("Tutorial")
        def go_to_quiz(filename: str) -> None:
            self.game.change_scene("Quiz", filename=filename)
        def quit() -> None:
            self.game.quit()
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

    def on_exit(self, **kwargs) -> None:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def update(self, delta: float) -> None:
        self.debug_frame.update(delta)
        # self.navigation.update(delta)
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
        # self.navigation.draw(surface)
        self.debug_frame.draw(surface)

__all__ = ["Menu"]

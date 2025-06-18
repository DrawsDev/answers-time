import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.utility import *
from src.framework.application import Application
from src.framework.scene import Scene
from src.framework.scene.ui import DebugFrame
from src.framework.scene.ui import ExplorerFrame
from src.framework.scene.ui import *
from src.answerstime.ui.menu.layouts import *
from src.answerstime.ui import Background

class Menu(Scene):
    def __init__(self, app: Application):
        self.app = app
        self.debug_frame = DebugFrame(app)
        self.warning = Warning(app)
        self.explorer = ExplorerFrame(app)
        self.background = Background(load_asset(SPRITES, "quiz_background.png"), 0, 10)
        self.ui_menu = UIMenu(app)
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
        def quit() -> None:
            self.app.quit()
        def open_menu() -> None:
            self.ui_menu.layout.enabled = True
            self.ui_quiz_select_menu.enabled = False
            self.ui_editor_menu.enabled = False
            self.ui_new_quiz_menu.layout.enabled = False
            self.ui_settings_menu.enabled = False
            self.ui_about_menu.layout.enabled = False
            self.ui_about_menu.scroll_frame.enabled = False
        def open_editor_menu() -> None:
            self.ui_menu.layout.enabled = False
            self.ui_quiz_select_menu.enabled = False
            self.ui_editor_menu.enabled = True
            self.ui_new_quiz_menu.layout.enabled = False
            self.ui_settings_menu.enabled = False
            self.ui_about_menu.layout.enabled = False
            self.ui_editor_menu.create_buttons(go_to_editor_with_exists_quiz)
            self.explorer.enabled = False
        def open_settings_menu() -> None:
            self.ui_menu.layout.enabled = False
            self.ui_quiz_select_menu.enabled = False
            self.ui_editor_menu.enabled = False
            self.ui_new_quiz_menu.layout.enabled = False
            self.ui_settings_menu.enabled = True
            self.ui_about_menu.layout.enabled = False
        def open_about_menu() -> None:
            self.ui_menu.layout.enabled = False
            self.ui_quiz_select_menu.enabled = False
            self.ui_editor_menu.enabled = False
            self.ui_new_quiz_menu.layout.enabled = False
            self.ui_settings_menu.enabled = False
            self.ui_about_menu.layout.enabled = True
            self.ui_about_menu.scroll_frame.reset_scrolling()
            self.ui_about_menu.scroll_frame.enabled = True
        def open_new_quiz_menu() -> None:
            self.ui_menu.layout.enabled = False
            self.ui_quiz_select_menu.enabled = False
            self.ui_editor_menu.enabled = False
            self.ui_new_quiz_menu.layout.enabled = True
            self.ui_settings_menu.enabled = False
            self.ui_about_menu.layout.enabled = False
        def open_editor_menu_import() -> None:
            self.explorer.open(0)
            self.explorer.cancel_callback.set(close_editor_menu_import)
            self.explorer.confirm_callback.set(self._try_import_quiz_file)
            self.ui_editor_menu.enabled = False
        def close_editor_menu_import() -> None:
            self.ui_editor_menu.enabled = True
            self.ui_editor_menu.create_buttons(go_to_editor_with_exists_quiz)
        
        # Главное меню
        self.ui_menu.start.pressed_callback.set(self._open_quiz_select_menu)
        self.ui_menu.tutorial.pressed_callback.set(self._go_to_tutorial)
        self.ui_menu.editor.pressed_callback.set(open_editor_menu)
        self.ui_menu.settings.pressed_callback.set(open_settings_menu)
        self.ui_menu.about.pressed_callback.set(open_about_menu)
        self.ui_menu.exit.pressed_callback.set(quit)

        # Меню Выбор теста
        self.ui_quiz_select_menu.back.pressed_callback.set(open_menu)
        
        # Меню редактора
        self.ui_editor_menu.back.pressed_callback = open_menu
        self.ui_editor_menu.new.pressed_callback = open_new_quiz_menu
        self.ui_editor_menu.imp.pressed_callback = open_editor_menu_import
        # Меню создания нового теста
        self.ui_new_quiz_menu.create.pressed_callback = go_to_editor_with_new_quiz
        self.ui_new_quiz_menu.back.pressed_callback = open_editor_menu
       
        # Меню настроек
        self.ui_settings_menu.back.pressed_callback.set(open_menu)
        
        # Меню о программе
        self.ui_about_menu.back.pressed_callback = open_menu
        self.ui_about_menu.github.pressed_callback = (open_url, ("https://github.com/DrawsDev/answers-time",))
        self.ui_about_menu.itch.pressed_callback = (open_url, ("https://drawsdev.itch.io/answers-time",))
        # Меню о тесте
        self.ui_editor_quiz_info_menu.back.pressed_callback = open_editor_menu

    def update(self, delta: float) -> None:
        self.debug_frame.update()
        self.background.update(delta)
        self.ui_menu.layout.update(delta)
        self.ui_quiz_select_menu.update(delta)
        self.ui_editor_menu.update(delta)
        self.ui_new_quiz_menu.layout.update(delta)
        self.ui_settings_menu.update(delta)
        self.ui_about_menu.layout.update(delta)
        self.ui_editor_quiz_info_menu.layout.update(delta)
        self.explorer.update(delta)
        self.warning.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill(Pallete.ATBlue5)
        self.background.draw(surface)
        self.ui_menu.layout.draw(surface)
        self.ui_quiz_select_menu.draw(surface)
        self.ui_editor_menu.draw(surface)
        self.ui_new_quiz_menu.layout.draw(surface)
        self.ui_settings_menu.draw(surface)
        self.ui_about_menu.layout.draw(surface)
        self.ui_editor_quiz_info_menu.layout.draw(surface)
        self.debug_frame.draw(surface)
        self.explorer.draw(surface)
        self.warning.draw(surface)

    def _try_import_quiz_file(self, path: str, filename: str) -> None:
        self.ui_editor_menu.enabled = True
        
        if os.path.exists(asset_path(QUIZZES, filename)):
            self.ui_editor_menu.enabled = False
            self.warning.enabled = True
            self.warning.warn1 = f"«{filename}» уже существует."
            self.warning.warn2 = "Вы хотите заменить его?"
            self.warning.confirm_callback.set((self._import_quiz_file_and_open_editor_menu, (os.path.join(path, filename), asset_path(QUIZZES))))
            self.warning.deny_callback.set(self._open_editor_menu)
        else:
            self._import_quiz_file_and_open_editor_menu(os.path.join(path, filename), asset_path(QUIZZES))

    def _import_quiz_file_and_open_editor_menu(self, source_path: str, destination_path: str) -> None:
        self.explorer.copy(source_path, destination_path)
        self._open_editor_menu()

    def _open_editor_menu(self) -> None:
            self.ui_editor_menu.enabled = True
            self.ui_editor_menu.create_buttons(self._go_to_editor_with_exists_quiz)
            self.ui_menu.layout.enabled = False
            self.warning.enabled = False

    def _go_to_editor_with_exists_quiz(self, filename: str) -> None:
        self.app.change_scene("Editor", filename=filename)

    ########################################
    #             Главное меню             #
    ########################################

    def _go_to_tutorial(self) -> None:
        self.app.change_scene("Tutorial")

    def _open_quiz_select_menu(self) -> None:
        self.ui_menu.layout.enabled = False
        self.ui_quiz_select_menu.enabled = True
        self.ui_quiz_select_menu.create_buttons(self._go_to_quiz)

    ########################################
    #             Выбор теста              #
    ########################################

    def _go_to_quiz(self, filename: str) -> None:
        self.app.change_scene("Quiz", filename=filename)

    ########################################

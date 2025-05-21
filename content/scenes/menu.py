import os
import random
import pygame
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.components.scene import Scene
from src.ui.debug_frame import DebugFrame
from src.ui.label import Label
from src.ui.frame import Frame
from src.ui.image import Image
from src.ui.text_button import TextButton
from src.ui.layout import Layout

class Menu(Scene):
    def __init__(self, game: Game):
        self.game = game
        self.debug_frame = DebugFrame(game)

        self._create_main_menu()
        self._create_start_menu()
        self._create_editor_menu()
        self._create_settings_menu()
        self._create_about_menu()

    def _create_main_menu(self) -> None:
        # Основное
        self.main_menu = Layout()
        # Логотип
        self.logo = Image(self.game, os.path.join(SPRITES, "new_logo.png"))
        self.logo.anchor = Anchor.MidRight
        self.logo.position = [self.game.surface.get_width() - 32, self.game.surface.get_height() / 2]
        # Фрейм
        self.frame = Frame(self.game, [144, self.game.surface.get_height()], [32, 0])
        self.frame.transparency = 175
        # Кнопки
        self.texts = ["Начать тест", "Редактор", "Настройки", "Об программе", "Выход"]
        self.buttons = []
        for i in range(0, 5):
            button = TextButton(self.game, self.texts[i], [self.frame.image.get_width(), 40], [32, 50 + 40 * i])
            button.button_color = [0, 0, 0, 0]
            button.button_hover_color = "#64646E"
            button.button_press_color = "#000000"
            self.buttons.append(button)
        #
        self.main_menu.add(self.logo, self.frame, self.buttons)

    def _create_start_menu(self) -> None:
        # Основное
        self.start_menu = Layout()
        self.start_menu.enabled = False
        # Фрейм
        self.start_menu_frame = Frame(self.game, [144, self.game.surface.get_height()], [144 + 32, 0])
        self.start_menu_frame.transparency = 175
        # Кнопки
        # 1
        self.start_menu_button_1 = TextButton(self.game, "Обучение", [self.start_menu_frame.image.get_width(), 40], [144 + 32, 50])
        self.start_menu_button_1.text_align = pygame.FONT_CENTER
        self.start_menu_button_1.text_wraplength = self.start_menu_frame.image.get_width() - 10
        self.start_menu_button_1.button_color = [0, 0, 0, 0]
        self.start_menu_button_1.button_hover_color = "#64646E"
        self.start_menu_button_1.button_press_color = "#000000"
        # 2
        self.start_menu_button_2 = TextButton(self.game, "Выбрать тест", [self.start_menu_frame.image.get_width(), 40], [144 + 32, 90])
        self.start_menu_button_2.text_align = pygame.FONT_CENTER
        self.start_menu_button_2.text_wraplength = self.start_menu_frame.image.get_width() - 10
        self.start_menu_button_2.button_color = [0, 0, 0, 0]
        self.start_menu_button_2.button_hover_color = "#64646E"
        self.start_menu_button_2.button_press_color = "#000000"
        #
        self.start_menu.add(self.start_menu_frame, self.start_menu_button_1, self.start_menu_button_2)

    def _create_editor_menu(self) -> None:
        # Основное
        self.editor_menu = Layout()
        self.editor_menu.enabled = False
        # Фрейм
        self.editor_menu_frame = Frame(self.game, self.game.surface.get_size())
        self.editor_menu_frame.transparency = 225
        # Заголовок
        self.editor_menu_title = Label(self.game, "Редактор", [self.game.surface.get_width() / 2, 0])
        self.editor_menu_title.align = pygame.FONT_CENTER
        self.editor_menu_title.anchor = Anchor.MidTop
        self.editor_menu_title.color = "#3CA4FF"
        # Линия под заголовком
        self.editor_menu_title_line = Frame(self.game, [self.game.surface.get_width() - 10, 2])
        self.editor_menu_title_line.color = "#3CA4FF"
        self.editor_menu_title_line.anchor = Anchor.Center
        self.editor_menu_title_line.position = [self.game.surface.get_width() / 2, self.editor_menu_title.image.get_height()]
        # Кнопки
        # 1
        self.editor_menu_button_1 = TextButton(self.game, "Назад", [130, 40])
        self.editor_menu_button_1.position = [self.game.surface.get_width() / 2 - 65, self.game.surface.get_height() - 5]
        self.editor_menu_button_1.anchor = Anchor.BottomRight
        self.editor_menu_button_1.text_align = pygame.FONT_CENTER
        self.editor_menu_button_1.text_wraplength = self.editor_menu_button_1.image.get_width() - 10
        self.editor_menu_button_1.button_color = [0, 0, 0, 0]
        self.editor_menu_button_1.button_hover_color = "#64646E"
        self.editor_menu_button_1.button_press_color = "#000000"
        # 2
        self.editor_menu_button_2 = TextButton(self.game, "Новый тест", [130, 40])
        self.editor_menu_button_2.position = [self.game.surface.get_width() / 2, self.game.surface.get_height() - 5]
        self.editor_menu_button_2.anchor = Anchor.MidBottom
        self.editor_menu_button_2.text_align = pygame.FONT_CENTER
        self.editor_menu_button_2.text_wraplength = self.editor_menu_button_2.image.get_width() - 10
        self.editor_menu_button_2.button_color = [0, 0, 0, 0]
        self.editor_menu_button_2.button_hover_color = "#64646E"
        self.editor_menu_button_2.button_press_color = "#000000"
        # 3
        self.editor_menu_button_3 = TextButton(self.game, "Импортировать тест", [130, 40])
        self.editor_menu_button_3.position = [self.game.surface.get_width() / 2 + 65, self.game.surface.get_height() - 5]
        self.editor_menu_button_3.anchor = Anchor.BottomLeft
        self.editor_menu_button_3.text_align = pygame.FONT_CENTER
        self.editor_menu_button_3.text_wraplength = self.editor_menu_button_3.image.get_width() - 20
        self.editor_menu_button_3.button_color = [0, 0, 0, 0]
        self.editor_menu_button_3.button_hover_color = "#64646E"
        self.editor_menu_button_3.button_press_color = "#000000"
        #
        self.editor_menu.add(self.editor_menu_frame, self.editor_menu_title, self.editor_menu_title_line)
        self.editor_menu.add(self.editor_menu_button_1, self.editor_menu_button_2, self.editor_menu_button_3)

    def _create_settings_menu(self) -> None:
        # Основное
        self.settings_menu = Layout()
        self.settings_menu.enabled = False
        # Фрейм
        self.settings_menu_frame = Frame(self.game, self.game.surface.get_size())
        self.settings_menu_frame.transparency = 225
        # Заголовок
        self.settings_menu_title = Label(self.game, "Настройки", [self.game.surface.get_width() / 2, 0])
        self.settings_menu_title.align = pygame.FONT_CENTER
        self.settings_menu_title.anchor = Anchor.MidTop
        self.settings_menu_title.color = "#3CA4FF"
        # Линия под заголовком
        self.settings_menu_title_line = Frame(self.game, [self.game.surface.get_width() - 10, 2])
        self.settings_menu_title_line.color = "#3CA4FF"
        self.settings_menu_title_line.anchor = Anchor.Center
        self.settings_menu_title_line.position = [self.game.surface.get_width() / 2, self.settings_menu_title.image.get_height()]
        # Кнопки
        # 1
        self.settings_menu_button_1 = TextButton(self.game, "Назад", [130, 40])
        self.settings_menu_button_1.position = [self.game.surface.get_width() / 2, self.game.surface.get_height() - 5]
        self.settings_menu_button_1.anchor = Anchor.MidBottom
        self.settings_menu_button_1.text_align = pygame.FONT_CENTER
        self.settings_menu_button_1.text_wraplength = self.settings_menu_button_1.image.get_width() - 10
        self.settings_menu_button_1.button_color = [0, 0, 0, 0]
        self.settings_menu_button_1.button_hover_color = "#64646E"
        self.settings_menu_button_1.button_press_color = "#000000"
        #
        self.settings_menu.add(self.settings_menu_frame, self.settings_menu_title, self.settings_menu_title_line, self.settings_menu_button_1)

    def _create_about_menu(self) -> None:
        # Основное
        self.about_menu = Layout()
        self.about_menu.enabled = False
        # Фрейм
        self.about_menu_frame = Frame(self.game, self.game.surface.get_size())
        self.about_menu_frame.transparency = 225
        # Заголовок
        self.about_menu_title = Label(self.game, "Об программе", [self.game.surface.get_width() / 2, 0])
        self.about_menu_title.align = pygame.FONT_CENTER
        self.about_menu_title.anchor = Anchor.MidTop
        self.about_menu_title.color = "#3CA4FF"
        # Линия под заголовком
        self.about_menu_title_line = Frame(self.game, [self.game.surface.get_width() - 10, 2])
        self.about_menu_title_line.color = "#3CA4FF"
        self.about_menu_title_line.anchor = Anchor.Center
        self.about_menu_title_line.position = [self.game.surface.get_width() / 2, self.about_menu_title.image.get_height()]
        # Кнопки
        # 1
        self.about_menu_button_1 = TextButton(self.game, "Назад", [130, 40])
        self.about_menu_button_1.position = [self.game.surface.get_width() / 2, self.game.surface.get_height() - 5]
        self.about_menu_button_1.anchor = Anchor.MidBottom
        self.about_menu_button_1.text_align = pygame.FONT_CENTER
        self.about_menu_button_1.text_wraplength = self.about_menu_button_1.image.get_width() - 10
        self.about_menu_button_1.button_color = [0, 0, 0, 0]
        self.about_menu_button_1.button_hover_color = "#64646E"
        self.about_menu_button_1.button_press_color = "#000000"
        #
        self.about_menu.add(self.about_menu_frame, self.about_menu_title, self.about_menu_title_line, self.about_menu_button_1)

    def _update_main_menu(self, delta: float) -> None:
        self.main_menu.update(delta)
        
        if self.buttons[0].pressed:
            self.start_menu.enabled = not self.start_menu.enabled
        elif self.buttons[1].pressed:
            self.main_menu.enabled = False
            self.start_menu.enabled = False
            self.editor_menu.enabled = True
        elif self.buttons[2].pressed:
            self.main_menu.enabled = False
            self.start_menu.enabled = False
            self.settings_menu.enabled = True
        elif self.buttons[3].pressed:
            self.main_menu.enabled = False
            self.start_menu.enabled = False
            self.about_menu.enabled = True
        elif self.buttons[4].pressed:
            self.game.quit()

    def _update_start_menu(self, delta: float) -> None:
        self.start_menu.update(delta)

        if self.start_menu_button_1.pressed:
            self.game.change_scene("Tutorial")

    def _update_editor_menu(self, delta: float) -> None:
        self.editor_menu.update(delta)

        if self.editor_menu_button_1.pressed:
            self.main_menu.enabled = True
            self.editor_menu.enabled = False

    def _update_settings_menu(self, delta: float) -> None:
        self.settings_menu.update(delta)

        if self.settings_menu_button_1.pressed:
            self.main_menu.enabled = True
            self.settings_menu.enabled = False

    def _update_about_menu(self, delta: float) -> None:
        self.about_menu.update(delta)

        if self.about_menu_button_1.pressed:
            self.main_menu.enabled = True
            self.about_menu.enabled = False
            print("cla")
            
    def on_exit(self, **kwargs):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def update(self, delta: float):
        self.debug_frame.update(delta)
        self._update_main_menu(delta)
        self._update_start_menu(delta)
        self._update_editor_menu(delta)
        self._update_settings_menu(delta)
        self._update_about_menu(delta)

    def draw(self, surface: pygame.Surface):
        surface.fill("Gray")
        self.main_menu.draw(surface)
        self.start_menu.draw(surface)
        self.editor_menu.draw(surface)
        self.settings_menu.draw(surface)
        self.about_menu.draw(surface)
        self.debug_frame.draw(surface)

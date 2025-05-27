import os
import random
import pygame
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import asset_path, load_asset
from src.components.scene import Scene
from src.ui.debug_frame import DebugFrame
from src.ui.navigation import UINavigation
from src.ui.layout import Layout
from src.ui.frame import Frame
from src.ui.image_label import ImageLabel
from src.ui.text_button import TextButton
from src.ui.menu.menu_page import MenuPage

class Menu(Scene):
    def __init__(self, game: Game):
        self.game = game
        self.debug_frame = DebugFrame(game)
        self.navigation = UINavigation(game)

        self._create_main_menu()
        self._create_start_menu()
        self._create_editor_menu()
        self._create_settings_menu()
        self._create_about_menu()
        self._create_select_test_menu()

        self.navigation.set_layout(self.main_menu)

    def _create_main_menu(self) -> None:
        # Основное
        self.main_menu = Layout()
        # Логотип
        self.logo = ImageLabel(self.game, asset_path(SPRITES, "new_logo.png"))
        self.logo.anchor = Anchor.MidRight
        self.logo.position = [self.game.surface.get_width() - 32, self.game.surface.get_height() / 2]
        # Фрейм
        self.frame = Frame(self.game, [144, self.game.surface.get_height()], [32, 0])
        self.frame.transparency = 175
        # Кнопки
        texts = ("Начать тест", "Редактор", "Настройки", "О программе", "Выход")
        icons = ("start.png", "edit.png", "settings.png", "about.png", "exit.png")
        self.buttons = []
        
        for i in range(0, 5):
            button = TextButton(self.game, texts[i], [self.frame.image.get_width(), 40], [32, 50 + 40 * i])
            button.button_color = [0, 0, 0, 0]
            button.button_hover_color = "#64646E"
            button.button_press_color = "#000000"
            button.font_path = asset_path(FONTS, "Ramona-Bold.ttf")
            button.font_size = 16
            button.button_icon = load_asset(SPRITES, icons[i])
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
        self.start_menu_button_1.button_color = [0, 0, 0, 0]
        self.start_menu_button_1.button_hover_color = "#64646E"
        self.start_menu_button_1.button_press_color = "#000000"
        self.start_menu_button_1.button_icon = load_asset(SPRITES, "tutorial.png")
        self.start_menu_button_1.font_path = asset_path(FONTS, "Ramona-Bold.ttf")
        self.start_menu_button_1.font_size = 16
        # 2
        self.start_menu_button_2 = TextButton(self.game, "Выбрать тест", [self.start_menu_frame.image.get_width(), 40], [144 + 32, 90])
        self.start_menu_button_2.button_color = [0, 0, 0, 0]
        self.start_menu_button_2.button_hover_color = "#64646E"
        self.start_menu_button_2.button_press_color = "#000000"
        self.start_menu_button_2.button_icon = load_asset(SPRITES, "select.png")
        self.start_menu_button_2.font_path = asset_path(FONTS, "Ramona-Bold.ttf")
        self.start_menu_button_2.font_size = 16
        #
        self.start_menu.add(self.start_menu_frame, self.start_menu_button_1, self.start_menu_button_2)

    def _create_editor_menu(self) -> None:
        # Основное
        self.editor_menu = Layout()
        self.editor_menu.enabled = False
        # Кнопки
        # 1
        self.editor_menu_button_1 = TextButton(self.game, "Назад", [130, 40])
        self.editor_menu_button_1.position = [self.game.surface.get_width() / 2 - 65, self.game.surface.get_height() - 5]
        self.editor_menu_button_1.anchor = Anchor.BottomRight
        self.editor_menu_button_1.button_color = [0, 0, 0, 0]
        self.editor_menu_button_1.button_hover_color = "#64646E"
        self.editor_menu_button_1.button_press_color = "#000000"
        self.editor_menu_button_1.button_icon = load_asset(SPRITES, "back.png")
        self.editor_menu_button_1.font_path = asset_path(FONTS, "Ramona-Bold.ttf")
        self.editor_menu_button_1.font_size = 16
        # 2
        self.editor_menu_button_2 = TextButton(self.game, "Новый тест", [130, 40])
        self.editor_menu_button_2.position = [self.game.surface.get_width() / 2, self.game.surface.get_height() - 5]
        self.editor_menu_button_2.anchor = Anchor.MidBottom
        self.editor_menu_button_2.button_color = [0, 0, 0, 0]
        self.editor_menu_button_2.button_hover_color = "#64646E"
        self.editor_menu_button_2.button_press_color = "#000000"
        self.editor_menu_button_2.button_icon = load_asset(SPRITES, "add.png")
        self.editor_menu_button_2.font_path = asset_path(FONTS, "Ramona-Bold.ttf")
        self.editor_menu_button_2.font_size = 16
        # 3
        self.editor_menu_button_3 = TextButton(self.game, "Импортировать тест", [130, 40])
        self.editor_menu_button_3.position = [self.game.surface.get_width() / 2 + 65, self.game.surface.get_height() - 5]
        self.editor_menu_button_3.anchor = Anchor.BottomLeft
        self.editor_menu_button_3.button_color = [0, 0, 0, 0]
        self.editor_menu_button_3.button_hover_color = "#64646E"
        self.editor_menu_button_3.button_press_color = "#000000"
        self.editor_menu_button_3.button_icon = load_asset(SPRITES, "import.png")
        self.editor_menu_button_3.font_path = asset_path(FONTS, "Ramona-Bold.ttf")
        self.editor_menu_button_3.font_size = 16
        #
        self.editor_menu.add(MenuPage(self.game, "Редактор").children)
        self.editor_menu.add(self.editor_menu_button_1, self.editor_menu_button_2, self.editor_menu_button_3)

    def _create_settings_menu(self) -> None:
        # Основное
        self.settings_menu = Layout()
        self.settings_menu.enabled = False
        # Кнопки
        # 1
        self.settings_menu_button_1 = TextButton(self.game, "Назад", [130, 40])
        self.settings_menu_button_1.position = [self.game.surface.get_width() / 2, self.game.surface.get_height() - 5]
        self.settings_menu_button_1.anchor = Anchor.MidBottom
        self.settings_menu_button_1.button_color = [0, 0, 0, 0]
        self.settings_menu_button_1.button_hover_color = "#64646E"
        self.settings_menu_button_1.button_press_color = "#000000"
        self.settings_menu_button_1.button_icon = load_asset(SPRITES, "back.png")
        self.settings_menu_button_1.font_path = asset_path(FONTS, "Ramona-Bold.ttf")
        self.settings_menu_button_1.font_size = 16
        #
        self.settings_menu.add(MenuPage(self.game, "Настройки").children, self.settings_menu_button_1)

    def _create_about_menu(self) -> None:
        # Основное
        self.about_menu = Layout()
        self.about_menu.enabled = False
        # Кнопки
        # 1
        self.about_menu_button_1 = TextButton(self.game, "Назад", [130, 40])
        self.about_menu_button_1.position = [self.game.surface.get_width() / 2, self.game.surface.get_height() - 5]
        self.about_menu_button_1.anchor = Anchor.MidBottom
        self.about_menu_button_1.button_color = [0, 0, 0, 0]
        self.about_menu_button_1.button_hover_color = "#64646E"
        self.about_menu_button_1.button_press_color = "#000000"
        self.about_menu_button_1.button_icon = load_asset(SPRITES, "back.png")
        self.about_menu_button_1.font_path = asset_path(FONTS, "Ramona-Bold.ttf")
        self.about_menu_button_1.font_size = 16
        #
        self.about_menu.add(MenuPage(self.game, "О программе").children, self.about_menu_button_1)

    def _create_select_test_menu(self) -> None:
        # Основное
        self.select_test_menu = Layout()
        self.select_test_menu.enabled = False
        # Кнопки
        # 1
        self.select_test_menu_button_1 = TextButton(self.game, "Назад", [130, 40])
        self.select_test_menu_button_1.position = [self.game.surface.get_width() / 2, self.game.surface.get_height() - 5]
        self.select_test_menu_button_1.anchor = Anchor.MidBottom
        self.select_test_menu_button_1.button_color = [0, 0, 0, 0]
        self.select_test_menu_button_1.button_hover_color = "#64646E"
        self.select_test_menu_button_1.button_press_color = "#000000"
        self.select_test_menu_button_1.button_icon = load_asset(SPRITES, "back.png")
        self.select_test_menu_button_1.font_path = asset_path(FONTS, "Ramona-Bold.ttf")
        self.select_test_menu_button_1.font_size = 16
        #
        self.select_test_menu.add(MenuPage(self.game, "Выбрать тест").children, self.select_test_menu_button_1)        

    def _update_main_menu(self, delta: float) -> None:
        self.main_menu.update(delta)

        if self.buttons[0].pressed:
            self.start_menu.enabled = not self.start_menu.enabled
            if self.start_menu.enabled:
                self.navigation.set_layout(self.main_menu, self.start_menu)
            else:
                self.navigation.set_layout(self.main_menu)
        elif self.buttons[1].pressed:
            self.main_menu.enabled = False
            self.start_menu.enabled = False
            self.editor_menu.enabled = True
            self.navigation.set_layout(self.editor_menu)
        elif self.buttons[2].pressed:
            self.main_menu.enabled = False
            self.start_menu.enabled = False
            self.settings_menu.enabled = True
            self.navigation.set_layout(self.settings_menu)
        elif self.buttons[3].pressed:
            self.main_menu.enabled = False
            self.start_menu.enabled = False
            self.about_menu.enabled = True
            self.navigation.set_layout(self.about_menu)
        elif self.buttons[4].pressed:
            self.game.quit()

    def _update_start_menu(self, delta: float) -> None:
        self.start_menu.update(delta)

        if self.start_menu_button_1.pressed:
            self.game.change_scene("Tutorial")
        
        if self.start_menu_button_2.pressed:
            self.main_menu.enabled = False
            self.start_menu.enabled = False
            self.select_test_menu.enabled = True
            self.navigation.set_layout(self.select_test_menu)

    def _update_editor_menu(self, delta: float) -> None:
        self.editor_menu.update(delta)

        if self.editor_menu_button_1.pressed:
            self.main_menu.enabled = True
            self.editor_menu.enabled = False
            self.navigation.set_layout(self.main_menu)

    def _update_settings_menu(self, delta: float) -> None:
        self.settings_menu.update(delta)

        if self.settings_menu_button_1.pressed:
            self.main_menu.enabled = True
            self.settings_menu.enabled = False
            self.navigation.set_layout(self.main_menu)

    def _update_about_menu(self, delta: float) -> None:
        self.about_menu.update(delta)

        if self.about_menu_button_1.pressed:
            self.main_menu.enabled = True
            self.about_menu.enabled = False
            self.navigation.set_layout(self.main_menu)

    def _update_select_test_menu(self, delta: float) -> None:
        self.select_test_menu.update(delta)

        if self.select_test_menu_button_1.pressed:
            self.main_menu.enabled = True
            self.start_menu.enabled = True
            self.select_test_menu.enabled = False
            self.navigation.set_layout(self.main_menu, self.start_menu)

    def on_exit(self, **kwargs) -> None:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def update(self, delta: float) -> None:
        self.debug_frame.update(delta)
        self.navigation.update(delta)
        self._update_main_menu(delta)
        self._update_start_menu(delta)
        self._update_editor_menu(delta)
        self._update_settings_menu(delta)
        self._update_about_menu(delta)
        self._update_select_test_menu(delta)

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill("Gray")
        self.main_menu.draw(surface)
        self.start_menu.draw(surface)
        self.editor_menu.draw(surface)
        self.settings_menu.draw(surface)
        self.about_menu.draw(surface)
        self.select_test_menu.draw(surface)
        self.navigation.draw(surface)
        self.debug_frame.draw(surface)

__all__ = ["Menu"]

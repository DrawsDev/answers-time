import pygame
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.layout import Layout

class UIMenu():
    def __init__(self, game: Game) -> None:
        self.game = game
        self.layout = Layout(False)
        self.pos = (game.surface.get_width() / 2, game.surface.get_height() / 2)
        self._create_back_button()
        self._create_save_button()
        self._create_info_button()
        self._create_import_button()
        self._create_export_button()
        self._create_exit_button()
        self.layout.insert_child(self.back, self.save, self.info, self.imp, self.exp, self.exit)

    def _create_back_button(self) -> None:
        self.back = TextButton(
            game=self.game,
            text="Назад",
            size=(130, 40),
            position=(self.game.surface.get_width() / 2, self.game.surface.get_height()),
            anchor=Anchor.MidBottom,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "back.png")
        )

    def _create_exit_button(self) -> None:
        self.exit = TextButton(
            game=self.game,
            text="Выйти из редактора",
            size=(260 + 5, 40),
            position=(self.pos[0], self.pos[1] + 25),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "exit.png")
        )

    def _create_save_button(self) -> None:
        self.save = TextButton(
            game=self.game,
            text="Сохранить тест",
            size=(130, 40),
            position=(self.pos[0] - 2, self.pos[1] - 45),
            anchor=Anchor.MidRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "test2.png")
        )

    def _create_info_button(self) -> None:
        self.info = TextButton(
            game=self.game,
            text="Настройки теста",
            size=(130, 40),
            position=(self.pos[0] + 3, self.pos[1] - 45),
            anchor=Anchor.MidLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "test2.png")
        )
    
    def _create_export_button(self) -> None:
        self.exp = TextButton(
            game=self.game,
            text="Экспорт",
            size=(130, 40),
            position=(self.pos[0] + 3, self.pos[1]),
            anchor=Anchor.MidLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "export.png")
        )

    def _create_import_button(self) -> None:
        self.imp = TextButton(
            game=self.game,
            text="Импорт",
            size=(130, 40),
            position=(self.pos[0] - 2, self.pos[1]),
            anchor=Anchor.MidRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "import.png")
        )

__all__ = ["UIMenu"]

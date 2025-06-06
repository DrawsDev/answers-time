import os
from typing import Callable
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.frame import Frame
from src.ui.layout import Layout
from src.ui.explorer_frame import ExplorerFrame

GAP = 4

class UIEditorMenu:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.layout = Layout(False)
        self.explorer = ExplorerFrame(game)
        self.buttons = []
        self._create_back_button()
        self._create_new_button()
        self._create_import_button()
        self._create_frame()
        self.layout.insert_child(self.back, self.new, self.imp, self.frame, self.explorer)
    
    def _create_back_button(self) -> None:
        self.back = TextButton(
            game=self.game,
            text="Назад",
            size=(130, 40),
            position=(self.game.surface.get_width() / 2 - 65 - GAP, self.game.surface.get_height() - GAP),
            anchor=Anchor.BottomRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "back.png")
        )

    def _create_new_button(self) -> None:
        self.new = TextButton(
            game=self.game,
            text="Новый тест",
            size=(130, 40),
            position=(self.game.surface.get_width() / 2, self.game.surface.get_height() - GAP),
            anchor=Anchor.MidBottom,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "add.png")
        )

    def _create_import_button(self) -> None:
        self.imp = TextButton(
            game=self.game,
            text="Импортировать тест",
            size=(130, 40),
            position=(self.game.surface.get_width() / 2 + 65 + GAP, self.game.surface.get_height() - GAP),
            anchor=Anchor.BottomLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "import.png")
        )
    
    def _create_frame(self) -> None:
        self.frame = Frame(
            game=self.game,
            color="#4E4E56",
            size=(420, 260),
            position=(self.game.surface.get_width() / 2, self.game.surface.get_height() / 2),
            anchor=Anchor.Center,
            z_index=-1
        )

    def create_buttons(self, callback: Callable) -> None:
        self.layout.remove_child(self.buttons)
        self.buttons.clear()
        files = [file for file in os.listdir(asset_path(QUIZZES)) if file.endswith(".json")]
        x = -130 - GAP
        y = 0
        for i in range(len(files)):
            x += 130 + GAP
            if x >= self.frame.rect.width:
                x = 0
                y += 40 + GAP
            button = TextButton(
                game=self.game,
                text=files[i],
                size=(130, 40),
                position=(self.frame.rect.left + x, self.frame.rect.top + y),
                anchor=Anchor.TopLeft,
                font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
                font_size=16,
                font_align=Align.Center,
                text_color="white",
                button_color="#4E4E56",
                button_hover_color="#64646E",
                button_press_color="#000000"
            )
            button.pressed_callback.set((callback, (files[i],)))
            self.buttons.append(button)
        self.layout.insert_child(self.buttons)

__all__ = ["UIEditorMenu"]

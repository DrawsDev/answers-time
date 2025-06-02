from typing import Callable
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.frame import Frame
from src.ui.layout import Layout

class UIQuizSelectMenu:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.layout = Layout(False)
        self.buttons = []
        self._create_back_button()
        self._create_frame()
        self.layout.insert_child(self.back, self.frame)
    
    def _create_frame(self) -> None:
        self.frame = Frame(
            game=self.game,
            color="#4E4E56",
            size=(420, 260),
            position=(self.game.surface.get_width() / 2, self.game.surface.get_height() / 2),
            anchor=Anchor.Center
        )

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

    def create_buttons(self, callback: Callable) -> None:
        self.layout.remove_child(self.buttons)
        self.buttons.clear()
        files = [file for file in os.listdir(asset_path(QUIZZES)) if file.endswith(".json")]
        for i in range(len(files)):
            button = TextButton(
                game=self.game,
                text=files[i],
                size=(40, 40),
                position=(self.game.surface.get_width() / 2 - self.frame.size[0] / 2 + 40 * i, self.game.surface.get_height() / 2 - self.frame.size[1] / 2),
                anchor=Anchor.TopLeft,
                font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
                font_size=16,
                font_align=Align.Center,
                text_color="white",
                button_color="#4E4E56",
                button_hover_color="#64646E",
                button_press_color="#000000"
            )
            button.pressed_callback = (callback, (files[i],))
            self.buttons.append(button)
        self.layout.insert_child(self.buttons)

__all__ = ["UIQuizSelectMenu"]

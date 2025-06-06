from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.text_box import TextBox
from src.ui.layout import Layout

class UINewQuizMenu:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.pos = (game.surface.get_width() / 2, game.surface.get_height() / 2)
        self.layout = Layout(False)
        self._create_back_button()
        self._create_create_button()
        self._create_name_input()
        self.layout.insert_child(self.back, self.create, self.name_input)
    
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
    
    def _create_create_button(self) -> None:
        self.create = TextButton(
            game=self.game,
            text="Создать",
            size=(130, 40),
            position=(self.pos[0], self.pos[1] + 2),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "add.png")
        )
    
    def _create_name_input(self) -> None:
        self.name_input = TextBox(
            game=self.game,
            text="",
            placeholder="Введите название теста",
            size=(300, 40),
            position=(self.pos[0], self.pos[1] - 3),
            anchor=Anchor.MidBottom,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color="white"
        )

__all__ = ["UINewQuizMenu"]

from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.image_label import ImageLabel
from src.ui.frame import Frame
from src.ui.layout import Layout

class UIStartMenu:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.layout = Layout(False)
        self._create_frame()
        self._create_tutorial_button()
        self._create_select_button()
        self.layout.insert_child(self.frame, self.tutorial, self.select)
    
    def _create_frame(self) -> None:
        self.frame = Frame(
            game=self.game,
            color=(0, 0, 0, 175),
            size=(144, self.game.surface.get_height()),
            position=(176, 0),
            anchor=Anchor.TopLeft
        )

    def _create_tutorial_button(self) -> None:
        self.tutorial = TextButton(
            game=self.game,
            text="Обучение",
            size=(144, 40),
            position=(176, 50),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color=(0, 0, 0, 0),
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "tutorial.png")
        )

    def _create_select_button(self) -> None:
        self.select = TextButton(
            game=self.game,
            text="Выбрать тест",
            size=(144, 40),
            position=(176, 90),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color=(0, 0, 0, 0),
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "select.png")
        )

__all__ = ["UIStartMenu"]

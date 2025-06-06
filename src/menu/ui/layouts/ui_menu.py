from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.image_label import ImageLabel
from src.ui.frame import Frame
from src.ui.layout import Layout

from src.ui.text_box import TextBox
from src.experimental.text_box import TextBox as TextBox2

class UIMenu:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.layout = Layout(True)
        self._create_logo()
        self._create_frame()
        self._create_start_button()
        self._create_editor_button()
        self._create_settings_button()
        self._create_about_button()
        self._create_exit_button()
        self.layout.insert_child(
            self.logo,
            self.frame,
            self.start,
            self.editor,
            self.settings,
            self.about,
            self.exit
        )
    
    def _create_logo(self) -> None:
        self.logo = ImageLabel(
            game=self.game, 
            path=asset_path(SPRITES, "new_logo.png"),
            position=(self.game.surface.get_width() - 32, self.game.surface.get_height() / 2),
            anchor=Anchor.MidRight
        )

    def _create_frame(self) -> None:
        self.frame = Frame(
            game=self.game,
            color=(0, 0, 0, 175),
            size=(144, self.game.surface.get_height()),
            position=(32, 0),
            anchor=Anchor.TopLeft,
            z_index=-1
        )

    def _create_start_button(self) -> None:
        self.start = TextButton(
            game=self.game,
            text="Начать тест",
            size=(144, 40),
            position=(32, 50),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color=(0, 0, 0, 0),
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "start.png")
        )

    def _create_editor_button(self) -> None:
        self.editor = TextButton(
            game=self.game,
            text="Редактор",
            size=(144, 40),
            position=(32, 90),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color=(0, 0, 0, 0),
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "editor.png")
        )

    def _create_settings_button(self) -> None:
        self.settings = TextButton(
            game=self.game,
            text="Настройки",
            size=(144, 40),
            position=(32, 130),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color=(0, 0, 0, 0),
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "settings.png")
        )

    def _create_about_button(self) -> None:
        self.about = TextButton(
            game=self.game,
            text="О программе",
            size=(144, 40),
            position=(32, 170),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color=(0, 0, 0, 0),
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "about.png")
        )

    def _create_exit_button(self) -> None:
        self.exit = TextButton(
            game=self.game,
            text="Выйти",
            size=(144, 40),
            position=(32, 210),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color=(0, 0, 0, 0),
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "exit.png")
        )

__all__ = ["UIMenu"]

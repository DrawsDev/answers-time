from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.frame import Frame
from src.ui.layout import Layout

class UIEditorQuizInfoMenu:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.pos = (self.game.surface.get_width() / 2, self.game.surface.get_height() / 2)
        self.layout = Layout(False)
        self._create_back_button()
        self._create_frame()
        self._create_open_button()
        self._create_delete_button()
        self.layout.insert_child(self.back, self.frame, self.open, self.delete)
    
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

    def _create_frame(self) -> None:
        self.frame = Frame(
            game=self.game,
            color="#4E4E56",
            size=(420, 260),
            position=(self.game.surface.get_width() / 2, self.game.surface.get_height() / 2),
            anchor=Anchor.Center
        )
    
    def _create_open_button(self) -> None:
        self.open = TextButton(
            game=self.game,
            text="Открыть в редакторе",
            size=(130, 40),
            position=(self.pos[0], self.pos[1] + 130),
            anchor=Anchor.BottomRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "test2.png")
        )

    def _create_delete_button(self) -> None:
        self.delete = TextButton(
            game=self.game,
            text="Удалить",
            size=(130, 40),
            position=(self.pos[0], self.pos[1] + 130),
            anchor=Anchor.BottomLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "test2.png")
        )

__all__ = ["UIEditorQuizInfoMenu"]

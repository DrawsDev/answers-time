from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *

class UIEditorQuizInfoMenu:
    def __init__(self, app: Application) -> None:
        self.app = app
        self.pos = (self.app.surface.get_width() / 2, self.app.surface.get_height() / 2)
        self.layout = Layout(False)
        self._create_back_button()
        self._create_frame()
        self._create_open_button()
        self._create_delete_button()
        self.layout.insert_child(self.back, self.frame, self.open, self.delete)
    
    def _create_back_button(self) -> None:
        self.back = TextButton(
            app=self.app,
            text="Назад",
            size=(130, 40),
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height()),
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
            app=self.app,
            color="#4E4E56",
            size=(420, 260),
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() / 2),
            anchor=Anchor.Center
        )
    
    def _create_open_button(self) -> None:
        self.open = TextButton(
            app=self.app,
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
            app=self.app,
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

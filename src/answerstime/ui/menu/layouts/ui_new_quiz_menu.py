from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *

class UINewQuizMenu:
    def __init__(self, app: Application) -> None:
        self.app = app
        self.pos = (app.surface.get_width() / 2, app.surface.get_height() / 2)
        self.layout = Layout(False)
        self._create_back_button()
        self._create_create_button()
        self._create_name_input()
        self.layout.insert_child(self.back, self.create, self.name_input)
    
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
    
    def _create_create_button(self) -> None:
        self.create = TextButton(
            app=self.app,
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
            app=self.app,
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

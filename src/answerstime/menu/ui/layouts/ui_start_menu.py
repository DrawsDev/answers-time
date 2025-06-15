from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *

class UIStartMenu:
    def __init__(self, app: Application) -> None:
        self.app = app
        self.layout = Layout(False)
        self._create_frame()
        self._create_tutorial_button()
        self._create_select_button()
        self.layout.insert_child(self.frame, self.tutorial, self.select)
    
    def _create_frame(self) -> None:
        self.frame = Frame(
            app=self.app,
            color=(0, 0, 0, 175),
            size=(144, self.app.surface.get_height()),
            position=(176, 0),
            anchor=Anchor.TopLeft,
            z_index=-1
        )

    def _create_tutorial_button(self) -> None:
        self.tutorial = TextButton(
            app=self.app,
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
            app=self.app,
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

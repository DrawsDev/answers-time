from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *

class UIMenu:
    def __init__(self, app: Application) -> None:
        self.app = app
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
            app=self.app, 
            path=asset_path(SPRITES, "new_logo.png"),
            position=(self.app.surface.get_width() - 32, self.app.surface.get_height() / 2),
            anchor=Anchor.MidRight
        )

    def _create_frame(self) -> None:
        self.frame = Frame(
            app=self.app,
            color=(0, 0, 0, 175),
            size=(144, self.app.surface.get_height()),
            position=(32, 0),
            anchor=Anchor.TopLeft,
            z_index=-1
        )

    def _create_start_button(self) -> None:
        self.start = TextButton(
            app=self.app,
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
            app=self.app,
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
            app=self.app,
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
            app=self.app,
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
            app=self.app,
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

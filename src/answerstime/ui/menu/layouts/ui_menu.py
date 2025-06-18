from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *

GAP = 4

class UIMenu:
    def __init__(self, app: Application) -> None:
        self.app = app
        self.layout = Layout(True)
        self._create_logo()
        self._create_build_label()
        self._create_title_label()
        self._create_start_quiz_button()
        self._create_tutorial_button()
        self._create_editor_button()
        self._create_settings_button()
        self._create_about_button()
        self._create_exit_button()
        self.layout.insert_child(
            self.logo,
            self.build,
            self.title,
            self.start,
            self.tutorial,
            self.editor,
            self.settings,
            self.about,
            self.exit
        )
    
    def _create_logo(self) -> None:
        self.logo = ImageLabel(
            app=self.app, 
            path=asset_path(SPRITES, "new_logo.png"),
            position=(self.app.surface.get_width() - 64, self.app.surface.get_height() / 2),
            anchor=Anchor.MidRight
        )

    def _create_build_label(self) -> None:
        self.build = TextLabel(
            app=self.app,
            text=f"Сборка {VERSION_MAJOR}.{VERSION_MINOR}.{BUILD}",
            position=(self.logo.rect.centerx, self.logo.rect.bottom + GAP),
            anchor=Anchor.MidTop,
            z_index=0,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=13,
            font_align=Align.Center,
            text_color=Pallete.White
        )        

    def _create_title_label(self) -> None:
        self.title = TextLabel(
            app=self.app,
            text="Главное меню",
            position=(42, 30),
            anchor=Anchor.TopLeft,
            z_index=0,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=22,
            font_align=Align.Left,
            text_color=Pallete.White
        )

    def _create_start_quiz_button(self) -> None:
        self.start = TextButton(
            app=self.app,
            text="Начать тест",
            size=(144, 40),
            position=(42, self.title.rect.bottom + GAP),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_icon=load_asset(SPRITES, "start.png"),
            button_border_radius=6
        )

    def _create_tutorial_button(self) -> None:
        self.tutorial = TextButton(
            app=self.app,
            text="Обучение",
            size=(144, 40),
            position=(42, self.start.rect.bottom + GAP),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_icon=load_asset(SPRITES, "tutorial.png"),
            button_border_radius=6
        )

    def _create_editor_button(self) -> None:
        self.editor = TextButton(
            app=self.app,
            text="Редактор",
            size=(144, 40),
            position=(42, self.tutorial.rect.bottom + GAP),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_icon=load_asset(SPRITES, "editor.png"),
            button_border_radius=6
        )

    def _create_settings_button(self) -> None:
        self.settings = TextButton(
            app=self.app,
            text="Настройки",
            size=(144, 40),
            position=(42, self.editor.rect.bottom + GAP),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_icon=load_asset(SPRITES, "settings.png"),
            button_border_radius=6
        )

    def _create_about_button(self) -> None:
        self.about = TextButton(
            app=self.app,
            text="О программе",
            size=(144, 40),
            position=(42, self.settings.rect.bottom + GAP),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_icon=load_asset(SPRITES, "about.png"),
            button_border_radius=6
        )

    def _create_exit_button(self) -> None:
        self.exit = TextButton(
            app=self.app,
            text="Выйти",
            size=(144, 40),
            position=(42, self.about.rect.bottom + GAP),
            anchor=Anchor.TopLeft,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_icon=load_asset(SPRITES, "exit.png"),
            button_border_radius=6
        )

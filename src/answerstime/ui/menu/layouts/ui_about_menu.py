from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *

GAP = 4

class UIAboutMenu:
    def __init__(self, app: Application) -> None:
        self.app = app
        self.pos = (self.app.surface.get_width() / 2, self.app.surface.get_height() / 2)
        self.layout = Layout(False)
        self._create_menu_title_label()
        self._create_back_button()
        self._create_scroll_frame()
        self._create_logo()
        self._create_version_label()
        self._create_copyright_label()
        self._create_github_button()
        self._create_itch_button()
        self._create_telegram_button()
        self.layout.insert_child(self.back, self.scroll_frame, self.menu_title, self.menu_title_line)
        self.scroll_frame.insert_child(self.logo, self.version, self.copyright, self.github, self.itch)
    
    def _create_scroll_frame(self) -> None:
        self.scroll_frame = ScrollFrame(
            app=self.app,
            size=(self.menu_title_line.rect.width, 285),
            position=(self.menu_title.rect.centerx, self.menu_title.rect.bottom + 5),
            anchor=Anchor.MidTop
        )
        self.scroll_frame.backcolor = (0, 0, 0, 0)
        self.scroll_frame.scrollbar_width = 15

    def _create_logo(self) -> None:
        self.logo = ImageLabel(
            app=self.app, 
            path=asset_path(SPRITES, "new_logo.png"),
            position=(self.scroll_frame.rect.centerx, self.scroll_frame.rect.centery - 20),
            anchor=Anchor.Center
        )

    def _create_version_label(self) -> None:
        self.version = TextLabel(
            app=self.app,
            text=f"Версия {VERSION_MAJOR}.{VERSION_MINOR} сборка {BUILD}",
            position=(self.pos[0], self.logo.rect.bottom),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=11,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.app.surface.get_width()
        )

    def _create_copyright_label(self) -> None:
        self.copyright = TextLabel(
            app=self.app,
            text="Copyright © 2025 DrawsDev",
            position=(self.pos[0], self.version.rect.bottom),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=11,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.app.surface.get_width()
        )

    def _create_menu_title_label(self) -> None:
        self.menu_title = TextLabel(
            app=self.app,
            text="О программе",
            position=(self.app.surface.get_width() / 2, 0),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            text_wraplength=self.app.surface.get_width()
        )

        self.menu_title_line = Frame(
            app=self.app,
            color=Pallete.White,
            size=(self.app.surface.get_width() - 10, 2),
            position=(self.app.surface.get_width() / 2, self.menu_title.rect.bottom),
            anchor=Anchor.MidTop
        )

    def _create_github_button(self) -> None:
        self.github = TextButton(
            app=self.app,
            text="GitHub. Исходный код программы",
            size=(self.scroll_frame.rect.width / 2, 60),
            position=(self.scroll_frame.rect.centerx, self.copyright.rect.bottom + 20),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "export.png"),
            button_border_radius=6
        )

    def _create_itch_button(self) -> None:
        self.itch = TextButton(
            app=self.app,
            text="Itch.io. Страница программы на itch.io",
            size=(self.scroll_frame.rect.width / 2, 60),
            position=(self.scroll_frame.rect.centerx, self.github.rect.bottom + GAP),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#FF2449",
            button_hover_color="#FF2E51",
            button_press_color="#E1193B",
            button_icon=load_asset(SPRITES, "export.png"),
            button_border_radius=6
        )

    def _create_telegram_button(self) -> None:
        self.telegram = TextButton(
            app=self.app,
            text="Itch.io. Страница программы на itch.io",
            size=(self.scroll_frame.rect.width / 2, 40),
            position=(self.scroll_frame.rect.centerx, self.copyright.rect.bottom + GAP),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "back.png"),
            button_border_radius=6
        )

    def _create_back_button(self) -> None:
        self.back = TextButton(
            app=self.app,
            text="Вернуться в меню",
            size=(130, 40),
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() - GAP),
            anchor=Anchor.MidBottom,
            z_index=1,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_icon=load_asset(SPRITES, "back.png"),
            button_border_radius=6
        )

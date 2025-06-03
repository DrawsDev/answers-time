from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.image_label import ImageLabel
from src.ui.layout import Layout
from src.ui.scroll_frame import ScrollFrame
from src.ui.frame import Frame
from src.ui.text_box import TextBox

class UIAboutMenu:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.pos = (self.game.surface.get_width() / 2, self.game.surface.get_height() / 2)
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
            game=self.game,
            size=(self.menu_title_line.rect.width, 285),
            position=(self.menu_title.rect.centerx, self.menu_title.rect.bottom + 5),
            anchor=Anchor.MidTop
        )
        self.scroll_frame.backcolor = (0, 0, 0, 0)
        self.scroll_frame.scrollbar_width = 15

    def _create_logo(self) -> None:
        self.logo = ImageLabel(
            game=self.game, 
            path=asset_path(SPRITES, "new_logo.png"),
            position=(self.scroll_frame.rect.centerx, self.scroll_frame.rect.centery - 20),
            anchor=Anchor.Center
        )

    def _create_version_label(self) -> None:
        self.version = TextLabel(
            game=self.game,
            text="Версия 1.0 сборка 0",
            position=(self.pos[0], self.logo.rect.bottom),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=11,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.game.surface.get_width()
        )

    def _create_copyright_label(self) -> None:
        self.copyright = TextLabel(
            game=self.game,
            text="Copyright © 2025 DrawsDev",
            position=(self.pos[0], self.version.rect.bottom),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=11,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.game.surface.get_width()
        )

    def _create_menu_title_label(self) -> None:
        self.menu_title = TextLabel(
            game=self.game,
            text="О программе",
            position=(self.game.surface.get_width() / 2, 0),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="#3CA4FF",
            text_wraplength=self.game.surface.get_width()
        )

        self.menu_title_line = Frame(
            game=self.game,
            color="#3CA4FF",
            size=(self.game.surface.get_width() - 10, 2),
            position=(self.game.surface.get_width() / 2, self.menu_title.rect.bottom),
            anchor=Anchor.MidTop
        )

    def _create_github_button(self) -> None:
        self.github = TextButton(
            game=self.game,
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
            button_icon=load_asset(SPRITES, "exit.png")
        )

    def _create_itch_button(self) -> None:
        self.itch = TextButton(
            game=self.game,
            text="Itch.io. Страница программы на itch.io",
            size=(self.scroll_frame.rect.width / 2, 60),
            position=(self.scroll_frame.rect.centerx, self.github.rect.bottom + 5),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "exit.png")
        )

    def _create_telegram_button(self) -> None:
        self.telegram = TextButton(
            game=self.game,
            text="Itch.io. Страница программы на itch.io",
            size=(self.scroll_frame.rect.width / 2, 40),
            position=(self.scroll_frame.rect.centerx, self.copyright.rect.bottom + 20),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "back.png")
        )

    def _create_back_button(self) -> None:
        self.back = TextButton(
            game=self.game,
            text="Назад",
            size=(130, 40),
            position=(self.game.surface.get_width() / 2, self.game.surface.get_height() - 5),
            anchor=Anchor.MidBottom,
            z_index=1,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "back.png")
        )

__all__ = ["UIAboutMenu"]

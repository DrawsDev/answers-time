import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *

GAP = 4

class UISelectExportType:
    def __init__(self, app: Application) -> None:
        self.app = app
        self._enabled = False
        self._layout = Layout(False)
        self._create_title_label()
        self._create_title_line()
        self._create_back_button()
        self._create_from_exists_quiz_button()
        self._create_from_file_button()
        self._layout.insert_child(
            self.title,
            self.title_line,
            self.back,
            self.from_exists_quiz,
            self.from_file
        )

    @property
    def enabled(self) -> bool:
        return self._enabled
    
    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value
        self._layout.enabled = value

    def update(self, delta: float) -> None:
        if self._enabled:
            self._layout.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        if self._enabled:
            self._layout.draw(surface)

    def _create_title_label(self) -> TextLabel:
        self.title = TextLabel(
            app=self.app,
            text="Экспорт",
            position=(self.app.surface.get_width() / 2, 0),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            text_wraplength=self.app.surface.get_width()
        )
    
    def _create_title_line(self) -> Frame:
        self.title_line = Frame(
            app=self.app,
            color=Pallete.White,
            size=(self.app.surface.get_width() - 10, 2),
            position=(self.title.rect.centerx, self.title.rect.bottom),
            anchor=Anchor.MidTop
        )

    def _create_back_button(self) -> None:
        self.back = TextButton(
            app=self.app,
            text="Назад",
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

    def _create_from_exists_quiz_button(self) -> None:
        self.from_exists_quiz = TextButton(
            app=self.app,
            text="Экспорт файла с тестом",
            size=(260, 40),
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() / 2 - GAP),
            anchor=Anchor.MidBottom,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_icon=load_asset(SPRITES, "export.png"),
            button_border_radius=6
        )

    def _create_from_file_button(self) -> None:
        self.from_file = TextButton(
            app=self.app,
            text="Скомпоновать в отдельный исполняемый файл",
            size=(260, 40),
            position=(self.from_exists_quiz.rect.centerx, self.from_exists_quiz.rect.bottom + GAP),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_icon=load_asset(SPRITES, "export.png"),
            button_border_radius=6
        )

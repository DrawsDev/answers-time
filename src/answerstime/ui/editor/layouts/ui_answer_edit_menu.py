import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *

GAP = 4

class UIAnswerEditMenu:
    def __init__(self, app: Application) -> None:
        self.app = app
        self._enabled = True
        self._layout = Layout(False)
        self._create_title_label()
        self._create_title_line()
        self._create_back_button()
        self._create_text_1_textbox()
        self._create_text_2_textbox()
        self._layout.insert_child(
            self.title,
            self.title_line,
            self.back,
            self.text_1
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

    def change_state(self, index: int = 0) -> None:
        if index == 0:
            self._layout.remove_child(self.text_2)
            self.text_1.placeholder = "Введите текст ответа"
            self.text_1.position = (self.app.surface.get_width() / 2, self.app.surface.get_height() / 2)
            self.text_1.anchor = Anchor.Center
        elif index == 1:
            self._layout.insert_child(self.text_2)
            self.text_1.placeholder = "Введите текста верхнего варианта"
            self.text_1.position = (self.app.surface.get_width() / 2, self.app.surface.get_height() / 2 - GAP / 2)
            self.text_1.anchor = Anchor.MidBottom

    def _create_title_label(self) -> None:
        self.title = TextLabel(
            app=self.app,
            text="Настройка ответа",
            position=(self.app.surface.get_width() / 2, 0),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.app.surface.get_width()
        )
    
    def _create_title_line(self) -> None:
        self.title_line = Frame(
            app=self.app,
            color="white",
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
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#000000",
            button_icon=load_asset(SPRITES, "back.png")
        )

    def _create_text_1_textbox(self) -> None:
        self.text_1 = TextBox(
            app=self.app,
            text="",
            placeholder="Введите текст ответа",
            size=(300, 80),
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() / 2),
            anchor=Anchor.Center,
            z_index=1,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color="white"
        )

    def _create_text_2_textbox(self) -> None:
        self.text_2 = TextBox(
            app=self.app,
            text="",
            placeholder="Введите текст нижнего варианта",
            size=(300, 80),
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() / 2 + GAP / 2),
            anchor=Anchor.MidTop,
            z_index=1,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Left,
            text_color="white"
        )

import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *

GAP = 4

class UITip:
    def __init__(self, app: Application) -> None:
        self.app = app
        self._enabled = False
        self._layout = Layout(False)
        self._create_text_label()
        self._create_title_line()
        self._create_title_label()
        self._create_back_button()
        self._layout.insert_child(
            self.text,
            self.title,
            self.title_line,
            self.back
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

    def set_tip(self, text: str) -> None:
        if self.text.text != text:
            self.text.text = text

    def _create_title_label(self) -> TextLabel:
        self.title = TextLabel(
            app=self.app,
            text="Подсказка",
            position=(self.title_line.rect.centerx, self.title_line.rect.top),
            anchor=Anchor.MidBottom,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.app.surface.get_width()
        )
    
    def _create_title_line(self) -> Frame:
        self.title_line = Frame(
            app=self.app,
            color="white",
            size=(self.app.surface.get_width() / 2, 2),
            position=(self.text.rect.centerx, self.text.rect.top - GAP),
            anchor=Anchor.MidBottom
        )

    def _create_text_label(self) -> TextLabel:
        self.text = TextLabel(
            app=self.app,
            text="Текст подсказки",
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() / 2),
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.app.surface.get_width()
        )

    def _create_back_button(self) -> None:
        self.back = TextButton(
            app=self.app,
            text="Вернуться к тесту",
            size=(130, 40),
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() - GAP),
            anchor=Anchor.MidBottom,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color=Pallete.White,
            button_color=Pallete.ATBlue3,
            button_hover_color=Pallete.ATBlue2,
            button_press_color=Pallete.ATBlue4,
            button_border_radius=6,
            button_icon=load_asset(SPRITES, "back.png")
        )

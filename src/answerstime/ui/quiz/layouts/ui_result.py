import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *

GAP = 4

class UIResult:
    def __init__(self, app: Application) -> None:
        self.app = app
        self._enabled = False
        self._layout = Layout(False)
        self._create_rating_label()
        self._create_info_label()
        self._create_back_button()
        self._layout.insert_child(
            self.rating,
            self.info,
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

    def _create_rating_label(self) -> TextLabel:
        self.rating = TextLabel(
            app=self.app,
            text="5",
            position=(self.app.surface.get_width() / 2, self.app.surface.get_height() / 2 - 20),
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=55,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.app.surface.get_width()
        )

    def _create_info_label(self) -> TextLabel:
        self.info = TextLabel(
            app=self.app,
            text="Правильных ответов: 0 из 0",
            position=(self.rating.rect.centerx, self.rating.rect.bottom + 10),
            anchor=Anchor.MidTop,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.app.surface.get_width()
        )

    def _create_back_button(self) -> None:
        self.back = TextButton(
            app=self.app,
            text="Выйти",
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
            button_icon=load_asset("back.png")
        )

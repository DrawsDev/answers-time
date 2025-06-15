import pygame
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *

GAP = 4

class UITimer:
    def __init__(self, app: Application) -> None:
        self.app = app
        self._enabled = True
        self._layout = Layout(True)
        self._create_timer_label()
        self._layout.insert_child(
            self.timer
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

    def _create_timer_label(self) -> TextLabel:
        self.timer = TextLabel(
            app=self.app,
            text="Оставшееся время: 0 с",
            position=(self.app.surface.get_width() - GAP, GAP),
            anchor=Anchor.TopRight,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Right,
            text_color="white",
            text_wraplength=self.app.surface.get_width()
        )

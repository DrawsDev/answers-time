import pygame
from typing import Tuple
from src.framework.enums import *
from src.framework.settings import *
from src.framework.application import Application
from src.framework.utility import *
from src.framework.scene.ui import *

GAP = 4

class InputAnswer(Primitive):
    def __init__(        
        self, 
        app: Application,
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
    ) -> None:
        super().__init__(app, (200, 90), position, anchor, 1)
        self._create_text_box()
        self._layout: Layout = Layout(True)
        self._layout.insert_child(self.textbox)
        self._update_image()

    def update(self, delta: float) -> None:
        super().update(delta)
        if self._layout.enabled:
            self._layout.update(delta)
 
    def draw(self, surface: pygame.Surface) -> None:
        super().draw(surface)
        if self._layout.enabled:
            self._layout.draw(surface)

    def _create_text_box(self) -> None:
        self.textbox = TextBox(
            app=self.app,
            text="",
            placeholder="Введите ответ",
            size=(300, 40),
            position=self.rect.center,
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white"
        )

import pygame
from typing import Tuple
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.base.ui_button import UIObject
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.image_label import ImageLabel
from src.ui.layout import Layout

GAP = 4

class XobjectiveAnswer(UIObject):
    def __init__(        
        self, 
        game: Game,
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
    ) -> None:
        super().__init__(game, (200, 90), position, anchor, 1)
        self._is_correct = False
        self._create_is_right_button()
        self._create_text_label()
        self._create_icon_label()
        self._layout: Layout = Layout(False)
        self._layout.insert_child(self.is_right)
        self._update_image()

    def update(self, delta: float) -> None:
        super().update(delta)
        if self._layout.enabled:
            self._layout.update(delta)
        else:
            self.text.update(delta)
            self.icon.update(delta)
    
    def draw(self, surface: pygame.Surface) -> None:
        super().draw(surface)
        if self._layout.enabled:
            self._layout.draw(surface)
        else:
            self.text.draw(surface)
            self.icon.draw(surface)
            surface.blit(self.icon.image, self.icon.rect)
            surface.blit(self.text.image, self.text.rect)

    def on_mouse_enter(self) -> None:
        self._layout.enabled = True

    def on_mouse_leave(self) -> None:
        self._layout.enabled = False

    def change_correct_state(self, value: bool = False) -> None:
        if self._is_correct != value:
            self._is_correct = value
            if value:
                self.icon.image_path = asset_path(SPRITES, "editor_correct_2.png")
            else:
                self.icon.image_path = None

    def _update_image(self):
        super()._update_image()
        self.image.fill("#747484")

    def _create_is_right_button(self) -> None:
        self.is_right = TextButton(
            game=self.game,
            text="",
            size=(34, 34),
            position=self.rect.center,
            anchor=Anchor.Center,
            z_index=3,
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#282835",
            button_icon=load_asset(SPRITES, "editor_correct.png")
        )

    def _create_text_label(self) -> None:
        self.text = TextLabel(
            game=self.game,
            text="test",
            position=self.rect.center,
            anchor=Anchor.Center,
            font_path=asset_path(FONTS, "Ramona-Bold.ttf"),
            font_size=16,
            font_align=Align.Center,
            text_color="white",
            text_wraplength=self.rect.width
        )

    def _create_icon_label(self) -> None:
        self.icon = ImageLabel(
            game=self.game,
            path=None,
            position=self.rect.topright,
            anchor=Anchor.TopRight,
            z_index=1
        )

__all__ = ["XobjectiveAnswer"]

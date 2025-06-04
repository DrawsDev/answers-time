import pygame
from typing import Tuple
from src.enums import *
from src.settings import *
from src.core.game import Game
from src.core.utility import load_asset, asset_path
from src.ui.base.ui_button import UIObject
from src.ui.text_button import TextButton
from src.ui.text_label import TextLabel
from src.ui.layout import Layout

class AnswerObject(UIObject):
    def __init__(        
        self, 
        game: Game,
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
    ) -> None:
        super().__init__(game, (200, 90), position, anchor, 1)# "#4E4E56", "#64646E", "#282835")
        self._create_edit_button()
        self._create_delete_button()
        self._create_move_button()
        self._create_text_label()
        self._layout: Layout = Layout(False)
        self._layout.insert_child(self.edit, self.delete, self.move)
        self._update_image()

    def update(self, delta: float) -> None:
        super().update(delta)
        if self._layout.enabled:
            self._layout.update(delta)
        else:
            self.text.update(delta)
    
    def draw(self, surface: pygame.Surface) -> None:
        super().draw(surface)
        if self._layout.enabled:
            self._layout.draw(surface)
        else:
            self.text.draw(surface)
            surface.blit(self.text.image, self.text.rect)

    def on_mouse_enter(self) -> None:
        self._layout.enabled = True

    def on_mouse_leave(self) -> None:
        self._layout.enabled = False

    def _update_image(self):
        super()._update_image()
        self.image.fill("#4E4E56")

    def _create_edit_button(self) -> None:
        self.edit = TextButton(
            game=self.game,
            text="",
            size=(34, 34),
            position=(self.rect.centerx - 38, self.rect.centery),
            anchor=Anchor.Center,
            z_index=3,
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#282835",
            button_icon=load_asset(SPRITES, "settings.png")
        )

    def _create_delete_button(self) -> None:
        self.delete = TextButton(
            game=self.game,
            text="",
            size=(34, 34),
            position=self.rect.center,
            anchor=Anchor.Center,
            z_index=3,
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#282835",
            button_icon=load_asset(SPRITES, "delete.png")
        )

    def _create_move_button(self) -> None:
        self.move = TextButton(
            game=self.game,
            text="",
            size=(34, 34),
            position=(self.rect.centerx + 38, self.rect.centery),
            anchor=Anchor.Center,
            z_index=3,
            button_color="#4E4E56",
            button_hover_color="#64646E",
            button_press_color="#282835",
            button_icon=load_asset(SPRITES, "test2.png")
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

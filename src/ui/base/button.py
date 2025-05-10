import pygame
from typing import Tuple
from src.core.game import Game
from src.ui.base.object import UIObject

class UIButton(UIObject):
    def __init__(self, 
                 game: Game, 
                 size: Tuple[int, int] = [100, 100], 
                 position: Tuple[int, int] = [0, 0]
                 ):
        super().__init__(game, size, position)

        self._down = False
        self._pressed = False
        self._button_color = "lavenderblush1"
        self._button_hover_color = "lavenderblush2"
        self._button_press_color = "lavenderblush3"
        self.image.fill(self._button_color)

    @property
    def pressed(self) -> bool:
        return self._pressed

    def on_mouse_pressed(self) -> None:
        self.image.fill(self._button_press_color)
        self._down = True

    def on_mouse_released(self) -> None:
        self.image.fill(self._button_hover_color if self._mouse_entered else self._button_color)
        if self._down:
            self._pressed = True
        self._down = False

    def on_mouse_enter(self):
        self.image.fill(self._button_press_color if self._down else self._button_hover_color)
    
    def on_mouse_leave(self):
        self.image.fill(self._button_color)

    def _mouse_handler(self, delta):
        super()._mouse_handler(delta)

        if self._mouse_entered:
            self._pressed = False

            if self.game.input.is_key_pressed("m_left"):
                self.on_mouse_pressed()
            if self.game.input.is_key_released("m_left"):
                self.on_mouse_released()
        else:
            if self._down and self.game.input.is_key_released("m_left"):
                self._down = False
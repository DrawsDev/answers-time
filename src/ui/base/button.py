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

        self._button_color = "lavenderblush1"
        self._button_hover_color = "lavenderblush2"
        self._button_press_color = "lavenderblush3"
        self.image.fill(self._button_color)

    def on_mouse_pressed(self, buttons: Tuple[bool, bool, bool, bool, bool]) -> None:
        if buttons[0]:
            self.image.fill(self._button_press_color)

    def on_mouse_released(self, buttons: Tuple[bool, bool, bool, bool, bool]) -> None:
        if buttons[0]:
            self.image.fill(self._button_hover_color if self._mouse_entered else self._button_color)

    def on_mouse_enter(self):
        self.image.fill(self._button_hover_color)
    
    def on_mouse_leave(self):
        self.image.fill(self._button_color)

    def _mouse_handler(self, delta):
        super()._mouse_handler(delta)
        if self._mouse_entered:
            self.on_mouse_pressed(pygame.mouse.get_just_pressed())
            self.on_mouse_released(pygame.mouse.get_just_released())

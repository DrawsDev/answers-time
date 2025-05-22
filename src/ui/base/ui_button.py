import pygame
from typing import Tuple
from src.enums import ButtonState
from src.core.game import Game
from src.ui.base.ui_object import UIObject

class UIButton(UIObject):
    def __init__(self, 
                 game: Game, 
                 size: Tuple[int, int] = [100, 100], 
                 position: Tuple[int, int] = [0, 0]
                 ):
        super().__init__(game, size, position)
        self._selectable = True
        self._down = False
        self._pressed = False
        self._button_size = size
        self._button_color = "lavenderblush1"
        self._button_hover_color = "lavenderblush2"
        self._button_press_color = "lavenderblush3"
        self._set_state(ButtonState.Idle)

    @property
    def pressed(self) -> bool:
        if self._pressed:
            self._pressed = False
            return True
        return False

    @property
    def button_color(self) -> pygame.Color:
        return self._button_color

    @property
    def button_hover_color(self) -> pygame.Color:
        return self._button_hover_color

    @property
    def button_press_color(self) -> pygame.Color:
        return self._button_press_color

    @property
    def button_state(self) -> ButtonState:
        return self._state

    @button_color.setter
    def button_color(self, value: pygame.Color) -> None:
        self._button_color = value
        self._set_state(self._state)

    @button_hover_color.setter
    def button_hover_color(self, value: pygame.Color) -> None:
        self._button_hover_color = value
        self._set_state(self._state)

    @button_press_color.setter
    def button_press_color(self, value: pygame.Color) -> None:
        self._button_press_color = value
        self._set_state(self._state)

    def on_mouse_pressed(self) -> None:
        self._set_state(ButtonState.Press)
        self._down = True

    def on_mouse_released(self) -> None:
        self._set_state(ButtonState.Hover if self._mouse_entered else ButtonState.Idle)
        if self._down:
            self._pressed = True
        self._down = False

    def on_mouse_enter(self) -> None:
        self._set_state(ButtonState.Press if self._down else ButtonState.Hover)
    
    def on_mouse_leave(self) -> None:
        self._set_state(ButtonState.Idle)

    def _mouse_handler(self, delta: float) -> None:
        super()._mouse_handler(delta)

        if self._mouse_entered:
            if self.game.input.is_key_pressed("m_left") or self._selected and self.game.input.is_key_pressed("return"):
                self.on_mouse_pressed()
            if self.game.input.is_key_released("m_left") or self._selected and self.game.input.is_key_released("return"):
                self.on_mouse_released()
        else:
            if self._down and (self.game.input.is_key_released("m_left") or self.game.input.is_key_released("return")):
                self._down = False #TODO: Здесь ошибка: если зажать мышкой и отвести её, потом нажать Enter, то тоже сработает.

    def _set_state(self, state: ButtonState) -> None:
        self._state = state
        self._update_image()

    def _update_image(self) -> None:
        super()._update_image()
        if self._state == ButtonState.Idle:
            self.image.fill(self._button_color)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        elif self._state == ButtonState.Hover:
            self.image.fill(self._button_hover_color)
        elif self._state == ButtonState.Press:
            self.image.fill(self._button_press_color)

    def update(self, delta):
        super().update(delta)
        
        if self._active and self._state in (ButtonState.Hover, ButtonState.Press):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

__all__ = ["UIButton"]

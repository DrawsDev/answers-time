import pygame
from typing import Tuple, Optional
from src.framework.enums import *
from src.framework.application import Application
from src.framework.callback import *
from src.framework.scene.ui import Primitive

class PrimitiveButton(Primitive):
    def __init__(
        self, 
        app: Application, 
        size: Tuple[int, int] = (100, 100), 
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
        z_index: int = 0,
        button_color: pygame.Color = "azure2",
        button_hover_color: pygame.Color = "azure3",
        button_press_color: pygame.Color = "azure4",
        button_border_radius: int = -1,
    ) -> None:
        super().__init__(app, size, position, anchor, z_index)
        self._selectable = True
        self._down = False
        self._pressed = False
        self._button_color = button_color
        self._button_hover_color = button_hover_color
        self._button_press_color = button_press_color
        self._button_border_radius = button_border_radius
        self._pressed_callback: Callback = Callback()
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

    @property
    def pressed_callback(self) -> Callback:
        return self._pressed_callback

    @pressed_callback.setter
    def pressed_callback(self, value: Optional[CallbackType]):
        if self._pressed_callback != value:
            self._pressed_callback.set(value)

    @property
    def button_border_radius(self) -> int:
        return self._button_border_radius
    
    @button_border_radius.setter
    def button_border_radius(self, value: int) -> None:
        if value >= -1:
            self._button_border_radius = value
            self._update_image()

    def on_mouse_pressed(self) -> None:
        self._set_state(ButtonState.Press)
        self._down = True

    def on_mouse_released(self) -> None:
        self._set_state(ButtonState.Hover if self._mouse_entered else ButtonState.Idle)
        if self._down:
            self._pressed = True
            self._pressed_callback()
        self._down = False

    def on_mouse_enter(self) -> None:
        self._set_state(ButtonState.Press if self._down else ButtonState.Hover)
    
    def on_mouse_leave(self) -> None:
        self._set_state(ButtonState.Idle)

    def _mouse_handler(self, delta: float) -> None:
        super()._mouse_handler(delta)

        if self._mouse_entered:
            if self.app.input.is_key_pressed("m_left") or self._selected and self.app.input.is_key_pressed("return"):
                self.on_mouse_pressed()
            if self.app.input.is_key_released("m_left") or self._selected and self.app.input.is_key_released("return"):
                self.on_mouse_released()
        else:
            if self._down and (self.app.input.is_key_released("m_left") or self.app.input.is_key_released("return")):
                self._down = False #TODO: Здесь ошибка: если зажать мышкой и отвести её, потом нажать Enter, то тоже сработает.

    def _set_state(self, state: ButtonState) -> None:
        self._state = state
        self._update_image()

    def _update_image(self) -> None:
        super()._update_image()
        if self._state == ButtonState.Idle:
            pygame.draw.rect(self.image, self._button_color, ((0, 0), self.rect.size), border_radius=self._button_border_radius)
            # pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        elif self._state == ButtonState.Hover:
            pygame.draw.rect(self.image, self._button_hover_color, ((0, 0), self.rect.size), border_radius=self._button_border_radius)
        elif self._state == ButtonState.Press:
            pygame.draw.rect(self.image, self._button_press_color, ((0, 0), self.rect.size), border_radius=self._button_border_radius)

    def update(self, delta):
        super().update(delta)
        
        if self._active and self._state in (ButtonState.Hover, ButtonState.Press):
            pass # pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

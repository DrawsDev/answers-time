import pygame
from typing import Tuple
from src.settings import SURFACE_SIZE

MOUSE_KEY_ALIASES = ("m_none", "m_left", "m_middle", "m_right", "m_wheel_up", "m_wheel_down", "m_extra_1", "m_extra_2")

class Input:
    def __init__(self):
        self._released_keys = set()
        self._pressed_keys = set()
        self._down_keys = set()
        self._mouse_moved = False
        self._mouse_position = (0, 0)
        self._mouse_activity = False
        self._unicode = ""
    
    @property
    def mouse_position(self) -> Tuple[int, int]:
        return self.get_mouse_position()

    def get_mouse_position(self) -> Tuple[int, int]:
        window_size = pygame.display.get_window_size()
        ratio = (
            window_size[0] / SURFACE_SIZE[0], 
            window_size[1] / SURFACE_SIZE[1]
        )
        ratio_mouse_position = (
            self._mouse_position[0] / ratio[0], 
            self._mouse_position[1] / ratio[1]
        )
        return ratio_mouse_position

    def is_mouse_activity(self) -> bool:
        return self._mouse_activity

    def is_mouse_moved(self) -> bool:
        return self._mouse_moved

    def get_unicode(self) -> str:
        return self._unicode

    def get_axis(self, positive_key: str, negative_key: str) -> int:
        key1 = int(self.is_key_down(positive_key))
        key2 = int(self.is_key_down(negative_key))
        return key1 - key2
    
    def is_key_pressed(self, key: str) -> bool:
        return key in self._pressed_keys

    def is_key_released(self, key: str) -> bool:
        return key in self._released_keys

    def is_key_down(self, key: str) -> bool:
        return key in self._down_keys

    def is_anything_pressed(self) -> bool:
        return len(self._pressed_keys) > 0

    def update(self) -> None:
        self._pressed_keys.clear()
        self._released_keys.clear()
        self._unicode = ""
        self._mouse_moved = False
        self._mouse_activity = False

    def handle_event(self, event: pygame.Event) -> None:
        if event.type == pygame.KEYUP:
            key_name = pygame.key.name(event.key)
            self._down_keys.discard(key_name)
            self._released_keys.add(key_name)

        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            self._down_keys.add(key_name)
            self._pressed_keys.add(key_name)

        if event.type == pygame.MOUSEBUTTONUP:
            key_name = MOUSE_KEY_ALIASES[event.button]
            self._down_keys.discard(key_name)
            self._released_keys.add(key_name)
            self._mouse_activity = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            key_name = MOUSE_KEY_ALIASES[event.button]
            self._down_keys.add(key_name)
            self._pressed_keys.add(key_name)
            self._mouse_activity = True

        if event.type == pygame.MOUSEWHEEL:
            self._mouse_activity = True

        if event.type == pygame.MOUSEMOTION:
            self._mouse_moved = True
            self._mouse_position = event.pos
            self._mouse_activity = True

        if event.type == pygame.TEXTINPUT:
            self._unicode = event.text

        if self.is_key_pressed("f11"):
            pygame.display.toggle_fullscreen()

__all__ = ["Input"]

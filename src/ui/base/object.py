import pygame
from typing import Tuple
from src.enums import Anchor
from src.settings import *
from src.core.game import Game

class UIObject(pygame.sprite.Sprite):
    def __init__(self, 
                 game: Game, 
                 size: Tuple[int, int] = [100, 100], 
                 position: Tuple[int, int] = [0, 0]
                 ):
        super().__init__()
        self.game = game
        self.image = pygame.Surface(size)
        
        self._active = True
        self._position = position
        self._anchor = Anchor.TopLeft
        self._mouse_entered = False
        self._mouse_previous_position = [0, 0]
        self._update_rect()

    @property
    def active(self) -> bool:
        return self._active

    @property
    def position(self) -> Tuple[int, int]:
        return self._position

    @property
    def anchor(self) -> Anchor:
        return self._anchor

    @active.setter
    def active(self, value: bool) -> None:
        self._active = value

    @position.setter
    def position(self, value: Tuple[int, int]) -> None:
        self._position = value
        self._update_rect()

    @anchor.setter
    def anchor(self, value: Anchor) -> None:
        self._anchor = value
        self._update_rect()

    def on_mouse_enter(self) -> None: ...

    def on_mouse_leave(self) -> None: ...

    def on_mouse_moved(self) -> None: ...

    def _mouse_enter_handler(self) -> None:
        if not self._mouse_entered:
            self._mouse_entered = True
            self.on_mouse_enter()

    def _mouse_leave_handler(self) -> None:
        if self._mouse_entered:
            self._mouse_entered = False
            self.on_mouse_leave()

    def _mouse_moved_handler(self) -> None:
        mouse_position = pygame.mouse.get_pos()
        x_diff = mouse_position[0] - self._mouse_previous_position[0]
        y_diff = mouse_position[1] - self._mouse_previous_position[1]

        if self._mouse_entered and not (x_diff == y_diff == 0):
            self.on_mouse_moved()

        self._mouse_previous_position = mouse_position
    
    def _mouse_handler(self, delta: float) -> None:
        mouse_position = pygame.mouse.get_pos()
        ratio = [WINDOW_SIZE[0] / SURFACE_SIZE[0], WINDOW_SIZE[1] / SURFACE_SIZE[1]]

        if self.rect.collidepoint(mouse_position[0] / ratio[0], mouse_position[1] / ratio[1]):
            self._mouse_enter_handler()
            self._mouse_moved_handler()
        else:
            self._mouse_leave_handler()

    def _update_rect(self) -> None:
        self.rect = self.image.get_rect(**{self._anchor: self._position})

    def draw(self, surface: pygame.Surface) -> None: ...

    def update(self, delta: float) -> None:
        if self._active:
            self._mouse_handler(delta)

__all__ = ["UIObject"]

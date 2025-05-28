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
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        
        self._selectable = False
        self._selected = False
        self._active = True
        self._size = size
        self._position = position
        self._anchor = Anchor.TopLeft
        self._mouse_entered = False
        self._update_rect()

    @property
    def selectable(self) -> bool:
        return self._selectable

    @property
    def selected(self) -> bool:
        return self._selected

    @property
    def active(self) -> bool:
        return self._active

    @property
    def size(self) -> Tuple[int, int]:
        return self._size

    @property
    def position(self) -> Tuple[int, int]:
        return self._position

    @property
    def anchor(self) -> Anchor:
        return self._anchor

    @selectable.setter
    def selectable(self, value: bool) -> None:
        self._selectable = value
        self._selected = self._selected and value

    @selected.setter
    def selected(self, value: bool) -> None:
        self._selected = self._selectable and value

    @active.setter
    def active(self, value: bool) -> None:
        self._active = value

    @size.setter
    def size(self, value: Tuple[int, int]) -> None:
        self._size = value
        self._update_image()

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
        if self.game.input.is_mouse_moved():
            self.on_mouse_moved()
    
    def _mouse_handler(self, delta: float) -> None:
        mouse_position = pygame.mouse.get_pos()
        window_size = pygame.display.get_window_size()
        ratio = [window_size[0] / SURFACE_SIZE[0], window_size[1] / SURFACE_SIZE[1]]

        if self.rect.collidepoint(mouse_position[0] / ratio[0], mouse_position[1] / ratio[1]) or self._selected:
            self._mouse_enter_handler()
            self._mouse_moved_handler()
        else:
            self._mouse_leave_handler()

    def _update_image(self) -> None:
        self.image = pygame.Surface(self._size, pygame.SRCALPHA)
        self._update_rect()

    def _update_rect(self) -> None:
        self.rect = self.image.get_rect(**{self._anchor: self._position})

    def draw(self, surface: pygame.Surface) -> None: ...

    def update(self, delta: float) -> None:
        if self._active:
            self._mouse_handler(delta)

__all__ = ["UIObject"]

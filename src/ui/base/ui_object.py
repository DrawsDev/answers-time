import pygame
from typing import Tuple, List
from src.enums import Anchor
from src.settings import *
from src.core.game import Game

class UIObject(pygame.sprite.Sprite):
    def __init__(
        self, 
        game: Game, 
        size: Tuple[int, int] = (100, 100), 
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft,
        z_index: int = 0
    ) -> None:
        super().__init__()
        self.game = game
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self._selectable = False
        self._selected = False
        self._active = True
        self._mouse_entered = False
        self._z_index = z_index
        self._size = size
        self._position = position
        self._anchor = anchor
        self._update_rect()

    @property
    def selectable(self) -> bool:
        return self._selectable

    @selectable.setter
    def selectable(self, value: bool) -> None:
        if self._selectable != value:
            self._selectable = value

    @property
    def selected(self) -> bool:
        return self._selected

    @selected.setter
    def selected(self, value: bool) -> None:
        if self._selectable and self._selected != value:
            self._selected = value

    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, value: bool) -> None:
        if self._active != value:
            self._active = value

    @property
    def z_index(self) -> int:
        return self._z_index

    @z_index.setter
    def z_index(self, value: int) -> None:
        if self._z_index != value:
            self._z_index = value

    @property
    def size(self) -> Tuple[int, int]:
        return self._size

    @size.setter
    def size(self, value: Tuple[int, int]) -> None:
        if self._size != value:
            self._size = value
            self._update_image()

    @property
    def position(self) -> Tuple[int, int]:
        return self._position

    @position.setter
    def position(self, value: Tuple[int, int]) -> None:
        if self._position != value:
            self._position = value
            self._update_rect()

    @property
    def anchor(self) -> Anchor:
        return self._anchor

    @anchor.setter
    def anchor(self, value: Anchor) -> None:
        if self._anchor != value:
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
        mouse_position = self.game.input.mouse_position

        if self.rect.collidepoint(mouse_position[0], mouse_position[1]) or self._selected:
            objects = self._get_objects_in_point(mouse_position)
            if objects:
                top_object = max(objects, key=lambda obj: obj.z_index)
                if top_object != self:
                    self._mouse_leave_handler()
                    return
            self._mouse_enter_handler()
            self._mouse_moved_handler()
        else:
            self._mouse_leave_handler()

    def _get_objects_in_point(self, point: Tuple[int, int]) -> List["UIObject"]:
        objects = []
        if hasattr(self, "groups") and self.groups():
            for group in self.groups():
                for sprite in group.sprites():
                    if (isinstance(sprite, UIObject)) and sprite.active and sprite.rect.collidepoint(point):
                        objects.append(sprite)
        return objects

    def _update_image(self) -> None:
        self.image = pygame.Surface(self._size, pygame.SRCALPHA)
        self._update_rect()

    def _update_rect(self) -> None:
        self.rect = self.image.get_rect(**{self._anchor: self._position})

    def update(self, delta: float) -> None:
        if self._active:
            self._mouse_handler(delta)

    def draw(self, surface: pygame.Surface) -> None: ...

__all__ = ["UIObject"]

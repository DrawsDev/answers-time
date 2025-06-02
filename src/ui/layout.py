import pygame
from typing import Union, Iterable, List
from src.ui.base.ui_object import UIObject

class Layout:
    def __init__(self, enabled: bool = True):
        self._children = pygame.sprite.Group()
        self._enabled = enabled

    @property
    def enabled(self) -> bool:
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool) -> None:
        if self._enabled != value:
            self._enabled = value
            self._change_children_activity(value)

    @property
    def children(self) -> List[pygame.sprite.Sprite]:
        return self._children.sprites()

    def insert_child(self, *child: Union[UIObject, Iterable[UIObject]]) -> None:
        self._children.add(*child)
        self._change_children_activity(self._enabled)

    def remove_child(self, *child: Union[UIObject, Iterable[UIObject]]) -> None:
        self._children.remove(*child)
    
    def _change_children_activity(self, value: bool) -> None:
        for child in self._children:
            if hasattr(child, "active"):
                child.active = value

    def update(self, delta: float) -> None:
        self._children.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        if self._enabled:
            self._children.draw(surface)
            for child in self._children:
                child.draw(surface)

__all__ = ["Layout"]

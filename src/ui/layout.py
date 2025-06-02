import pygame
from typing import Union, Iterable, List

class Layout:
    def __init__(self, enabled: bool = True):
        self._group = pygame.sprite.Group()
        self._enabled = enabled

    @property
    def enabled(self) -> bool:
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value
        self._show() if value else self._hide()

    @property
    def children(self) -> List[pygame.sprite.Sprite]:
        return self._group.sprites()

    def add(self, *ui_objects: Union[pygame.sprite.Sprite, Iterable[pygame.sprite.Sprite]]) -> None:
        self._group.add(*ui_objects)
        self.enabled = self.enabled

    def remove(self, *ui_objects: Union[pygame.sprite.Sprite, Iterable[pygame.sprite.Sprite]]) -> None:
        self._group.remove(*ui_objects)

    def update(self, delta: float) -> None:
        self._group.update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        if self._enabled:
            self._group.draw(surface)
            for child in self._group:
                child.draw(surface)

    def _show(self) -> None:
        for ui_object in self._group.sprites():
            if hasattr(ui_object, "active"):
                if not ui_object.active: ui_object.active = True

    def _hide(self) -> None:
        for ui_object in self._group.sprites():
            if hasattr(ui_object, "active"):
                if ui_object.active: ui_object.active = False

__all__ = ["Layout"]

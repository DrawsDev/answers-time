from typing import Tuple

import pygame

from src.core.objects.resources import Resource


class BoxStyle(Resource):
    def __init__(self) -> None:
        super().__init__()
        self._margin_left = 0
        self._margin_right = 0
        self._margin_top = 0
        self._margin_bottom = 0
        self._corner_radius = 0

    @property
    def margin_left(self) -> float:
        return self._margin_left
    
    @margin_left.setter
    def margin_left(self, value: float) -> None:
        if value > -1:
            self._margin_left = value
            self._changed.emit()

    @property
    def margin_right(self) -> float:
        return self._margin_right
    
    @margin_right.setter
    def margin_right(self, value: float) -> None:
        if value > -1:
            self._margin_right = value
            self._changed.emit()

    @property
    def margin_top(self) -> float:
        return self._margin_top
    
    @margin_top.setter
    def margin_top(self, value: float) -> None:
        if value > -1:
            self._margin_top = value
            self._changed.emit()

    @property
    def margin_bottom(self) -> float:
        return self._margin_bottom
    
    @margin_bottom.setter
    def margin_bottom(self, value: float) -> None:
        if value > -1:
            self._margin_bottom = value
            self._changed.emit()

    @property
    def corner_radius(self) -> int:
        return self._corner_radius
    
    @corner_radius.setter
    def corner_radius(self, value: int) -> None:
        if value > -1:
            self._corner_radius = value
            self._changed.emit()

    def set_margin_all(self, offset: float) -> None:
        if offset > -1:
            self._margin_left = offset
            self._margin_right = offset
            self._margin_top = offset
            self._margin_bottom = offset
            self._changed.emit()

    def get_offset(self) -> Tuple[float, float]:
        return (self._margin_left, self._margin_top)

    def get_render(
        self, rect: pygame.FRect, color: pygame.Color = None
    ) -> pygame.Surface:
        width = rect.width + self._margin_left + self._margin_right
        height = rect.height + self._margin_top + self._margin_bottom
        size = (width, height)
        surface = pygame.Surface(size, pygame.SRCALPHA)

        if color:
            pygame.draw.rect(surface, color, surface.get_rect(), 0, self.corner_radius)

        return surface

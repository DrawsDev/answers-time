import pygame
from typing import Tuple, Union, Iterable
from src.enums import Anchor
from src.core.game import Game
from src.core.utility import lerp, clamp
from src.ui.base.ui_object import UIObject

class ScrollFrame(UIObject):
    def __init__(
        self, 
        game: Game,
        size: Tuple[int, int] = (100, 100),
        position: Tuple[int, int] = (0, 0),
        anchor: Anchor = Anchor.TopLeft
    ) -> None:
        super().__init__(game, size, position, anchor)
        self._enabled = False
        self._backcolor = "#000000"
        self._scroll_position = (0, 0)
        self._scroll_next_position = (0, 0)
        self._scroll_size = (0, 0)
        self._scroll_strength = 20.0
        self._scroll_horizontal_enabled = False
        self._scroll_vertical_enabled = True
        self._scrollbar_width = 10
        self._scrollbar_color1 = "#FFFFFF"
        self._scrollbar_color2 = "#4E4E56"
        self._dragging = False
        self._dragging_mouse_pos = None
        self._dragging_scroll_pos = None
        self._children = pygame.sprite.Group()

    @property
    def enabled(self) -> bool:
        return self._enabled
    
    @enabled.setter
    def enabled(self, value: bool) -> None:
        if self._enabled != value:
            self._enabled = value

    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, value: bool) -> None:
        if self._active != value:
            self._active = value
            self._change_children_activity(value)

    @property
    def backcolor(self) -> pygame.Color:
        return self._backcolor

    @backcolor.setter
    def backcolor(self, value: pygame.Color) -> None:
        if self._backcolor != value:
            self._backcolor = value

    @property
    def scroll_strength(self) -> float:
        return self._scroll_strength

    @scroll_strength.setter
    def scroll_strength(self, value: float) -> None:
        if self._scroll_strength != value:
            self._scroll_strength = value

    @property
    def scroll_horizontal_enabled(self) -> bool:
        return self._scroll_horizontal_enabled

    @scroll_horizontal_enabled.setter
    def scroll_horizontal_enabled(self, value: bool) -> None:
        if self._scroll_horizontal_enabled != value:
            self._scroll_horizontal_enabled = value

    @property
    def scroll_vertical_enabled(self) -> bool:
        return self._scroll_horizontal_enabled

    @scroll_vertical_enabled.setter
    def scroll_vertical_enabled(self, value: bool) -> None:
        if self.scroll_vertical_enabled != value:
            self.scroll_vertical_enabled = value    

    @property
    def scrollbar_width(self) -> int:
        return self._scrollbar_width

    @scrollbar_width.setter
    def scrollbar_width(self, value: int) -> None:
        if self._scrollbar_width != value and value > 0:
            self._scrollbar_width = value

    @property
    def scrollbar_color1(self) -> pygame.Color:
        return self._scrollbar_color1

    @scrollbar_color1.setter
    def scrollbar_color1(self, value: pygame.Color) -> None:
        if self._scrollbar_color1 != value:
            self._scrollbar_color1 = value    

    @property
    def scrollbar_color2(self) -> pygame.Color:
        return self._scrollbar_color2

    @scrollbar_color2.setter
    def scrollbar_color2(self, value: pygame.Color) -> None:
        if self._scrollbar_color2 != value:
            self._scrollbar_color2 = value    

    @property
    def children(self) -> Tuple[UIObject]:
        return tuple(self._children.sprites())

    def insert_child(self, *child: Union[UIObject, Iterable[UIObject]]) -> None:
        self._children.add(*child)
        self._change_children_activity(self._enabled)
        self._update_scroll_size()

    def remove_child(self, *child: Union[UIObject, Iterable[UIObject]]) -> None:
        self._children.remove(*child)
        self._update_scroll_size()

    def reset_scrolling(self) -> None:
        self._scroll_position = (0, 0)
        self._scroll_next_position = (0, 0)

    def draw(self, surface: pygame.Surface) -> None:
        self.image = pygame.Surface(self._size, pygame.SRCALPHA)
        self.image.fill(self._backcolor)
        self._draw_children(self.image)
        self._draw_vertical_scrollbar(self.image)

    def update(self, delta: float) -> None:
        super().update(delta)
        if self._enabled:
            self._update_scroll_position(delta)
            self._clamp_scroll_position()
            self._update_children(delta)

    def _change_children_activity(self, value: bool) -> None:
        for child in self._children.sprites():
            if hasattr(child, "active"):
                child.active = value

    def _update_children(self, delta: float) -> None:
        for child in self._children:
            child.rect = child.image.get_rect(**{child.anchor: (
                child.position[0] - self._scroll_position[0],
                child.position[1] - self._scroll_position[1]
            )})
            
            child_rect = child.image.get_rect(**{child.anchor: (
                child.position[0] - self.rect.x - self._scroll_position[0],
                child.position[1] - self.rect.y - self._scroll_position[1]
            )})

            if not child_rect.colliderect(pygame.Rect(0, 0, *self._size)):
                child.active = False
            elif self._active:
                child.active = True
        self._children.update(delta)

    def _update_scroll_size(self) -> None:
        max_x, max_y = 0, 0
        for child in self._children:
            max_x = max(max_x, child.rect.right - self.rect.x)
            max_y = max(max_y, child.rect.bottom - self.rect.y)
        self._scroll_size = (max_x, max_y + 5)
        self._clamp_scroll_position()

    def _update_scroll_position(self, delta: float) -> None:
        if self._scroll_position != self._scroll_next_position:
            self._scroll_position = (
                lerp(self._scroll_position[0], self._scroll_next_position[0], 0.3),
                lerp(self._scroll_position[1], self._scroll_next_position[1], 0.3)
            )

    def _clamp_scroll_position(self) -> None:
        max_x = max(0, self._scroll_size[0] - self.rect.width)
        max_y = max(0, self._scroll_size[1] - self.rect.height)
        self._scroll_next_position = (
            clamp(self._scroll_next_position[0], 0, max_x), 
            clamp(self._scroll_next_position[1], 0, max_y)
        )

    def _stop_dragging(self) -> None:
        if self._dragging:
            self._dragging = False
            self._dragging_mouse_pos = None
            self._dragging_scroll_pos = None

    def _dragging_handler(self) -> None:
        if not self._dragging_mouse_pos:
            self._dragging_mouse_pos = self.game.input.get_mouse_position()
            self._dragging_scroll_pos = self._scroll_position
        mouse_pos = self.game.input.get_mouse_position()
        difference = (
            self._dragging_mouse_pos[0] - mouse_pos[0],
            self._dragging_mouse_pos[1] - mouse_pos[1]
        )
        self._scroll_next_position = (
            (self._dragging_scroll_pos[0] + difference[0]) if self._scroll_horizontal_enabled else self._scroll_position[0],
            (self._dragging_scroll_pos[1] + difference[1]) if self._scroll_vertical_enabled else self._scroll_position[1]
        )

    def _mouse_wheel_handler(self, delta: float) -> None:
        wheel = self.game.input.get_mouse_wheel()
        direction = wheel.y * self._scroll_strength
        shift = self.game.input.is_key_down("left shift") or self.game.input.is_key_down("right shift")
        self._scroll_next_position = (
            (self._scroll_position[0] - direction) if self._scroll_horizontal_enabled and shift else self._scroll_position[0], 
            (self._scroll_position[1] - direction) if self._scroll_vertical_enabled and not shift else self._scroll_position[1]
        )
    
    def _mouse_handler(self, delta):
        super()._mouse_handler(delta)
        
        if self.game.input.is_key_released("m_left"):
            self._stop_dragging()
        
        if self._mouse_entered and self.game.input.is_key_pressed("m_left"):
            self._dragging = True 
        
        if self._mouse_entered and self.game.input.is_mouse_wheel():
            self._mouse_wheel_handler(delta)
        
        if self._dragging:
            self._dragging_handler()

    def _draw_children(self, surface: pygame.Surface) -> None:
        for child in self._children:
            child_rect = child.image.get_rect(**{child.anchor: (
                child.position[0] - self.rect.x - self._scroll_position[0],
                child.position[1] - self.rect.y - self._scroll_position[1]
            )})

            if child_rect.colliderect(pygame.Rect(0, 0, *self._size)):
                surface.blit(child.image, child_rect)

    def _draw_vertical_scrollbar(self, surface: pygame.Surface) -> None:
        if self._scroll_size[1] <= self.rect.height:
            return
        
        x = self.rect.width - self._scrollbar_width
        w = self._scrollbar_width
        h = max(30, (self.rect.height / self._scroll_size[1]) * self.rect.height)
        y = (self._scroll_position[1] / (self._scroll_size[1] - self.rect.height)) * (self.rect.height - h)

        pygame.draw.rect(surface, self._scrollbar_color2, (x, 0, w, self.rect.height))
        pygame.draw.rect(surface, self._scrollbar_color1, (x, y, w, h))

__all__ = ["ScrollFrame"]

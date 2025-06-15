import pygame
from typing import List, Tuple
from src.framework.utility import *
from src.framework.application import Application
from src.framework.scene.ui import *

class UINavigation:
    def __init__(self, app: Application):
        self.app = app
        self._enabled = False
        self._auto_enabling = True
        self._index = 0
        self._prev_index = 0
        self._uiobjects: List[Primitive] = []
        self._cursor_surface = None
        self._cursor_color = "White"
        self._cursor_thickness = 2

    @property
    def enabled(self) -> bool:
        return self._enabled
    
    @property
    def auto_enabling(self) -> bool:
        return self._auto_enabling

    @property
    def cursor_color(self) -> pygame.Color:
        return self._cursor_color

    @property
    def cursor_thickness(self) -> int:
        return self._cursor_thickness

    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value
        if len(self._uiobjects) > 0:
            self._uiobjects[self._index].selected = value
    
    @auto_enabling.setter
    def auto_enabling(self, value: bool) -> None:
        self._auto_enabling = value

    @cursor_color.setter
    def cursor_color(self, value: pygame.Color) -> None:
        self._cursor_color = value
        self._create_cursor_surface()

    @cursor_thickness.setter
    def cursor_thickness(self, value: int) -> None:
        self._cursor_thickness = clamp(value, 1, 8)
        self._create_cursor_surface()

    def _sort(self, layouts: Tuple[Layout]) -> None:
        uiobjects: List[Primitive] = []
        # Задействование только видимых групп
        for layout in layouts:
            if layout.enabled:
                uiobjects.extend(layout.children)
        # Задействование только выбираемых объектов
        uiobjects = [uiobject for uiobject in uiobjects if uiobject.selectable]
        # Сортировка объектов по Y и X
        self._uiobjects = sorted(uiobjects, key=lambda uiobject: (uiobject.position[1], uiobject.position[0]))

    def set_layout(self, *layouts: Layout) -> None:
        if len(self._uiobjects) > 0: 
            self._uiobjects[self._index].selected = False
        self._uiobjects.clear()
        self._index = 0
        self._prev_index = 0
        self._sort(layouts)
        self._create_cursor_surface()
        if len(self._uiobjects) > 0: 
            self._uiobjects[self._index].selected = True

    def update(self, delta: float) -> None:
        if self._enabled:
            self._input_handler()
        self._check_mouse_activity()

    def draw(self, surface: pygame.Surface) -> None:
        if self._enabled:
            uiobject = self._uiobjects[self._index]
            surface.blit(self._cursor_surface, self._cursor_surface.get_rect(**{uiobject.anchor: uiobject.position}))

    def _check_mouse_activity(self) -> None:
        if self.game.input.is_mouse_activity():
            self.enabled = False
        elif not self.enabled:
            self.enabled = self.game.input.is_key_pressed("tab")

    def _input_handler(self) -> None:
        count = len(self._uiobjects)
        
        if count > 0 and self.game.input.is_key_pressed("tab"):
            self._prev_index = self._index
            self._index += -1 if self.game.input.is_key_down("left shift") else 1
            if self._index > count - 1:
                self._index = 0
            if self._index < 0:
                self._index = count - 1
            self._create_cursor_surface()
            self._uiobjects[self._index].selected = True
            if count > 1: 
                self._uiobjects[self._prev_index].selected = False        

    def _create_cursor_surface(self) -> None:
        if len(self._uiobjects) <= 0:
            return
        uiobject = self._uiobjects[self._index]
        w, h = uiobject.image.get_size()
        self._cursor_surface = pygame.Surface((w, h), pygame.SRCALPHA)
        self._cursor_surface.fill(self._cursor_color, (0, 0, w, self._cursor_thickness))
        self._cursor_surface.fill(self._cursor_color, (w - self._cursor_thickness, 0, w - self._cursor_thickness, h))
        self._cursor_surface.fill(self._cursor_color, (0, h - self._cursor_thickness, w, h))
        self._cursor_surface.fill(self._cursor_color, (0, 0, self._cursor_thickness, h))

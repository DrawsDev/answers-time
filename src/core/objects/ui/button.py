from typing import Callable, Optional

import pygame
import pygame.freetype

from src.core.objects.ui.element_ui import ElementUI


class Button(ElementUI):
    def __init__(self) -> None:
        super().__init__()
        self._offset = pygame.Vector2()
        self._text = ""
        self._font = pygame.freetype.Font(None, 24)
        self._font_color = "white"
        self._hover_color = "#97AACD"
        self._normal_color = "#717F99"
        self._pressed_color = "#383F4C"
        self._held = False
        self._callback = None
        self._update_surface()
    
    @property
    def surface(self) -> pygame.Surface:
        return self._surface
    
    @property
    def offset(self) -> pygame.Vector2:
        return self._offset
    
    @offset.setter
    def offset(self, value: pygame.Vector2) -> None:
        self._offset = value
        self._update_rect()
    
    @property
    def text(self) -> str:
        return self._text
    
    @text.setter
    def text(self, value: str) -> None:
        self._text = value
        self._update_surface()

    @property
    def font_color(self) -> pygame.Color:
        return self._font_color
    
    @font_color.setter
    def font_color(self, value: pygame.Color):
        self._font_color = value
        self._update_surface()

    @property
    def font_filepath(self) -> str:
        return self._font.path
    
    @font_filepath.setter
    def font_filepath(self, value: str) -> None:
        self._font = pygame.freetype.Font(value, self._font.size)
        self._update_surface()
    
    @property
    def font_size(self) -> int:
        return self._font.size
    
    @font_size.setter
    def font_size(self, value: int) -> None:
        if value > 0:
            self._font.size = value
            self._update_surface()

    @property
    def callback(self) -> Optional[Callable]:
        return self._callback
    
    @callback.setter
    def callback(self, value: Optional[Callable]) -> None:
        if self._callback != value:
            self._callback = value
 
    def _update_rect(self) -> None:
        position = self._position + self._offset
        self._rect = self._surface.get_frect(**{self._anchor: position})

    def _update_surface(self) -> None:
        text_surface, _ = self._font.render(self._text, self._font_color)
        button_surface = pygame.Surface(text_surface.size)

        if self._hovered and not self._held:
            button_surface.fill(self._hover_color)
        elif self._hovered and self._held:
            button_surface.fill(self._pressed_color)
        else:
            button_surface.fill(self._normal_color)
        
        button_surface.blit(text_surface)

        self._surface = button_surface
        self._update_rect()

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self._surface, self._rect)

    def event(self, event: pygame.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self._rect.collidepoint(event.pos):
                self._held = True
                self._update_surface()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self._rect.collidepoint(event.pos):
                if self._held:
                    if self._callback:
                        self._callback()
                    self._held = False
                    self._update_surface()
            elif self._held:
                self._held = False
                self._update_surface()
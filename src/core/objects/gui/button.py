from typing import Callable, Optional

import pygame

from src.core.objects.gui import Element
from src.core.objects.resources import ButtonTheme


class Button(Element):
    def __init__(self) -> None:
        super().__init__()
        self._offset = pygame.Vector2()
        self._text = ""
        self._theme = ButtonTheme()
        self._held = False
        self._callback = None
        self._theme.changed.connect(self._update_surface)
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
    def theme(self) -> ButtonTheme:
        return self._theme
    
    @theme.setter
    def theme(self, value: ButtonTheme) -> None:
        if self._theme != value:
            self._theme.changed.disconnect(self._update_surface)
            self._theme = value
            self._theme.changed.connect(self._update_surface)
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
        if self._hovered and not self._held:
            box_color = self.theme.box_hover_color
        elif self._hovered and self._held:
            box_color = self.theme.box_pressed_color
        else:
            box_color = self.theme.box_normal_color
        
        text_surface = self.theme.font.get_render(self._text, self.theme.font_color)

        self._surface = self.theme.box_style.get_render(text_surface.get_frect(), box_color)
        self._surface.blit(text_surface, self.theme.box_style.get_offset())

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

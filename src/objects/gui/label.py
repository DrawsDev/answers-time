import pygame

from src.objects.gui import Element
from src.objects.resources import LabelTheme


class Label(Element):
    def __init__(self) -> None:
        super().__init__()
        self._offset = pygame.Vector2()
        self._text = ""
        self._theme = LabelTheme()
        self._theme.changed.connect(self._update_surface)
        self._update_surface()

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
    def theme(self) -> LabelTheme:
        return self._theme
    
    def _update_surface(self) -> None:
        text_surface = self.theme.font.get_render(self.text, self.theme.font_color)

        self._surface = self.theme.box_style.get_render(text_surface.get_frect(), self.theme.box_normal_color)
        self._surface.blit(text_surface, self.theme.box_style.get_offset())

        self._update_rect()

    def _update_rect(self) -> None:
        position = self._position + self._offset
        self._rect = self._surface.get_frect(**{self._anchor: position})

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self._surface, self._rect)

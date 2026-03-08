from typing import Optional

import pygame

from src.core.objects.resources import Resource, Font, BoxStyle


class LabelTheme(Resource):
    def __init__(self) -> None:
        super().__init__()

        self._font: Font = Font()
        self._font_color: pygame.Color = pygame.Color("#FFFFFF")

        self._box_style: BoxStyle = BoxStyle()
        self._box_normal_color: Optional[pygame.Color] = None

        self._font.changed.connect(self.changed.emit)
        self._box_style.changed.connect(self.changed.emit)

    @property
    def font(self) -> Font:
        return self._font
    
    @property
    def font_color(self) -> pygame.Color:
        return self._font_color

    @font_color.setter
    def font_color(self, value: pygame.Color) -> None:
        if self._font_color != value:
            self._font_color = value
            self._changed.emit()

    @property
    def box_style(self) -> BoxStyle:
        return self._box_style

    @property
    def box_normal_color(self) -> Optional[pygame.Color]:
        return self._box_normal_color
    
    @box_normal_color.setter
    def box_normal_color(self, value: Optional[pygame.Color]):
        if self._box_normal_color != value:
            self._box_normal_color = value
            self._changed.emit()

    def free(self):
        super().free()
        self._font.free()
        self._box_style.free()
        self._font = None
        self._box_style = None


class ButtonTheme(Resource):
    def __init__(self) -> None:
        super().__init__()

        self._font: Font = Font()
        self._font_color: pygame.Color = pygame.Color("#FFFFFF")
        
        self._box_style: BoxStyle = BoxStyle()
        self._box_hover_color: pygame.Color = pygame.Color("#97AACD")
        self._box_normal_color: pygame.Color = pygame.Color("#717F99")
        self._box_pressed_color: pygame.Color = pygame.Color("#383F4C")

        self._box_style.set_margin_all(10)

        self._font.changed.connect(self.changed.emit)
        self._box_style.changed.connect(self.changed.emit)

    @property
    def font(self) -> Font:
        return self._font
    
    @property
    def font_color(self) -> pygame.Color:
        return self._font_color

    @font_color.setter
    def font_color(self, value: pygame.Color) -> None:
        if self._font_color != value:
            self._font_color = value
            self._changed.emit()

    @property
    def box_style(self) -> BoxStyle:
        return self._box_style

    @property
    def box_hover_color(self) -> Optional[pygame.Color]:
        return self._box_hover_color

    @box_hover_color.setter
    def box_hover_color(self, value: Optional[pygame.Color]):
        if self._box_hover_color != value:
            self._box_hover_color = value
            self._changed.emit()

    @property
    def box_normal_color(self) -> Optional[pygame.Color]:
        return self._box_normal_color

    @box_normal_color.setter
    def box_normal_color(self, value: Optional[pygame.Color]):
        if self._box_normal_color != value:
            self._box_normal_color = value
            self._changed.emit()

    @property
    def box_pressed_color(self) -> Optional[pygame.Color]:
        return self._box_pressed_color

    @box_pressed_color.setter
    def box_pressed_color(self, value: Optional[pygame.Color]):
        if self._box_pressed_color != value:
            self._box_pressed_color = value
            self._changed.emit()

    def free(self):
        super().free()
        self._font.free()
        self._box_style.free()
        self._font = None
        self._box_style = None


class Theme(Resource):
    def __init__(self) -> None:
        super().__init__()
        self._label = LabelTheme()
        self._button = ButtonTheme()
        self._label.changed.connect(self.changed.emit)
        self._button.changed.connect(self.changed.emit)

    @property
    def label(self) -> LabelTheme:
        return self._label
    
    @property
    def button(self) -> ButtonTheme:
        return self._button

    def free(self):
        super().free()
        self._label.free()
        self._button.free()
        self._label = None
        self._button = None

import time
import pygame
from typing import Tuple, Optional
from src.framework.enums import *
from src.framework.application import Application
from src.framework.textinput import TextInput
from src.framework.callback import *
from src.framework.scene.ui import *

class TextBox(Primitive):
    def __init__(
        self, 
        app: Application, 
        text: str = "",
        placeholder: str = "Placeholder",
        size: Tuple[int, int] = (200, 40), 
        position: Tuple[int, int] = (0, 0), 
        anchor: Anchor = Anchor.TopLeft,
        font_path: Optional[str] = None,
        font_size: int = 20,
        font_align: Align = Align.Left,
        text_color: pygame.Color = "#000000",
        placeholder_color: pygame.Color = "#A0A0A0",
        maxlength: int = 64,
        line_length: int = 0,
        backcolor_focus: pygame.Color = "#FFFFFF",
        backcolor_unfocus: pygame.Color = "#FFFFFF",
        border_color: pygame.Color = "#FFFFFF",
        border_width: int = 0,
        border_radius: int = -1,
        cursor_color: pygame.Color = "#000000",
        cursor_selection_color: pygame.Color = "#A3A3A3",
        z_index: int = 0
    ) -> None:
        super().__init__(app, size, position, anchor, z_index)
        self._selectable = True
        self._dragging = False
        self._focus = False
        self._focus_lost_callback = Callback()
        
        self._textinput = TextInput(app, text, placeholder, maxlength, line_length)
        self._textinput.enabled = True
        
        self._font = pygame.Font(font_path, font_size)
        self._font_path = font_path
        self._font.align = font_align
        self._text_color = text_color
        self._placeholder_color = placeholder_color
        self._text_rect = pygame.Rect()
        
        self._cursor_color = cursor_color
        self._cursor_selection_color = cursor_selection_color
        self._cursor_visibled = True
        self._cursor_blink_interval = 0.5
        self._cursor_previous_blink_time = 0
        self._cursor_click_count = 0
        self._cursor_previous_click_time = 0
        self._cursor_double_click_threshold = 300
        
        self._backcolor_focus = backcolor_focus
        self._backcolor_unfocus = backcolor_unfocus

        self._border_color = border_color
        self._border_width = border_width
        self._border_radius = border_radius
        
        self._update_image()

    @property
    def text(self) -> str:
        return self._textinput.text
    
    @text.setter
    def text(self, value: str) -> None:
        if self._textinput.text != value and len(value) <= self._textinput.maxlength:
            self._textinput.text = value
            self._update_image()

    @property
    def placeholder(self) -> str:
        return self._textinput.placeholder
    
    @placeholder.setter
    def placeholder(self, value: str) -> None:
        self._textinput.placeholder = value
        self._update_image()    

    @property
    def text_color(self) -> pygame.Color:
        return self._text_color
    
    @text_color.setter
    def text_color(self, value: pygame.Color) -> None:
        if self._text_color != value:
            self._text_color = value
            self._update_image()

    @property
    def focus_lost_callback(self) -> Callback:
        return self._focus_lost_callback

    @property
    def textinput_enabled(self) -> bool:
        return self._textinput.enabled
    
    @textinput_enabled.setter
    def textinput_enabled(self, value: bool) -> None:
        self._textinput.enabled = value

    @property
    def backcolor_focus(self) -> pygame.Color:
        return self._backcolor_focus
    
    @backcolor_focus.setter
    def backcolor_focus(self, value: pygame.Color) -> None:
        self._backcolor_focus = value
        self._update_image()

    @property
    def backcolor_unfocus(self) -> pygame.Color:
        return self._backcolor_unfocus
    
    @backcolor_unfocus.setter
    def backcolor_unfocus(self, value: pygame.Color) -> None:
        self._backcolor_unfocus = value
        self._update_image()

    def _get_cursor_position_from_mouse(self) -> int:
        mouse_x, _ = self.app.input.get_mouse_position()
        text = self.text
        relative_x = mouse_x - self.rect.x - self._text_rect.x

        if not text:
            return 0

        for i in range(len(text) + 1):
            text_width = self._font.size(text[:i])[0]
            if relative_x <= text_width:
                previous_width = self._font.size(text[:i-1])[0] if i > 0 else 0
                if relative_x - previous_width < text_width - relative_x:
                    return i - 1 if i > 0 else 0
                return i
        return len(text)

    def _reset_cursor_blink(self) -> None:
        self._cursor_visibled = True
        self._cursor_previous_blink_time = time.time() + self._cursor_blink_interval

    def _mouse_pressed_handler(self) -> None:
        self._dragging = True
        cursor_pos = self._get_cursor_position_from_mouse()
        self._textinput.cursor_position = cursor_pos
        self._textinput.selection_start_position = cursor_pos
        self._reset_cursor_blink()

    def _mouse_released_handler(self) -> None:
        if self._dragging:
            self._focus = True
            self._dragging = False

            current_time = pygame.time.get_ticks()
            if current_time - self._cursor_previous_click_time < self._cursor_double_click_threshold:
                self._cursor_click_count += 1
            else:
                self._cursor_click_count = 1
            
            self._cursor_previous_click_time = current_time

            if not self.text:
                return
            
            if self._cursor_click_count == 2:
                cursor_pos = self._get_cursor_position_from_mouse()
                
                left = cursor_pos
                while left > 0 and self._textinput._text[left-1].isalnum():
                    left -= 1
                
                right = cursor_pos
                while right < len(self._textinput._text) and self._textinput._text[right].isalnum():
                    right += 1
                
                self._textinput.selection_start_position = left
                self._textinput.cursor_position = right                   
            elif self._cursor_click_count == 3:
                self._textinput.select_all()
            
            self._update_image()

    def _mouse_motion_handler(self) -> None:
        if self._dragging:
            if not self._focus:
                self._focus = True
            cursor_pos = self._get_cursor_position_from_mouse()
            self._textinput.cursor_position = cursor_pos
            self._update_image()

    def _mouse_handler(self, delta) -> None:
        super()._mouse_handler(delta)

        if self.app.input.is_mouse_moved():
            self._mouse_motion_handler()

        if self._mouse_entered:
            if self.app.input.is_key_pressed("m_left"):
                self._mouse_pressed_handler()
            if self.app.input.is_key_released("m_left"):
                self._mouse_released_handler()
        else:
            if self._dragging and self.app.input.is_key_released("m_left"):
                self._dragging = False
            if self.app.input.is_key_pressed("m_left"):
                if self._focus:
                    self._focus = False
                    self._focus_lost_callback(self.text)
                    self._update_image()

    def _draw_selection_range(self) -> None:
        if self._focus and self._textinput.has_selection():
            start, end = self._textinput.get_selection_range()
            self.image.fill(self._cursor_selection_color, (
                self._text_rect.x + self._font.size(self._textinput.text[:start])[0],
                self._text_rect.y,
                self._font.size(self._textinput.text[start:end])[0],
                self._font.get_linesize()
            ))

    def _draw_text(self) -> None:
        if self.text == "":
            text_surface = self._font.render(self.placeholder, True, self._placeholder_color)
        else:
            text_surface = self._font.render(self.text, True, self._text_color)
        self._text_rect = text_surface.get_rect(midleft=(5, self.image.get_height() / 2))
        self.image.blit(text_surface, self._text_rect)

    def _draw_cursor(self) -> None:
        if self._focus and self._cursor_visibled:
            self.image.fill(self._cursor_color, (
                self._text_rect.x + self._font.size(self._textinput.text[:self._textinput.cursor_position])[0], 
                self._text_rect.y,
                1,
                self._font.get_linesize()
            ))

    def _update_image(self):
        color = self.backcolor_focus if self._focus else self.backcolor_unfocus
        pygame.draw.rect(self.image, color, ((0, 0), self.rect.size), 0, 6)

        if self._border_width > 0:
            pygame.draw.rect(self.image, self._border_color, ((0, 0), self.rect.size), self._border_width, self._border_radius)

        self._draw_selection_range()
        self._draw_text()
        self._draw_cursor()

    def _update_cursor_blink(self) -> None:
        current_time = time.time()
        if current_time - self._cursor_previous_blink_time > self._cursor_blink_interval:
            self._cursor_visibled = not self._cursor_visibled
            self._cursor_previous_blink_time = current_time
            self._update_image()

    def _update_input_box(self) -> None:
        if self._focus:
            self._textinput.update()
        if self._textinput.changed:
            self._reset_cursor_blink()
            self._update_image()        

    def update(self, delta: float) -> None:
        super().update(delta)
        self._update_input_box()
        self._update_cursor_blink()

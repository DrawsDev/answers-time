import time
import pygame
from typing import Tuple, Optional
from src.enums import Anchor, Align
from src.core.game import Game
from src.core.callback import *
from src.experimental.input_box import InputBox
from src.ui.base.ui_object import UIObject

class TextBox(UIObject):
    def __init__(
        self, 
        game: Game, 
        text: str = "",
        placeholder: str = "Placeholder",
        size: Tuple[int, int] = (200, 100),  # Increased default height for multiline
        position: Tuple[int, int] = (0, 0), 
        anchor: Anchor = Anchor.TopLeft,
        z_index: int = 0,
        font_path: Optional[str] = None,
        font_size: int = 20,
        font_align: Align = Align.Left,
        text_color: pygame.Color = "white",
        line_spacing: int = 5,
        padding: Tuple[int, int] = (5, 5)
    ) -> None:
        super().__init__(game, size, position, anchor, z_index)
        self._selectable = True
        self._dragging = False
        self._focus = False
        self._focus_lost_callback = Callback()
        self._input_box = InputBox(game, text, placeholder, multiline=True)
        self._input_box.enabled = True
        self._font = pygame.Font(font_path, font_size)
        self._font_path = font_path
        self._font.align = font_align
        self._text_color = text_color
        self._line_spacing = line_spacing
        self._padding = padding
        self._cursor_color = "white"
        self._cursor_selection_color = [0, 0, 255, 100]
        self._cursor_visibled = True
        self._cursor_visible_time = 0.5
        self._cursor_invisible_time = 0.75
        self._cursor_previous_time = 0
        self._cursor_click_count = 0
        self._cursor_previous_click_time = 0
        self._scroll_offset = 0
        self._update_image()
    
    @property
    def text(self) -> str:
        return self._input_box.text
    
    @text.setter
    def text(self, value: str) -> None:
        if self._input_box.text != value:
            self._input_box.text = value
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
    def line_spacing(self) -> int:
        return self._line_spacing
    
    @line_spacing.setter
    def line_spacing(self, value: int) -> None:
        if self._line_spacing != value:
            self._line_spacing = value
            self._update_image()
    
    @property
    def padding(self) -> Tuple[int, int]:
        return self._padding
    
    @padding.setter
    def padding(self, value: Tuple[int, int]) -> None:
        if self._padding != value:
            self._padding = value
            self._update_image()
    
    @property
    def focus_lost_callback(self) -> Callback:
        return self._focus_lost_callback
        
    def _get_cursor_position_from_mouse(self) -> Tuple[int, int]:
        mouse_x, mouse_y = self.game.input.get_mouse_position()
        rel_x = mouse_x - self.rect.x - self._padding[0]
        rel_y = mouse_y - self.rect.y - self._padding[1] + self._scroll_offset
        
        line_height = self._font.get_linesize() + self._line_spacing
        line_index = max(0, min(len(self._input_box.lines)-1, rel_y // line_height))
        
        line = self._input_box.lines[line_index]
        x_pos = rel_x
        
        # Find character position in line
        char_pos = 0
        min_dist = float('inf')
        best_pos = 0
        
        for i in range(len(line)+1):
            text_width = self._font.size(line[:i])[0]
            dist = abs(x_pos - text_width)
            if dist < min_dist:
                min_dist = dist
                best_pos = i
        
        return (line_index, best_pos)
    
    def _reset_cursor_visibility(self) -> None:
        self._cursor_visibled = True
        self._cursor_previous_time = time.time()        
    
    def _mouse_pressed_handler(self) -> None:
        self._dragging = True
        cursor_pos = self._get_cursor_position_from_mouse()
        self._input_box.cursor_position = cursor_pos
        self._input_box.selection_start_position = cursor_pos
        self._reset_cursor_visibility()
    
    def _mouse_released_handler(self) -> None:
        if self._dragging:
            self._focus = True
            self._dragging = False
            
            current_time = pygame.time.get_ticks()
            if current_time - self._cursor_previous_click_time < 300:
                self._cursor_click_count += 1
            else:
                self._cursor_click_count = 1
            self._cursor_previous_click_time = current_time
            
            if self._cursor_click_count == 2:
                line, pos = self._get_cursor_position_from_mouse()
                current_line = self._input_box.lines[line]
                
                if current_line:
                    left = pos
                    while left > 0 and current_line[left-1].isalnum():
                        left -= 1
                    right = pos
                    while right < len(current_line) and current_line[right].isalnum():
                        right += 1
                    
                    self._input_box.selection_start_position = (line, left)
                    self._input_box.cursor_position = (line, right)                   
            elif self._cursor_click_count == 3:
                line, _ = self._get_cursor_position_from_mouse()
                self._input_box.selection_start_position = (line, 0)
                self._input_box.cursor_position = (line, len(self._input_box.lines[line]))
            else:
                self._cursor_click_count = 1
            
            self._update_image()
    
    def _mouse_motion_handler(self) -> None:
        if self._dragging:
            if not self._focus:
                self._focus = True
            cursor_pos = self._get_cursor_position_from_mouse()
            self._input_box.cursor_position = cursor_pos        
            self._reset_cursor_visibility()
            self._update_image()
    
    def _mouse_handler(self, delta) -> None:
        super()._mouse_handler(delta)

        if self.game.input.is_mouse_moved():
            self._mouse_motion_handler()

        if self._mouse_entered:
            if self.game.input.is_key_pressed("m_left") or self._selected and self.game.input.is_key_pressed("return"):
                self._mouse_pressed_handler()
            if self.game.input.is_key_released("m_left") or self._selected and self.game.input.is_key_released("return"):
                self._mouse_released_handler()
        else:
            if self._dragging and (self.game.input.is_key_released("m_left") or self.game.input.is_key_released("return")):
                self._dragging = False
            if self.game.input.is_key_pressed("m_left") or self._selected and self.game.input.is_key_pressed("return"):
                if self._focus:
                    self._focus = False
                    self._focus_lost_callback()
                    self._update_image()
    
    def _draw_selection_range(self) -> None:
        if self._focus and self._input_box.has_selection():
            (start_line, start_pos), (end_line, end_pos) = self._input_box.get_selection_range()
            line_height = self._font.get_linesize() + self._line_spacing
            
            if start_line == end_line:
                # Single line selection
                line = self._input_box.lines[start_line]
                selected_text = line[start_pos:end_pos]
                text_width = self._font.size(line[:start_pos])[0]
                
                y_pos = start_line * line_height - self._scroll_offset
                if 0 <= y_pos <= self.rect.height - line_height:
                    self.image.fill(
                        self._cursor_selection_color,
                        (
                            self._padding[0] + text_width,
                            self._padding[1] + y_pos,
                            self._font.size(selected_text)[0],
                            line_height - self._line_spacing
                        )
                    )
            else:
                # Multi-line selection
                for line_num in range(start_line, end_line + 1):
                    if line_num >= len(self._input_box.lines):
                        continue
                        
                    line = self._input_box.lines[line_num]
                    y_pos = line_num * line_height - self._scroll_offset
                    
                    if line_num == start_line:
                        # First line
                        selected_text = line[start_pos:]
                        text_width = self._font.size(line[:start_pos])[0]
                        self.image.fill(
                            self._cursor_selection_color,
                            (
                                self._padding[0] + text_width,
                                self._padding[1] + y_pos,
                                self._font.size(selected_text)[0],
                                line_height - self._line_spacing
                            )
                        )
                    elif line_num == end_line:
                        # Last line
                        selected_text = line[:end_pos]
                        self.image.fill(
                            self._cursor_selection_color,
                            (
                                self._padding[0],
                                self._padding[1] + y_pos,
                                self._font.size(selected_text)[0],
                                line_height - self._line_spacing
                            )
                        )
                    else:
                        # Middle lines (fully selected)
                        self.image.fill(
                            self._cursor_selection_color,
                            (
                                self._padding[0],
                                self._padding[1] + y_pos,
                                self._font.size(line)[0],
                                line_height - self._line_spacing
                            )
                        )
    
    def _draw_text(self) -> None:
        line_height = self._font.get_linesize() + self._line_spacing
        visible_lines = (self.rect.height - 2 * self._padding[1]) // line_height + 1
        
        for i, line in enumerate(self._input_box.lines):
            y_pos = i * line_height - self._scroll_offset
            if -line_height <= y_pos <= self.rect.height:
                if line or i == 0:
                    text_surface = self._font.render(line, True, self._text_color)
                    self.image.blit(text_surface, (self._padding[0], self._padding[1] + y_pos))
        
        # Draw placeholder if text is empty
        if not any(line for line in self._input_box.lines):
            text_surface = self._font.render(self._input_box.placeholder, True, self._text_color)
            text_surface.set_alpha(150)
            self.image.blit(text_surface, (self._padding[0], self._padding[1]))
    
    def _draw_cursor(self) -> None:
        if self._focus and self._cursor_visibled:
            line, pos = self._input_box.cursor_position
            if line >= len(self._input_box.lines):
                return
                
            line_text = self._input_box.lines[line]
            cursor_x = self._font.size(line_text[:pos])[0]
            line_height = self._font.get_linesize() + self._line_spacing
            cursor_y = line * line_height - self._scroll_offset
            
            if 0 <= cursor_y <= self.rect.height - line_height:
                self.image.fill(
                    self._cursor_color,
                    (
                        self._padding[0] + cursor_x,
                        self._padding[1] + cursor_y,
                        1,
                        line_height - self._line_spacing
                    )
                )
    
    def _update_scroll(self) -> None:
        line_height = self._font.get_linesize() + self._line_spacing
        total_height = len(self._input_box.lines) * line_height
        visible_height = self.rect.height - 2 * self._padding[1]
        
        if total_height > visible_height:
            line, pos = self._input_box.cursor_position
            cursor_y = line * line_height
            cursor_bottom = cursor_y + line_height
            
            # Adjust scroll to keep cursor visible
            if cursor_y < self._scroll_offset:
                self._scroll_offset = max(0, cursor_y)
            elif cursor_bottom > self._scroll_offset + visible_height:
                self._scroll_offset = min(
                    total_height - visible_height, 
                    cursor_bottom - visible_height
                )
        else:
            self._scroll_offset = 0
    
    def _update_image(self):
        self.image.fill("darkgray")
        self._update_scroll()
        self._draw_selection_range()
        self._draw_text()
        self._draw_cursor()
    
    def _update_cursor_visibility(self) -> None:
        current_time = time.time()
        if self._cursor_visibled:
            if current_time - self._cursor_previous_time > self._cursor_visible_time:
                self._cursor_previous_time = current_time
                self._cursor_visibled = False
                self._update_image()
        else:
            if current_time - self._cursor_previous_time > self._cursor_invisible_time:
                self._cursor_previous_time = current_time
                self._cursor_visibled = True
                self._update_image()
    
    def _update_input_box(self) -> None:
        if self._focus:
            self._input_box.update()
        if self._input_box.changed:
            self._reset_cursor_visibility()
            self._update_image()        
    
    def update(self, delta):
        super().update(delta)
        self._update_input_box()
        self._update_cursor_visibility()
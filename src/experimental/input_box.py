import pygame.scrap
from typing import Tuple, Optional, List
from src.core.game import Game

class InputBox:
    def __init__(
        self,
        game: Game,
        text: str = "",
        placeholder: str = "Placeholder",
        maxlength: int = 1024,
        multiline: bool = True
    ) -> None:
        self.game = game
        self._text = text
        self._placeholder = placeholder
        self._maxlength = maxlength
        self._cursor = (0, 0)  # (line, pos_in_line)
        self._selection_start = None
        self._enabled = False
        self._changed = False
        self._multiline = multiline
        self._lines = self._split_text_to_lines(text)
    
    @property
    def text(self) -> str:
        return "\n".join(self._lines)
    
    @text.setter
    def text(self, value: str) -> None:
        if self._text != value and len(value) <= self._maxlength:
            self._text = value
            self._lines = self._split_text_to_lines(value)
            self._changed = True
    
    @property
    def lines(self) -> List[str]:
        return self._lines.copy()
    
    def _split_text_to_lines(self, text: str) -> List[str]:
        return text.split("\n") if text else [""]
    
    def _join_lines_to_text(self, lines: List[str]) -> str:
        return "\n".join(lines)
    
    @property
    def placeholder(self) -> str:
        return self._placeholder
    
    @placeholder.setter
    def placeholder(self, value: str) -> None:
        if self._placeholder != value and len(value) <= self._maxlength:
            self._placeholder = value
            self._changed = True
    
    @property
    def maxlength(self) -> int:
        return self._maxlength
    
    @maxlength.setter
    def maxlength(self, value: int) -> None:
        if self._maxlength != value and value >= 0:
            self._maxlength = value
            self._changed = True
    
    @property
    def enabled(self) -> bool:
        return self._enabled
    
    @enabled.setter
    def enabled(self, value: bool) -> None:
        if value != self._enabled:
            self._enabled = value
            self._changed = True
    
    @property
    def cursor_position(self) -> Tuple[int, int]:
        return self._cursor
    
    @cursor_position.setter
    def cursor_position(self, value: Tuple[int, int]) -> None:
        line, pos = value
        if (self._cursor != value and 
            0 <= line < len(self._lines) and 
            0 <= pos <= len(self._lines[line])):
            self._cursor = value
            self._changed = True
    
    @property
    def selection_start_position(self) -> Optional[Tuple[int, int]]:
        return self._selection_start
    
    @selection_start_position.setter
    def selection_start_position(self, value: Optional[Tuple[int, int]]) -> None:
        if value is not None:
            line, pos = value
            if not (0 <= line < len(self._lines) and 0 <= pos <= len(self._lines[line])):
                return
        if self._selection_start != value:
            self._selection_start = value
            self._changed = True
    
    @property
    def changed(self) -> bool:
        if self._changed:
            self._changed = False
            return True
        return False
    
    @property
    def multiline(self) -> bool:
        return self._multiline
    
    @multiline.setter
    def multiline(self, value: bool) -> None:
        if self._multiline != value:
            self._multiline = value
            self._changed = True
    
    def has_selection(self) -> bool:
        return (self._selection_start is not None and 
                self._selection_start != self._cursor)
    
    def get_selection_range(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        if self._selection_start is None:
            return (self._cursor, self._cursor)
        
        start_line, start_pos = self._selection_start
        end_line, end_pos = self._cursor
        
        if (start_line > end_line or 
            (start_line == end_line and start_pos > end_pos)):
            return ((end_line, end_pos), (start_line, start_pos))
        return ((start_line, start_pos), (end_line, end_pos))
    
    def delete_selected_text(self) -> None:
        if self.has_selection():
            (start_line, start_pos), (end_line, end_pos) = self.get_selection_range()
            
            if start_line == end_line:
                # Selection within single line
                line = self._lines[start_line]
                self._lines[start_line] = line[:start_pos] + line[end_pos:]
            else:
                # Multi-line selection
                first_part = self._lines[start_line][:start_pos]
                last_part = self._lines[end_line][end_pos:]
                self._lines[start_line] = first_part + last_part
                del self._lines[start_line+1:end_line+1]
            
            self._cursor = (start_line, start_pos)
            self._selection_start = None
            self._text = self._join_lines_to_text(self._lines)
            self._changed = True
    
    def backspace(self) -> None:
        if self.has_selection():
            self.delete_selected_text()
        else:
            line, pos = self._cursor
            if pos > 0:
                # Delete character in current line
                self._lines[line] = self._lines[line][:pos-1] + self._lines[line][pos:]
                self._cursor = (line, pos-1)
                self._changed = True
            elif line > 0:
                # Merge with previous line
                prev_line_len = len(self._lines[line-1])
                self._lines[line-1] += self._lines[line]
                del self._lines[line]
                self._cursor = (line-1, prev_line_len)
                self._text = self._join_lines_to_text(self._lines)
                self._changed = True
    
    def delete(self) -> None:
        if self.has_selection():
            self.delete_selected_text()
        else:
            line, pos = self._cursor
            current_line = self._lines[line]
            
            if pos < len(current_line):
                # Delete character after cursor
                self._lines[line] = current_line[:pos] + current_line[pos+1:]
                self._changed = True
            elif line < len(self._lines) - 1:
                # Merge with next line
                self._lines[line] += self._lines[line+1]
                del self._lines[line+1]
                self._text = self._join_lines_to_text(self._lines)
                self._changed = True
    
    def insert_text(self, text: str) -> None:
        if not text:
            return
            
        if len(self._text) + len(text) > self._maxlength:
            return
            
        self.delete_selected_text()
        
        lines_to_insert = text.split("\n")
        line, pos = self._cursor
        current_line = self._lines[line]
        
        if len(lines_to_insert) == 1:
            # Single line insertion
            self._lines[line] = current_line[:pos] + lines_to_insert[0] + current_line[pos:]
            self._cursor = (line, pos + len(lines_to_insert[0]))
        else:
            # Multi-line insertion
            first_part = current_line[:pos]
            last_part = current_line[pos:]
            
            # Modify first line
            self._lines[line] = first_part + lines_to_insert[0]
            
            # Insert middle lines
            for i in range(1, len(lines_to_insert)-1):
                self._lines.insert(line+i, lines_to_insert[i])
            
            # Insert last line with remaining text
            last_line = lines_to_insert[-1] + last_part
            self._lines.insert(line + len(lines_to_insert)-1, last_line)
            
            # Update cursor position
            self._cursor = (line + len(lines_to_insert)-1, len(lines_to_insert[-1]))
        
        self._text = self._join_lines_to_text(self._lines)
        self._changed = True
    
    def copy(self) -> None:
        if self.has_selection():
            (start_line, start_pos), (end_line, end_pos) = self.get_selection_range()
            
            if start_line == end_line:
                selected_text = self._lines[start_line][start_pos:end_pos]
            else:
                selected_text = []
                selected_text.append(self._lines[start_line][start_pos:])
                for line in range(start_line+1, end_line):
                    selected_text.append(self._lines[line])
                selected_text.append(self._lines[end_line][:end_pos])
                selected_text = "\n".join(selected_text)
            
            pygame.scrap.put_text(selected_text)
    
    def paste(self) -> None:
        clipboard_text = pygame.scrap.get_text()
        if clipboard_text:
            self.insert_text(clipboard_text)
    
    def cut(self) -> None:
        if self.has_selection():
            self.copy()
            self.delete_selected_text()
    
    def select_all(self) -> None:
        if self._lines:
            self._cursor = (len(self._lines)-1, len(self._lines[-1]))
            self._selection_start = (0, 0)
            self._changed = True
    
    def move_cursor(self, direction: Tuple[int, int], shift: bool) -> None:
        line, pos = self._cursor
        new_line, new_pos = line, pos
        
        # Handle vertical movement
        if direction[1] != 0:
            new_line = max(0, min(len(self._lines)-1, line + direction[1]))
            # Try to maintain similar horizontal position
            if new_line != line:
                new_pos = min(len(self._lines[new_line]), pos)
        
        # Handle horizontal movement
        if direction[0] != 0:
            if new_pos + direction[0] >= 0:
                if new_pos + direction[0] <= len(self._lines[new_line]):
                    new_pos += direction[0]
                elif self._multiline and new_line < len(self._lines)-1:
                    # Move to start of next line
                    new_line += 1
                    new_pos = 0
            elif new_line > 0 and self._multiline:
                # Move to end of previous line
                new_line -= 1
                new_pos = len(self._lines[new_line])
        
        if (new_line, new_pos) != (line, pos):
            if shift:
                if self._selection_start is None:
                    self._selection_start = (line, pos)
            else:
                self._selection_start = None
            
            self._cursor = (new_line, new_pos)
            self._changed = True
    
    def insert_newline(self) -> None:
        if not self._multiline:
            return
            
        if len(self._text) + 1 > self._maxlength:
            return
            
        line, pos = self._cursor
        current_line = self._lines[line]
        
        self._lines[line] = current_line[:pos]
        self._lines.insert(line+1, current_line[pos:])
        
        self._cursor = (line+1, 0)
        self._text = self._join_lines_to_text(self._lines)
        self._changed = True
    
    def _handle_events(self) -> None:
        if not self._enabled: 
            return
         
        if self.game.input.is_key_pressed("backspace"):
            self.backspace()
        elif self.game.input.is_key_pressed("delete"):
            self.delete()
        elif self.game.input.is_key_pressed("return"):
            self.insert_newline()
        elif self.game.input.is_key_pressed("right") or self.game.input.is_key_pressed("left"):
            x_dir = self.game.input.get_axis("right", "left")
            y_dir = 0
            shift = self.game.input.is_key_down("left shift") or self.game.input.is_key_down("right shift")
            self.move_cursor((x_dir, y_dir), shift)
        elif self.game.input.is_key_pressed("up") or self.game.input.is_key_pressed("down"):
            x_dir = 0
            y_dir = self.game.input.get_axis("down", "up")
            shift = self.game.input.is_key_down("left shift") or self.game.input.is_key_down("right shift")
            self.move_cursor((x_dir, y_dir), shift)
        elif self.game.input.is_key_down("left ctrl") or self.game.input.is_key_down("right ctrl"):
            if self.game.input.is_key_pressed("c"):
                self.copy()
            if self.game.input.is_key_pressed("v"):
                self.paste()
            if self.game.input.is_key_pressed("x"):
                self.cut()
            if self.game.input.is_key_pressed("a"):
                self.select_all()
        elif self.game.input.is_anything_pressed():
            unicode = self.game.input.get_unicode()
            if unicode:
                self.insert_text(unicode)
    
    def update(self) -> None:
        self._handle_events()
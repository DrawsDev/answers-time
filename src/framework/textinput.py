import pygame.scrap
from typing import Tuple, Optional, List
from src.framework.application import Application
from src.framework.utility import clamp

class TextInput:
    def __init__(
        self,
        app: Application,
        text: str = "",
        placeholder: str = "Placeholder",
        maxlength: int = 64,
        line_length: int = 0
    ) -> None:
        self.app = app
        self._text = text
        self._placeholder = placeholder
        self._maxlength = maxlength
        self._line_length = line_length
        self._cursor = 0
        self._selection_start = None
        self._enabled = False
        self._changed = False
    
    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        if self._text != value and len(value) <= self._maxlength:
            self._text = value
            self._changed = True

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
    def line_length(self) -> int:
        return self._line_length
    
    @line_length.setter
    def line_length(self, value: int) -> None:
        if self._line_length != value and value >= 0:
            self._line_length = value
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
    def cursor_position(self) -> int:
        return self._cursor
    
    @cursor_position.setter
    def cursor_position(self, value: int) -> None:
        if self._cursor != value and 0 <= value <= len(self._text):
            self._cursor = value
            self._changed = True

    @property
    def selection_start_position(self) -> Optional[int]:
        return self._selection_start

    @selection_start_position.setter
    def selection_start_position(self, value: Optional[int]) -> None:
        if self._selection_start != value and (value is None or 0 <= value <= len(self._text)):
            self._selection_start = value
            self._changed = True

    @property
    def changed(self) -> bool:
        if self._changed:
            self._changed = False
            return True
        return False

    def has_selection(self) -> bool:
        return self._selection_start is not None and self._selection_start != self._cursor

    def get_selection_range(self) -> Tuple[int, int]:
        if self._selection_start is None:
            return (self._cursor, self._cursor)
        return (min(self._selection_start, self._cursor), max(self._selection_start, self._cursor))

    def delete_selected_text(self) -> None:
        if self.has_selection():
            start, end = self.get_selection_range()
            self._text = self._text[:start] + self._text[end:]
            self._cursor = start
            self._selection_start = None
            self._changed = True

    def backspace(self) -> None:
        if self.has_selection():
            self.delete_selected_text()
        elif self._cursor > 0:
            self._text = self._text[:self._cursor - 1] + self._text[self._cursor:]
            self._cursor -= 1
            self._selection_start = None
            self._changed = True

    def delete(self) -> None:
        if self.has_selection():
            self.delete_selected_text()
        elif self._cursor < len(self._text):
            self._text = self._text[:self._cursor] + self._text[self._cursor + 1:]
            self._selection_start = None
            self._changed = True

    def copy(self) -> None:
        if self.has_selection():
            start, end = self.get_selection_range()
            selected_text = self._text[start:end]
            pygame.scrap.put_text(selected_text)

    def paste(self) -> None:
        clipboard_text = pygame.scrap.get_text()
        if clipboard_text and len(self._text) + len(clipboard_text) <= self._maxlength:
            self.delete_selected_text()
            self._text = self._text[:self._cursor] + clipboard_text + self._text[self._cursor:]
            self._cursor += len(clipboard_text)
            self._selection_start = None
            self._changed = True

    def cut(self) -> None:
        if self.has_selection():
            self.copy()
            self.delete_selected_text()

    def select_all(self) -> None:
        self._cursor = len(self._text)
        self._selection_start = 0
        self._changed = True

    def move_cursor(self, direction: int, shift: bool) -> None:
        new_pos = clamp(self._cursor + direction, 0, len(self._text))
        if shift:
            if self._selection_start is None:
                self._selection_start = self._cursor
        else:
            self._selection_start = None
        if new_pos != self._cursor:
            self._cursor = new_pos
            self._changed = True

    def key(self) -> None:
        unicode = self.app.input.get_unicode()
        if unicode:
            self.delete_selected_text()
            self._insert(unicode)

    def update(self) -> None:
        if not self._enabled:
            return
        
        if self.app.input.is_key_pressed("backspace"):
            self.backspace()
        elif self.app.input.is_key_pressed("delete"):
            self.delete()
        elif self.app.input.is_enter():
            self._insert("\n")
        elif self.app.input.is_key_pressed("right") or self.app.input.is_key_pressed("left"):
            direction = self.app.input.get_axis("right", "left")
            self.move_cursor(direction, self.app.input.is_shift())
        elif self.app.input.is_key_pressed("up") or self.app.input.is_key_pressed("down"):
            direction = self.app.input.get_axis("up", "down")
            self.move_cursor(direction, self.app.input.is_shift())
        elif self.app.input.is_ctrl():
            if self.app.input.is_key_pressed("c"):
                self.copy()
            if self.app.input.is_key_pressed("v"):
                self.paste()
            if self.app.input.is_key_pressed("x"):
                self.cut()
            if self.app.input.is_key_pressed("a"):
                self.select_all()
        elif self.app.input.is_anything_pressed():
            self.key()

    def _insert(self, char: str) -> None:
        self._text = self._text.replace("\n", "")
        raw_text = self._text[:self._cursor] + char + self._text[self._cursor:]
        
        if len(raw_text) > self._maxlength:
            return
        
        if self._line_length > 0:
            self._text = "\n".join([raw_text[i:i+self._line_length] for i in range(0, len(raw_text), self._line_length)])
            self._cursor += len(char) + len("\n")
        else:
            self._text = raw_text
            self._cursor += len(char)

        self._selection_start = None
        self._changed = True

import pygame.scrap
from typing import Tuple
from src.core.game import Game

class InputBox:
    def __init__(
        self,
        game: Game,
        text: str = "",
        placeholder: str = "Placeholder",
        maxlength: int = 64
    ) -> None:
        self.game = game
        self._text = text
        self._placeholder = placeholder
        self._maxlength = maxlength
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
    def enabled(self) -> bool:
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool) -> None:
        if value != self._enabled:
            self._enabled = value
            self._changed = True

    @property
    def cursor(self) -> int:
        return self._cursor
    
    @cursor.setter
    def cursor(self, value: int) -> None:
        if self._cursor != value and 0 <= value <= len(self._text):
            self._cursor = value

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
            start, end = self.get_selection_range()
            selected_text = self._text[start:end]
            pygame.scrap.put_text(selected_text)
            self.delete_selected_text()

    def select(self) -> None:
        self._cursor = len(self._text)
        self._selection_start = 0
        self._changed = True

    def move_cursor(self, direction: int, shift: bool) -> None:
        new_pos = max(0, min(len(self._text), self._cursor + direction))
        if shift:
            if self._selection_start is None:
                self._selection_start = self._cursor
        else:
            self._selection_start = None
        self._cursor = new_pos
        self._changed = True

    def key(self) -> None:
        unicode = self.game.input.get_unicode()
        if unicode != "" and len(self._text) < self._maxlength:
            self.delete_selected_text()
            self._text = self._text[:self._cursor] + unicode + self._text[self._cursor:]
            self._cursor += 1
            self._selection_start = None
            self._changed = True

    def _handle_events(self) -> None:
        if not self._enabled: 
            return
         
        if self.game.input.is_key_pressed("backspace"):
            self.backspace()
        elif self.game.input.is_key_pressed("delete"):
            self.delete()
        elif self.game.input.is_key_pressed("right") or self.game.input.is_key_pressed("left"):
            direction = self.game.input.get_axis("right", "left")
            shift = self.game.input.is_key_down("left shift") or self.game.input.is_key_down("right shift")
            self.move_cursor(direction, shift)
        elif self.game.input.is_key_down("left ctrl") or self.game.input.is_key_down("right ctrl"):
            if self.game.input.is_key_pressed("c"):
                self.copy()
            if self.game.input.is_key_pressed("v"):
                self.paste()
            if self.game.input.is_key_pressed("x"):
                self.cut()
            if self.game.input.is_key_pressed("a"):
                self.select()
        elif self.game.input.is_anything_pressed():
            self.key()

    def update(self) -> None:
        self._handle_events()

__all__ = ["InputBox"]

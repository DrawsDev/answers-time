import os
import shutil
from typing import Tuple, List

class Explorer:
    def __init__(self) -> None:
        self._home_path = os.path.expanduser("~")
        self._current_path = self.home_path
        self._history: List[str] = []
        self._history_index: int = -1
        self._add_to_history(self.current_path)

    @property
    def current_path(self) -> str:
        return self._current_path

    @current_path.setter
    def current_path(self, value: str) -> None:
        if self._current_path != value:
            self._current_path = value

    @property
    def home_path(self) -> str:
        return self._home_path

    @home_path.setter
    def home_path(self, value: str) -> None:
        if self._home_path != value:
            self._home_path = value

    def _add_to_history(self, path: str, new: bool = True) -> None:
        if len(self._history) >= 100:
            self._history.pop(0)
            self._history_index -= 1
        self._history.append(path)
        if new:
            self._history_index += 1
            self._current_path = path

    def copy(self, source_path: str, destination_path: str) -> None:
        try:
            shutil.copy(source_path, destination_path)
        except:
            return

    def move_to(self, path: str) -> None:
        new_path = os.path.abspath(os.path.join(self.current_path, path))

        if os.path.isdir(new_path):
            self._current_path = new_path
            self._add_to_history(new_path)

    def move_home(self) -> None:
        if self._current_path != self._home_path:
            self._current_path = self._home_path
            self._add_to_history(self._home_path)

    def move_up(self) -> None:
        parent = os.path.dirname(self._current_path)
        if self._current_path != parent:
            self._current_path = parent
            self._add_to_history(parent)

    def move_history_forward(self) -> None:
        if self._history_index < len(self._history) - 1:
            self._history_index += 1
            self._current_path = self._history[self._history_index]

    def move_history_backward(self) -> None:
        if self._history_index > 0:
            self._history_index -= 1
            self._current_path = self._history[self._history_index]
            self._add_to_history(self._current_path, False)

    def list_content(self, show_hidden: bool = False, target_extension: str = None) -> List[Tuple[str, str, str, str]]:
        content = []
        
        try:
            items = os.listdir(self.current_path)
        except PermissionError:
            return []

        for item in items:
            if not show_hidden and item.startswith("."):
                continue

            item_path = os.path.join(self.current_path, item)
            try:
                stat = os.stat(item_path)
                if os.path.isdir(item_path):
                    item_type = "dir"
                    size = ""
                else:
                    item_type = "file"
                    size = stat.st_size
                mod_time = stat.st_mtime

                if item_type == "file" and target_extension and not item.endswith(target_extension):
                    continue

                content.append((item, item_type, size, mod_time))
            except PermissionError:
                content.append((item, "access_denied", "", ""))
        return sorted(content, key=lambda x: (not x[1] == "dir", x[0].lower()))

__all__ = ["Explorer"]

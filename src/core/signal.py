from typing import Callable, Set


class Signal:
    def __init__(self) -> None:
        self._callbacks: Set[Callable] = set()

    def emit(self, *args, **kwargs) -> None:
        for callback in self._callbacks:
            callback(*args, **kwargs)

    def connect(self, callback: Callable) -> None:
        self._callbacks.add(callback)
    
    def disconnect(self, callback: Callable) -> None:
        self._callbacks.discard(callback)

    def disconnect_all(self) -> None:
        self._callbacks.clear()

    def get_connection_count(self) -> int:
        return len(self._callbacks)

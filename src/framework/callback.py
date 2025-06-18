from typing import Optional, Union, Tuple, Callable, Any

CallbackType = Union[
    Tuple[Callable, Tuple[Any, ...]],
    Callable,
    None
]

class Callback:
    def __init__(self, callback: Optional[CallbackType] = None):
        self._callback = callback
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Callback):
            return self._callback == other._callback
        if other is CallbackType:
            return self._callback == other
        return False

    def __call__(self, *args, **kwargs) -> None:
        if self._callback is not None:
            if isinstance(self._callback, tuple):
                func, given_args = self._callback
                func(*given_args, *args, **kwargs)
            else:
                self._callback(*args, **kwargs)

    def set(self, callback: Optional[CallbackType] = None) -> None:
        self._callback = callback

__all__ = ["Callback", "CallbackType"]

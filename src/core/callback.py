from typing import Optional, Union, Tuple, Callable, Any

CallbackType = Optional[
    Union[
        Tuple[Callable, Tuple[Any, ...]],
        Callable
    ]
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

    def __call__(self, *a, **kw) -> None:
        if self._callback is not None:
            if isinstance(self._callback, tuple):
                func, args = self._callback
                func(*args)
            else:
                self._callback()

    def set(self, callback: CallbackType) -> None:
        self._callback = callback

__all__ = ["Callback", "CallbackType"]

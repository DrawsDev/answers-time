from ..signal import Signal


class Resource:
    def __init__(self) -> None:
        self._changed: Signal = Signal()

    @property
    def changed(self) -> Signal:
        return self._changed

    def free(self) -> None:
        self._changed.disconnect_all()

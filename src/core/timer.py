from time import time

class Timer:
    def __init__(self, time=1.0, loop=False) -> None:
        self._time = time
        self._loop = loop
        self.reset()
    
    @property
    def expired(self) -> bool:
        result = time() - self._start_t > self._time
        if result & self._loop: self.reset()
        return result

    @property
    def time(self) -> float:
        return self._time
    
    @time.setter
    def time(self, value: float) -> None:
        self._time = value
        self.reset()

    @property
    def loop(self) -> bool:
        return self._loop
    
    @loop.setter
    def loop(self, value: bool) -> None:
        self._loop = value
        self.reset()

    def reset(self) -> None:
        self._start_t = time()
    
    def stop(self) -> None:
        self._start_t = time() - self._time
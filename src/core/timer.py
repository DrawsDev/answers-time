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
    def loop(self) -> bool:
        return self._loop
    
    @loop.setter
    def loop(self, value: bool) -> None:
        self._loop = value

    def reset(self) -> None:
        self._start_t = time()
    
    def stop(self) -> None:
        self._start_t = time() - self._time
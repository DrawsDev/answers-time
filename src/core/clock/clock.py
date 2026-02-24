import pygame

MS_PER_SEC = 1000


class Clock:
    def __init__(self) -> None:
        self._clock = pygame.Clock()
        self._framerate = 60.0
        self._delta = 0.0
        self._accurate = False
    
    @property
    def delta(self) -> float:
        return self._delta
    
    @property
    def framerate(self) -> int:
        return int(self._clock.get_fps())
    
    @framerate.setter
    def framerate(self, value: int) -> None:
        self._framerate = value

    @property
    def accurate(self) -> bool:
        return self._accurate
    
    @accurate.setter
    def accurate(self, value: bool) -> None:
        self._accurate = value

    def get_ticks(self) -> int:
        return pygame.time.get_ticks()

    def tick(self) -> None:
        if self._accurate:
            self._delta = self._clock.tick_busy_loop(self._framerate)
        else:
            self._delta = self._clock.tick(self._framerate)
        self._delta /= MS_PER_SEC
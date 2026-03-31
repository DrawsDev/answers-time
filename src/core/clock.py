import pygame

MS_PER_SEC = 1000


def get_ticks() -> int:
    return pygame.time.get_ticks()


class Clock:
    def __init__(self) -> None:
        self._clock = pygame.Clock()
        self._framerate = 60.0
        self._delta = 0.0
        self._accurate = False
    
    def get_delta(self) -> float:
        return self._delta
    
    def get_framerate(self) -> int:
        return int(self._clock.get_fps())

    def set_framerate(self, framerate: float) -> None:
        self._framerate = framerate

    def is_accurate(self) -> bool:
        return self._accurate
    
    def set_accurate(self, enabled: bool) -> None:
        self._accurate = enabled

    def tick(self) -> None:
        if self._accurate:
            self._delta = self._clock.tick_busy_loop(self._framerate)
        else:
            self._delta = self._clock.tick(self._framerate)
        self._delta /= MS_PER_SEC

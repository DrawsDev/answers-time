import pygame

class Window:
    def __init__(self, title: str, width: int, height: int) -> None:
        self._screen = pygame.display.set_mode((width, height), pygame.SCALED)
        self._clock = pygame.Clock()
        self._delta = 0.0
        self._framerate = 60.0
        self._should_close = False
        self.set_title(title)

    def get_delta(self) -> float:
        return self._delta

    def set_framerate(self, framerate: float) -> None:
        if self._framerate != framerate:
            self._framerate = framerate

    def get_framerate(self) -> int:
        framerate = self._clock.get_fps()
        return round(framerate)

    def toggle_fullscreen(self) -> None:
        pygame.display.toggle_fullscreen()

    def is_fullscreen(self) -> None:
        pygame.display.is_fullscreen()

    def set_title(self, title: str) -> None:
        pygame.display.set_caption(title)

    def get_title(self) -> str:
        return pygame.display.get_caption()[0]

    def is_should_close(self) -> bool:
        return self._should_close

    def process(self) -> None:
        self._delta = self._clock.tick(self._framerate) / 1000
        self._should_close = pygame.event.get(pygame.QUIT)
        pygame.display.update()

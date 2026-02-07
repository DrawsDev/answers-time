import pygame

class Window:
    def __init__(self, title: str, width: int, height: int) -> None:
        self.screen = pygame.display.set_mode((width, height), pygame.SCALED)
        self.clock = pygame.Clock()
        self.delta = 0.0
        self.framerate = 60.0
        self.should_close = False
        self.set_title(title)

    def get_delta(self) -> float:
        return self.delta

    def set_framerate(self, framerate: float) -> None:
        if self.framerate != framerate:
            self.framerate = framerate

    def get_framerate(self) -> float:
        return self.clock.get_fps()

    def toggle_fullscreen(self) -> None:
        pygame.display.toggle_fullscreen()

    def is_fullscreen(self) -> None:
        pygame.display.is_fullscreen()

    def set_title(self, title: str) -> None:
        pygame.display.set_caption(title)

    def get_title(self) -> str:
        return pygame.display.get_caption()[0]

    def is_should_close(self) -> bool:
        return self.should_close

    def process(self) -> None:
        self.delta = self.clock.tick(self.framerate) / 1000
        self.should_close = pygame.event.get(pygame.QUIT)
        pygame.display.update()

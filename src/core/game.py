import pygame
import sys
from src.components.scene import Scene

game = None

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("TEST")
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.Clock()
        self._init_scenes()

        global game
        game = self

    def _init_scenes(self) -> None:
        self._scene: Scene = None
        self._scenes: dict[str, Scene] = {}

    def add_scene(self, name: str, object: Scene):
        if not name in self._scenes:
            self._scenes[name] = object

    def change_scene(self, name: str, **kwargs) -> None:
        if name in self._scenes:
            if self._scene:
                self._scene.on_exit()
            self._scene = self._scenes[name]()
            self._scene.on_enter(**kwargs)

    def quit(self) -> None:
        pygame.quit()
        sys.exit()

    def run(self) -> None:
        while True:
            delta = self.clock.tick(60) / 1000
            self._input()
            self._update(delta)
            self._draw()

    def _input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
    
    def _update(self, delta: float) -> None:
        if self._scene:
            self._scene.update(delta)

    def _draw(self) -> None:
        if self._scene:
            self._scene.draw(self.screen)

        pygame.display.flip()

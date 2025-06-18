import sys
import pygame
from typing import Dict
from src.framework.settings import *
from src.framework.utility import *
from src.framework.input import Input
from src.framework.audio import Audio
from src.framework.scene import Scene

class Application:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(TITLE)
        self._settings = load_settings()
        self._screen = pygame.display.set_mode(WINDOW_SIZE, FLAGS, 0, 0, VSYNC)
        self._surface = pygame.Surface(SURFACE_SIZE)
        self._clock = pygame.Clock()
        self._input = Input()
        self._audio = Audio()
        self._apply_settings()
        self._scene: Scene = None
        self._scenes: Dict[str, Scene] = {}
    
    @property
    def surface(self) -> pygame.Surface:
        return self._surface
    
    @property
    def clock(self) -> pygame.Clock:
        return self._clock
    
    @property
    def input(self) -> Input:
        return self._input

    @property
    def settings(self) -> Dict:
        return self._settings

    def insert_scene(self, name: str, scene: Scene) -> None:
        if not name in self._scenes:
            self._scenes[name] = scene

    def remove_scene(self, name: str) -> None:
        if name in self._scenes:
            self._scenes.pop(name)

    def change_scene(self, name: str, *args, **kwargs) -> None:
        if name in self._scenes:
            if self._scene is not None:
                self._scene.on_exit()
            self._scene = self._scenes[name](self)
            self._scene.on_enter(*args, **kwargs)

    def run(self) -> None:
        while True:
            self._update()
            self._draw()

    def quit(self) -> None:
        pygame.quit()
        sys.exit()

    def update_setting(self, name: str, value: Any) -> None:
        self.settings[name] = value
        save_settings(self.settings)
        self._apply_settings()

    def _apply_settings(self) -> None:
        if self.settings is None:
            self._settings = get_default_settings()
            save_settings(self.settings)
        if self.settings["Fullscreen"] != pygame.display.is_fullscreen():
            pygame.display.toggle_fullscreen()
    
    def _update(self) -> None:
        delta = self._clock.tick(FRAMERATE) / 1000
        events = pygame.event.get()
        self._input.update(events)
        for event in events:
            if event.type == pygame.QUIT:
                self.quit()
        if self._scene is not None:
            self._scene.update(delta)
    
    def _draw(self) -> None:
        if self._scene is not None:
            self._scene.draw(self._surface)
        self._screen.blit(pygame.transform.scale(self._surface, self._screen.get_size()))
        pygame.display.update()

__all__ = ["Application"]

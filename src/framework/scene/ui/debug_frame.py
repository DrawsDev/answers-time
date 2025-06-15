import pygame
from typing import Tuple, List
from src.framework.settings import *
from src.framework.application import *

class DebugFrame:
    def __init__(self, app: Application):
        self.app = app
        self._font = pygame.Font(None, 13)
        self._enabled = False

    @property
    def enabled(self) -> bool:
        return self._enabled
    
    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value

    def _get_ratio(self) -> Tuple[float, float]:
        window_size = pygame.display.get_window_size()
        return (window_size[0] / SURFACE_SIZE[0], window_size[1] / SURFACE_SIZE[1])

    def _get_debug_items(self) -> List[Tuple[str, str]]:
        debug_items = []
        debug_items.append(("VER", f"{VERSION_MAJOR}.{VERSION_MINOR}.{BUILD}"))
        debug_items.append(("FPS", f"{self.app.clock.get_fps():.1f}"))
        debug_items.append(("W_MPOS", str(self.app.input.get_mouse_screen_position())))
        debug_items.append(("R_MPOS", str(self.app.input.get_mouse_position())))
        debug_items.append(("RATIO", str(self._get_ratio())))
        return debug_items

    def update(self) -> None:
        if self.app.input.is_key_pressed("f1"):
            self._enabled = not self._enabled

    def draw(self, surface: pygame.Surface) -> None:
        if self._enabled:
            linesize = self._font.get_linesize()
            for i, v in enumerate(self._get_debug_items()):
                text_surface = self._font.render(f"{v[0]}: {v[1]}", True, "White", "Black")
                surface.blit(text_surface, (0, linesize * i))

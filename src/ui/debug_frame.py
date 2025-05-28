import pygame
from typing import Tuple, List
from src.settings import SURFACE_SIZE
from src.core.game import Game

class DebugFrame:
    def __init__(self, game: Game):
        self.game = game
        self._font = pygame.Font(None, 13)
        self._enabled = False

    def _get_debug_items(self) -> List[Tuple[str, str]]:
        debug_items = []
        debug_items.append(("VER", "1.0"))
        debug_items.append(("FPS", f"{self.game.clock.get_fps():.1f}"))
        mouse_pos = pygame.mouse.get_pos()
        window_size = pygame.display.get_window_size()
        ratio = (window_size[0] / SURFACE_SIZE[0], window_size[1] / SURFACE_SIZE[1])
        ratio_mouse_pos = (int(mouse_pos[0] / ratio[0]), int(mouse_pos[1] / ratio[1]))
        debug_items.append(("W_MPOS", str(mouse_pos)))
        debug_items.append(("R_MPOS", str(ratio_mouse_pos)))
        debug_items.append(("RATIO", str(ratio)))
        return debug_items

    def update(self, delta: float) -> None:
        if self.game.input.is_key_pressed("f1"):
            self._enabled = not self._enabled

    def draw(self, surface: pygame.Surface) -> None:
        if not self._enabled:
            return
        linesize = self._font.get_linesize()
        for i, v in enumerate(self._get_debug_items()):
            text_surface = self._font.render(f"{v[0]}: {v[1]}", True, "White", "Black")
            surface.blit(text_surface, (0, linesize * i))

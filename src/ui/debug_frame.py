import pygame
from src.settings import FONTS, SURFACE_SIZE
from src.core.game import Game
from src.core.utility import asset_path

class DebugFrame:
    def __init__(self, game: Game):
        self.font = pygame.Font(asset_path(FONTS, "Tiny5-Regular.ttf"), 8)
        self.charsize = self.font.size(" ")
        self.clock = game.clock
    
    def _render(self, text: str) -> pygame.Surface:
        return self.font.render(text, True, "WHITE")

    def update(self, delta: float) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        # VER
        ver = self._render("VER: 1.0")
        surface.blit(ver, [0, 0])
        # FPS
        fps = self._render("FPS: %.1f" % self.clock.get_fps())
        surface.blit(fps, [0, self.charsize[1]])
        # MOUSE POSITION
        mouse_pos = pygame.mouse.get_pos()
        window_size = pygame.display.get_window_size()
        ratio = tuple([window_size[0] / SURFACE_SIZE[0], window_size[1] / SURFACE_SIZE[1]])
        ratio_mouse_pos = tuple([mouse_pos[0] / ratio[0], mouse_pos[1] / ratio[1]])
        surface.blit(self._render("WIN_POS: " + str(mouse_pos)), [0, self.charsize[1] * 2])
        surface.blit(self._render("SRF_POS: " + str(ratio_mouse_pos)), [0, self.charsize[1] * 3])
        surface.blit(self._render("RATIO: " + str(ratio)), [0, self.charsize[1] * 4])

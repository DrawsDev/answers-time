import pygame
from typing import Tuple

class Mouse:
    def _check_button_state(self, button: int, state: Tuple[bool, bool, bool, bool, bool]) -> bool:
        if 0 <= button <= 4:
            return state[button]
        return False
    
    def is_pressed(self, button: int) -> None:
        state = pygame.mouse.get_pressed(5)
        return self._check_button_state(button, state)

    def is_released(self, button: int) -> None:
        return not self.is_pressed(button)

    def is_just_pressed(self, button: int) -> None:
        state = pygame.mouse.get_just_pressed()
        return self._check_button_state(button, state)

    def is_just_released(self, button: int) -> None:
        state = pygame.mouse.get_just_released()
        return self._check_button_state(button, state)

    def set_position(self, position: Tuple[int, int]) -> None:
        pygame.mouse.set_pos(position)

    def get_position(self) -> Tuple[int, int]:
        return pygame.mouse.get_pos()

    def get_delta(self) -> Tuple[int, int]:
        return pygame.mouse.get_rel()

    def is_moved(self) -> bool:
        x, y = self.get_delta()
        return x != 0 or y != 0

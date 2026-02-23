from typing import Tuple
import pygame

class Mouse:
    @staticmethod
    def _get_button_state(button: int, state: Tuple[bool, bool, bool, bool, bool]) -> bool:
        if 0 <= button <= 4:
            return state[button]
        return False
    
    @staticmethod
    def is_pressed(button: int) -> None:
        state = pygame.mouse.get_pressed(5)
        return Mouse._get_button_state(button, state)

    @staticmethod
    def is_released(button: int) -> None:
        return not Mouse.is_pressed(button)

    @staticmethod
    def is_just_pressed(button: int) -> None:
        state = pygame.mouse.get_just_pressed()
        return Mouse._get_button_state(button, state)

    @staticmethod
    def is_just_released(button: int) -> None:
        state = pygame.mouse.get_just_released()
        return Mouse._get_button_state(button, state)

    @staticmethod
    def set_position(position: Tuple[int, int]) -> None:
        pygame.mouse.set_pos(position)

    @staticmethod
    def get_position() -> Tuple[int, int]:
        return pygame.mouse.get_pos()

    @staticmethod
    def get_delta() -> Tuple[int, int]:
        return pygame.mouse.get_rel()

    @staticmethod
    def is_moved() -> bool:
        x, y = Mouse.get_delta()
        return x != 0 or y != 0
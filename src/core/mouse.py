from typing import Tuple
import pygame


def _get_button_state(button: int, state: Tuple[bool, bool, bool, bool, bool]) -> bool:
    if 0 <= button <= 4:
        return state[button]
    return False


def is_pressed(button: int) -> None:
    state = pygame.mouse.get_pressed(5)
    return _get_button_state(button, state)


def is_released(button: int) -> None:
    return not is_pressed(button)


def is_just_pressed(button: int) -> None:
    state = pygame.mouse.get_just_pressed()
    return _get_button_state(button, state)


def is_just_released(button: int) -> None:
    state = pygame.mouse.get_just_released()
    return _get_button_state(button, state)


def set_position(position: Tuple[int, int]) -> None:
    pygame.mouse.set_pos(position)


def get_position() -> Tuple[int, int]:
    return pygame.mouse.get_pos()


def get_delta() -> Tuple[int, int]:
    return pygame.mouse.get_rel()


def is_moved() -> bool:
    x, y = get_delta()
    return x != 0 or y != 0

import os
import pygame
from typing import Tuple

# Window
TITLE: str = "Answers Time"
WINDOW_SIZE: Tuple[int, int] = (1280, 720)
SURFACE_SIZE: Tuple[int, int] = (640, 360)
FRAMERATE: int = 60
VSYNC: int = 1
FLAGS: int = pygame.DOUBLEBUF

# Paths
SPRITES: str = os.path.join("content", "sprites")
SOUNDS: str = os.path.join("content", "sounds")
FONTS: str = os.path.join("content", "fonts")
SCENES: str = os.path.join("content", "scenes")
QUIZZES: str = os.path.join("content", "quizzes")

# Version
VERSION_MAJOR: int = 1
VERSION_MINOR: int = 0
BUILD: int = 213

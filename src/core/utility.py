import os
import sys
import pygame
from typing import Any, Optional

PNG = ".png"
TTF = ".ttf"

def clamp(v: float, min_v: float, max_v: float) -> float:
    return max(min(v, max_v), min_v)

def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t

def path(relative_path: str) -> str:
    """Получение абсолютного пути до файла."""
    base_path = getattr(sys, "_MEIPASS", os.getcwd())
    # Если файл не запакован в exe (на деле костыль :P)
    if not os.path.exists(os.path.join(base_path, relative_path)):
        base_path = os.getcwd()
    return os.path.join(base_path, relative_path)

def asset_path(path: str, *paths: str) -> str:
    """Возвращает абсолютный путь к ресурсу"""
    relative_path = os.path.join(path, *paths)
    base_path = getattr(sys, "_MEIPASS", os.getcwd())
    # Если файл не запакован в exe (на деле костыль :P)
    if not os.path.exists(os.path.join(base_path, relative_path)):
        base_path = os.getcwd()
    return os.path.join(base_path, relative_path)

def _load_image(filepath: str) -> Optional[pygame.Surface]:
    """Загружает и возвращает изображение"""
    if os.path.exists(filepath):
        surface = pygame.image.load(filepath)
        surface.set_colorkey("Black")
        return surface
    return None

def _load_font(filepath: Optional[str] = None, size: int = 20) -> pygame.Font:
    """Загружает и возвращает шрифт"""
    if (filepath is None or os.path.exists(filepath)) and size >= 0:
        return pygame.Font(filepath, size)
    return pygame.Font()

def load_asset(path: str, *paths: str, **attributes) -> Optional[Any]:
    """Загружает ресурс по полученному пути и возвращает его"""
    path_to = asset_path(path, *paths)
    _, extension = os.path.splitext(path_to)
    if extension == PNG:
        return _load_image(path_to)
    elif extension == TTF:
        return _load_font(path_to, attributes.get("size"))

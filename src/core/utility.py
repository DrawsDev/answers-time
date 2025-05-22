import os
import sys

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

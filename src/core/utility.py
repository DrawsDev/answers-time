import sys

def clamp(v: float, min_v: float, max_v: float) -> float:
    return max(min(v, max_v), min_v)

def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t

def path(relative_path: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        return f"{sys._MEIPASS}\{relative_path}" 
    return relative_path

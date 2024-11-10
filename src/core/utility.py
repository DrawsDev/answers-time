def clamp(v: float, min_v: float, max_v: float) -> float:
    return max(min(v, max_v), min_v)

def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t

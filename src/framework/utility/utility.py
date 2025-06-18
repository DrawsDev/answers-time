import os
import sys
import json
import pygame
from typing import Any, Optional, Tuple, List

PNG = ".png"
TTF = ".ttf"

def clamp(v: float, min_v: float, max_v: float) -> float:
    return max(min(v, max_v), min_v)

def lerp(a: float, b: float, t: float) -> float:
    epsilon = 1e-9
    result = a + (b - a) * t
    if -epsilon < result < epsilon: 
        return 0
    if abs(abs(b) - abs(result)) <= epsilon:
        return b
    return result

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

def _wrap_text(
    text: str,  
    font: pygame.Font, 
    max_width: int
) -> List[str]:
    """Разбивает текст на строки, не превышающие максимальный предел по ширине

    Args:
        text (str): Текст
        font (pygame.Font): Шрифт
        max_width (int): Максимальный предел по ширине    

    Returns:
        List (List[str]): Строки
    """
    lines = []
    line = []
    for word in text.split():
        if font.size(" ".join(line + [word]))[0] <= max_width:
            line.append(word)
        else:
            if line:
                lines.append(" ".join(line))
            line = [word]
    if line:
        lines.append(" ".join(line))
    return lines 

def wrap_text(
    text: str, 
    font_path: Optional[str], 
    max_width: int, 
    max_height: int, 
    init_size: int
) -> Tuple[int, List[str]]:
    """Разбивает текст на строки, находит допустимый размер шрифта для их рендеринга

    Args:
        text (str): Текст
        fontpath (Optional[str]): Путь к шрифту
        max_width (int): Максимальный предел по ширине
        max_height (int): Максимальный предел по высоте
        init_size (int): Изначальный размер шрифта

    Returns:
        Tuple (Tuple[int, List[str]]): Размер шрифта и строки
    """
    font_size = init_size
    while font_size >= 1:
        font = pygame.Font(font_path, font_size)
        lines = _wrap_text(text, font, max_width)
        fits_width = all(font.size(line)[0] <= max_width for line in lines)
        fits_height = len(lines) * font.get_linesize() <= max_height
        if fits_width and fits_height:
            break
        font_size -= 1
    return font_size, lines

def open_url(url: str) -> None:
    """
    Открывает ссылку в браузере
    
    https://stackoverflow.com/a/4217323
    """
    if sys.platform == "win32":
        os.startfile(url)
    elif sys.platform == "darwin":
        subprocess.Popen(["open", url])
    else:
        try:
            subprocess.Popen(["xdg-open", url])
        except OSError:
            print("Please open a browser on:", url)

def load_settings() -> dict:
    filepath = os.path.join(os.getcwd(), "settings.json")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)

def save_settings(settings: dict) -> None:
    filepath = os.path.join(os.getcwd(), "settings.json")
    with open(filepath, "w", encoding="utf-8") as file:
        return json.dump(settings, file, ensure_ascii=False)

def get_default_settings() -> dict:
    return {
        "Fullscreen": True
    }

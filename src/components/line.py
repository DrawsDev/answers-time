import re
import pygame
from typing import List
from contextlib import suppress
from src.core.timer import Timer

class Line:
    def __init__(self, 
                 text: str = "",
                 color: pygame.Color = pygame.Color("Black"),
                 rgb: bool = False, 
                 angry: bool = False,
                 wave: bool = False,
                 quiet: bool = False,
                 shake: bool = False, 
                 shake_amplitude: float = 1,
                 wobble: bool = False,
                 pause: float = 0, 
                 typing_speed: float = 0.05,
                 gradient_color: pygame.Color = None) -> None:
        self.text: str = text
        self.color: pygame.Color = color
        self.rgb: bool  = rgb
        self.angry: bool  = angry
        self.wave: bool  = wave
        self.quiet: bool  = quiet
        self.shake: bool  = shake
        self.shake_amplitude: float = shake_amplitude
        self.wobble: bool = wobble
        self.pause: float = pause
        self.typing_speed: float = typing_speed
        self.gradient_color: pygame.Color | None = gradient_color
        self._next_color: pygame.Color = color
        self._offsets: List[float] = []
        self._alphas: List[float] = []

def parse_string(text: str) -> List[Line]:
    """
    Синтаксический анализ строки. Создаётся список Line с применёнными к ним найденных аттрибутов в метках.
    
    Пример: 
       Вход: `<f color=Lime>Привет </f><f rgb=True>мир</f>!`
       Выход: `[Line(text="Привет ", color=(0, 255, 0)), Line(text="мир", rgb=True), Line(text="!")]`
    
    Args:
        text (str): Строка с метками.
    
    Returns:
        List[Line]: Список Line.
    """
    lines: List[Line] = []
    line: Line = Line()
    index: int = 0
    
    while index < len(text):
        tag_match = re.search(r"<f\s+(.*?)>|</f>", text[index:])
        if not tag_match:
            line.text += text[index:]
            break
        
        start, end = tag_match.span()
        is_closing = tag_match.group(0).startswith("</")

        if start > 0:
            line.text = text[index:index+start]
        
        if line.text:
            lines.append(line)
            line = Line()
        
        if not is_closing:
            # Поиск аттрибутов и применение к Line
            for effect in tag_match.group(1).split():
                if "=" in effect:
                    key, value = effect.split("=", 1)
                    
                    if key == "color":
                        with suppress(ValueError): line.color = pygame.Color(value)
                    elif key == "rgb":
                        line.rgb = value.lower() == "true"
                        line.wave = True
                    elif key == "quiet":
                        line.quiet = value.lower() == "true"
                    elif key == "wave":
                        line.wave = value.lower() == "true"
                    elif key == "shake":
                        line.shake = True
                        with suppress(ValueError): line.shake_amplitude = float(value)
                    elif key == "wobble":
                        line.wobble = value.lower() == "true"
                    elif key == "angry":
                        line.angry = True
                        line.shake = True
                        with suppress(ValueError): line.shake_amplitude = float(value)
                    elif key == "typing_speed":
                        with suppress(ValueError): line.typing_speed = float(value)
                    elif key == "pause":
                        with suppress(ValueError): line.pause = float(value)
                    elif key == "gradient":
                        with suppress(ValueError): line.gradient_color = pygame.Color(value)

        index += end

    if line.text:
        lines.append(line)
        line = None

    return lines

def get_text_from_lines(lines: List[Line]) -> str:
    """Возвращает объединенный текст всех Line из списка."""
    return "".join(line.text for line in lines)

import math
import time
import copy
import random
import pygame
from typing import List, Tuple
from src.core.utility import lerp

BLACK = (0, 0, 0)
RED = (255, 0, 0)
MS_IN_SEC = 1000
SPACE = " "
PERIOD = "."
ANIM_START_OFFSET = 5
ANIM_END_OFFSET = 0
ANIM_OFFSET_STEP = 0.5
ANIM_END_ALPHA = 255
ANIM_START_ALPHA = 0
ANIM_ALPHA_STEP = 17
BOX_PADDING = [10, 10]

class Line:
    def __init__(self, text: str,
                 color: pygame.Color = BLACK,
                 rgb=False, 
                 angry=False,
                 wave=False,
                 quiet=False,
                 shake=False, shake_amplitude=1,
                 pause=0, speed=0.05) -> None:
        self.text = text
        self.color = color
        self.rgb = rgb
        self.angry = angry
        self.wave = wave
        self.quiet = quiet
        self.shake = shake
        self.shake_amplitude = shake_amplitude
        self.pause = pause
        self.speed = speed
        self._offsets: List[float] = []
        self._alphas: List[float] = []

    def get_shake_amplitude(self) -> float:
        return round(random.uniform(-self.shake_amplitude, self.shake_amplitude)) 

class Dialogue:
    def __init__(self) -> None:
        self.font = pygame.font.Font(None, 24) #None
        self.antialias = True #True
        self.width_limit = 280
        self.visible_characters = -1
        self.char_by_char = True

        self._ss = pygame.mixer.Sound("content/sounds/00000e80.wav") #etu_voice
        self._ss2 = pygame.mixer.Sound("content/sounds/00000ef7.wav")
        self._angry_voice = pygame.mixer.Sound("content/sounds/00000f08.wav")
        self._ss_start_time = 0

        self._next_line_sprite = pygame.image.load("content/images/next_line.png")
        self._next_line_sprite.set_colorkey("Black")

        self._typing_start_ms: int = 0
        self._current_text: str = ""
        self._current_lines: List[Line] = []
        self._output_lines: List[Line] = []
        self._line_index: int = 0
        self._char_index: int = 0
        self._ended: bool = False

    def render(self, text: str, color: pygame.Color = BLACK) -> pygame.Surface:
        """Отрисовывает текст и возвращает результат в виде поверхности. 

        Args:
            text (str): Текст для отрисовки.
            color (pygame.Color, optional): Цвет текста. Defaults to BLACK.

        Returns:
            pygame.Surface: Поверхность с отрисованным текстом.
        """        
        return self.font.render(text, self.antialias, color)

    def get_text_from_lines(self, lines: List[Line]) -> str:
        """Получить общий текст из списка с объектами Line.

        Args:
            lines (List[Line]): Список с объектами Line.

        Returns:
            str: Общий текст.
        """        
        return "".join([line.text for line in lines])

    def get_result_surface_size(self, lines: List[Line]) -> Tuple[int, int]:
        """Возвращает итоговый размер диалогового окна.

        Args:
            lines (List[Line]): Список текстов с эффектами.

        Returns:
            (width, height) (Tuple[int, int]): Итоговый размер диалогового окна.
        """        
        result_width = 0
        result_height = 0
        line_width = 0
        line_height = 0
        for line in lines:
            for char in line.text:
                char_w, char_h = self.font.size(char)

                line_width += char_w

                if result_width < line_width:
                    result_width = line_width

                if self.width_limit > 0 and line_width > self.width_limit and char == SPACE:
                    line_width = 0
                    line_height += char_h    
                    
                result_height = line_height + char_h

        return result_width + 20, result_height + 20
            
    def render_lines(self, lines: List[Line], position: pygame.Vector2, surface: pygame.Surface) -> None:
        """Отрисовывает текст с эффектами на поверхности.

        Args:
            lines (List[Line]): Список текстов с эффектами для отрисовки.
            surface (pygame.Surface): Поверхность, на которой будет отрисован весь текст.
        """        
        current_ms = time.time() * MS_IN_SEC
        
        # Если полученный текст не совпадает с прошлым, то всё обнулить
        text = self.get_text_from_lines(lines)
        if self._current_text != text:
            self._current_text = text
            self._current_lines = lines
            self._output_lines.clear()
            self._line_index = 0
            self._char_index = 0
            self._ended = False
            self._typing_start_ms = 0

            self._text_surface = pygame.Surface(self.get_result_surface_size(lines))
            self._text_surface.fill("#000D2C")

        # Текущая часть текста
        line = lines[self._line_index]

        # Посимвольный вывод текста
        if current_ms - self._typing_start_ms >= line.speed * MS_IN_SEC:
            self._typing_start_ms = current_ms

            if len(self._output_lines) == 0:
                copy_line = copy.deepcopy(line)
                copy_line.text = ""
                self._output_lines.append(copy_line)
            
            if self._output_lines[self._line_index].text == line.text:
                if self._line_index < len(lines) - 1:
                    self._line_index += 1

                    line = lines[self._line_index]
                    
                    copy_line = copy.deepcopy(line)
                    copy_line.text = ""
                    self._output_lines.append(copy_line)

                    self._char_index = 0
                    self._typing_start_ms = current_ms + line.pause * MS_IN_SEC
                else:
                    if not self._ended:
                        self._ended = True
                        self._ss2.play()
            else:
                if line.angry:
                    self._output_lines[self._line_index].text = line.text
                    for _ in line.text:
                        self._output_lines[self._line_index]._offsets.append(ANIM_END_OFFSET)
                        self._output_lines[self._line_index]._alphas.append(ANIM_END_ALPHA)
                    self._angry_voice.play()
                else:
                    char = line.text[self._char_index]

                    self._output_lines[self._line_index].text += char
                    self._output_lines[self._line_index]._offsets.append(ANIM_START_OFFSET)
                    self._output_lines[self._line_index]._alphas.append(ANIM_START_ALPHA)
                    self._char_index += 1

                    # Voice
                    if not char in (SPACE, PERIOD) and not line.quiet:
                        if current_ms - self._ss_start_time >= (self._ss.get_length()) * MS_IN_SEC: 
                            self._ss_start_time = current_ms
                            self._ss.play()

        # Отрисовка текста
        animation_step = (pygame.time.get_ticks() / 2000.0) * 4.0
        a_x = position[0] - self._text_surface.get_width() / 2
        a_y = position[1] - self._text_surface.get_height() - 15
        line_size = [0, 0]

        # Отрисовка окна и указателя
        surface.blit(self._text_surface, (a_x, a_y))
        pygame.draw.polygon(surface, "#000D2C", [(position[0] - 10, position[1] - 15), (position[0], position[1] - 5), (position[0] + 10, position[1] - 15)])

        # Отрисовка символов текста
        for _, line in enumerate(self._output_lines):
            if line.angry and line.shake_amplitude > 0:
                line.shake_amplitude = lerp(line.shake_amplitude, 0, 0.005)

            for char_index, char in enumerate(line.text):
                if line._offsets[char_index] > ANIM_END_OFFSET:
                    line._offsets[char_index] -= ANIM_OFFSET_STEP
                if line._alphas[char_index] < ANIM_END_ALPHA:
                    line._alphas[char_index] += ANIM_ALPHA_STEP

                # Отрисовка символа с эффектами
                sector = math.pi / 5

                if line.rgb:
                    hue = (animation_step * 32 + char_index) % 360
                    char_render = self.render(char, pygame.Color.from_hsva(hue, 100, 100))
                    char_pos = [a_x + BOX_PADDING[0] + 1 * math.cos(animation_step * 3 + sector * char_index), a_y + BOX_PADDING[1] + 2 * math.sin(animation_step * 3 + sector * char_index)]
                elif line.shake:
                    char_render = self.render(char, line.color)
                    char_pos = [a_x + BOX_PADDING[0] + line.get_shake_amplitude(), a_y + BOX_PADDING[1] + line.get_shake_amplitude()]          
                elif line.angry:
                    char_render = self.render(char, RED)
                    char_pos = [a_x + BOX_PADDING[0] + line.get_shake_amplitude(), a_y + BOX_PADDING[1] + line.get_shake_amplitude()]                       
                elif line.wave:
                    char_render = self.render(char, line.color)
                    char_pos = [a_x + BOX_PADDING[0] + 1 * math.cos(animation_step * 3 + sector * char_index), a_y + BOX_PADDING[1] + 2 * math.sin(animation_step * 3 + sector * char_index)] 
                else:
                    char_render = self.render(char, line.color)
                    char_pos = [a_x + BOX_PADDING[0], a_y + BOX_PADDING[1]]

                char_render.set_alpha(line._alphas[char_index])

                # Отрисовка
                surface.blit(char_render, (char_pos[0] + line_size[0], char_pos[1] + line_size[1] - line._offsets[char_index]))
                
                # Обновление позиционирования
                c_w, c_h = self.font.size(char)

                line_size[0] += c_w

                # Перенос на новую строку, если ширина строки больше лимита ширины
                if self.width_limit > 0 and line_size[0] > self.width_limit and char == SPACE:
                    line_size[0] = 0
                    line_size[1] += c_h               

        # Если всё отрисовано, то отрисовать указатель
        if self._ended:
            pos = (a_x + self._text_surface.get_width() + 5, a_y + self._text_surface.get_height() / 2)
            surface.blit(self._next_line_sprite, self._next_line_sprite.get_rect(**{"midleft": pos}))

    def skip_typing(self) -> None:
        """Пропустить появление символов и сразу показать весь текст."""
        self._typing_start_ms = 0

        for line_index, line in enumerate(self._current_lines):
            if line_index > len(self._output_lines) - 1:
                self._output_lines.append(copy.deepcopy(line))           

            self._output_lines[line_index].text = line.text

            if line.angry:
                self._output_lines[line_index].shake_amplitude = 0

            for char_index, _ in enumerate(line.text):
                if char_index > len(self._output_lines[line_index]._offsets) - 1:
                    self._output_lines[line_index]._offsets.append(ANIM_START_OFFSET)

                if char_index > len(self._output_lines[line_index]._alphas) - 1:
                    self._output_lines[line_index]._alphas.append(ANIM_START_ALPHA)

    def is_typing_finished(self) -> bool:
        """Проверить выведен весь текст или нет.

        Returns:
            bool: True - выведен весь текст. 
                  False - выведен не весь текст.
        """        
        return self._current_text != "" and self.get_text_from_lines(self._output_lines) == self._current_text

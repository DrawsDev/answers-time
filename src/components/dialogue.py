import math
import random
import pygame
from typing import List

BLACK = (0, 0, 0)

class Line:
    def __init__(self, text: str, 
                 color: pygame.Color = BLACK,
                 rgb=False, 
                 shake=False, shake_amplitude=1,
                 pause=0, speed=1) -> None:
        self.text = text
        self.color = color
        self.rgb = rgb
        self.shake = shake
        self.shake_amplitude = shake_amplitude
        self.pause = pause
        self.speed = speed

    def get_shake_amplitude(self) -> float:
        return random.uniform(-self.shake_amplitude, self.shake_amplitude)

class Dialogue:
    def __init__(self) -> None:
        self.font = pygame.font.Font(None, 24)
        self.antialias = True
        self.width_limit = 0
        self.visible_characters = -1
        self.char_by_char = True

        self._prev_text = ""
        self._ss = pygame.mixer.Sound("content/sounds/etu_voice.wav")
        self._ss_start_time = 0

    def render(self, text: str, color: pygame.Color = BLACK) -> pygame.Surface:
        """Отрисовывает текст и возвращает результат в виде поверхности. 

        Args:
            text (str): Текст для отрисовки.
            color (pygame.Color, optional): Цвет текста. Defaults to BLACK.

        Returns:
            pygame.Surface: Поверхность с отрисованным текстом.
        """        
        return self.font.render(text, self.antialias, color)

    def render_lines(self, lines: List[Line], surface: pygame.Surface) -> None:
        """Отрисовывает текст с эффектами на поверхности.

        Args:
            lines (List[Line]): Список текстов с эффектами для отрисовки.
            surface (pygame.Surface): Поверхность, на которой будет отрисован весь текст.
        """        
        a_x = surface.get_width() / 2
        a_y = surface.get_height() / 2
        line_size = [0, 0]

        step = (pygame.time.get_ticks() / 2000.0) * 4.0

        characters = 0

        # Обновление видимых символов при изменении текста
        if self.char_by_char:
            text = "".join([line.text for line in lines])

            if self._prev_text != text:
                self.visible_characters = -1
                self._prev_text = text

            if self.visible_characters < len(text):
                self.visible_characters += 1
                if pygame.time.get_ticks() - self._ss_start_time >= (self._ss.get_length()) * 1000:
                    self._ss_start_time = pygame.time.get_ticks()
                    self._ss.play()

        # Отрисовка строк по символам
        for line in lines:
            for index, char in enumerate(line.text):
                # Если количество символов больше видимых, то пропустить итерацию
                if self.visible_characters > -1 and characters >= self.visible_characters:
                    continue 
                
                # Отрисовка символа с эффектами
                if line.rgb:
                    hue = (step * 32 + index) % 360
                    char_render = self.render(char, pygame.Color.from_hsva(hue, 100, 100))
                    char_pos = [a_x + 1 * math.cos(step * 3 + 20 * index), a_y + 2 * math.sin(step * 3 + 20 * index)]
                elif line.shake:
                    char_render = self.render(char, line.color)
                    char_pos = [a_x + line.get_shake_amplitude(), a_y + line.get_shake_amplitude()]                    
                else:
                    char_render = self.render(char, line.color)
                    char_pos = [a_x, a_y]

                # Отрисовка
                surface.blit(char_render, (char_pos[0] + line_size[0], char_pos[1] + line_size[1]))
                
                # Обновление ширины строки
                line_size[0] += char_render.get_width()

                # Перенос на новую строку, если ширина строки больше лимита ширины
                if self.width_limit > 0 and line_size[0] > self.width_limit and char == " ":
                    line_size[0] = 0
                    line_size[1] += char_render.get_height()

                # Добавление пробелма в конец строки
                if index == len(line.text) - 1:
                    line_size[0] += self.render(" ").get_width()

                characters += 1
        
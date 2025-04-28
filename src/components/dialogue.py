import math
import copy
import random
import pygame
from typing import List, Tuple
from src.core.utility import lerp
from src.components.line import Line, get_text_from_lines

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

class Dialogue:
    def __init__(self) -> None:
        self.font = pygame.font.Font(None, 24)
        self.antialias = True
        self.width_limit = 280
        self._char_by_char = True

        self._typing_sound: pygame.mixer.Sound = pygame.mixer.Sound("content/sounds/00000e80.wav")
        self._ending_sound: pygame.mixer.Sound = pygame.mixer.Sound("content/sounds/00000ef7.wav")
        self._angry_typing_sound: pygame.mixer.Sound = pygame.mixer.Sound("content/sounds/00000f08.wav")
        self._previous_typing_sound_tick: int = 0

        self._next_line_sprite = pygame.image.load("content/images/next_line.png")
        self._next_line_sprite.set_colorkey("Black")

        self._previos_typing_tick: int = 0
        self._current_text: str = ""
        self._current_lines: List[Line] = []
        self._displayed_lines: List[Line] = []
        self._line_index: int = 0
        self._char_index: int = 0
        self._ending_sound_played: bool = False
        self._text_surface: pygame.Surface = None
        self._text_surface_resized: bool = False

    @property
    def text(self) -> str:
        return get_text_from_lines(self._current_lines)
    
    @property
    def displayed_text(self) -> str:
        return get_text_from_lines(self._displayed_lines)

    @property
    def char_by_char(self) -> bool:
        return self._char_by_char

    @property
    def finished(self) -> bool:
        return self._current_text != "" and self.displayed_text == self._current_text

    @char_by_char.setter
    def char_by_char(self, value: bool) -> None:
        if not value:
            self.skip_typing()
        self._char_by_char = value

    def get_surface_size(self, lines: List[Line]) -> Tuple[int, int]:
        """Возвращает итоговый размер диалогового окна.
        
        Args:
            lines (List[Line]): Список Line.
        
        Returns:
            (width, height) (Tuple[int, int]): Итоговый размер диалогового окна.
        """
        width: int = 0
        height: int = 0
        line_width: int = 0
        line_height: int = 0

        for line in lines:
            for char in line.text:
                char_width, char_height = self.font.size(char)

                line_width += char_width

                width = max(width, line_width)

                if self.width_limit > 0 and line_width > self.width_limit and char == SPACE:
                    line_width = 0
                    line_height += char_height
                    
                height = line_height + char_height
        
        return width + BOX_PADDING[0] * 2, height + BOX_PADDING[1] * 2

    def render_lines(self, lines: List[Line], position: Tuple[int, int], surface: pygame.Surface) -> None:
        """Отрисовывает текст с эффектами на поверхности.
        
        Args:
            lines (List[Line]): Список Line для отрисовки.
            surface (pygame.Surface): Поверхность, на которой будет отрисован текст.
        """
        tick: int = pygame.time.get_ticks()
        text: str = get_text_from_lines(lines)

        if self._current_text != text:
            self._current_text = text
            self._current_lines = lines
            self._displayed_lines.clear()
            self._line_index = 0
            self._char_index = 0
            self._ending_sound_played = False
            self._previos_typing_tick = 0
            self._text_surface_resized = False

            if self._text_surface is None:
                self._text_surface = pygame.Surface([1, 1])
                self._text_surface.fill("#000D2C")

            if not self.char_by_char:
                self.skip_typing()

        line = lines[self._line_index]

        # Плавное изменение размера диалогового окна
        target_size: Tuple[int, int] = self.get_surface_size(lines)
        previous_size: Tuple[int, int] = self._text_surface.get_size()
        if abs(target_size[0] - previous_size[0]) > 1 or abs(target_size[1] - previous_size[1]) > 1:
            new_size: Tuple[int, int] = [lerp(previous_size[0], target_size[0], 0.5), lerp(previous_size[1], target_size[1], 0.5)]
            self._text_surface = pygame.transform.scale(self._text_surface, new_size)
            if self._text_surface_resized:
                self._text_surface_resized = False
        else:
            if not self._text_surface_resized:
                self._text_surface_resized = True

        # Если выведен весь текст, то проиграть звуковой эффект
        if self.finished and not self._ending_sound_played:
            if not self._ending_sound_played:
                self._ending_sound_played = True
                self._ending_sound.play()
                     
        # Посимвольный вывод текста
        if tick - self._previos_typing_tick >= line.typing_speed * MS_IN_SEC and self._text_surface_resized:
            self._previos_typing_tick = tick

            if len(self._displayed_lines) == 0:
                copy_line = copy.deepcopy(line)
                copy_line.text = ""
                self._displayed_lines.append(copy_line)
            
            if self._displayed_lines[self._line_index].text == line.text:
                if self._line_index < len(lines) - 1:
                    self._line_index += 1

                    line = lines[self._line_index]
                    
                    copy_line = copy.deepcopy(line)
                    copy_line.text = ""
                    self._displayed_lines.append(copy_line)

                    self._char_index = 0
                    self._previos_typing_tick = tick + line.pause * MS_IN_SEC
            else:
                if line.angry:
                    self._displayed_lines[self._line_index].text = line.text
                    for _ in line.text:
                        self._displayed_lines[self._line_index]._offsets.append(ANIM_END_OFFSET)
                        self._displayed_lines[self._line_index]._alphas.append(ANIM_END_ALPHA)
                    
                    # Голос
                    self._angry_typing_sound.play()
                else:
                    char = line.text[self._char_index]

                    self._displayed_lines[self._line_index].text += char
                    self._displayed_lines[self._line_index]._offsets.append(ANIM_START_OFFSET)
                    self._displayed_lines[self._line_index]._alphas.append(ANIM_START_ALPHA)
                    self._char_index += 1

                    # Голос
                    if not char in (SPACE, PERIOD) and not line.quiet:
                        if tick - self._previous_typing_sound_tick >= (self._typing_sound.get_length()) * MS_IN_SEC:
                            self._typing_sound.play()
                            self._previous_typing_sound_tick = tick

        # Отрисовка текста
        animation_step = (pygame.time.get_ticks() / 2000.0) * 4.0
        anchor_x: float = position[0] - self._text_surface.get_width() / 2
        anchor_y: float = position[1] - self._text_surface.get_height() - 15
        line_size = [0, 0]

        # Отрисовка окна и указателя
        surface.blit(self._text_surface, (anchor_x, anchor_y))
        pygame.draw.polygon(surface, "#000D2C", [(position[0] - 10, position[1] - 15), (position[0], position[1] - 5), (position[0] + 10, position[1] - 15)])

        # Отрисовка символов текста
        for _, line in enumerate(self._displayed_lines):
            if line.angry and line.shake_amplitude > 0:
                line.shake_amplitude = lerp(line.shake_amplitude, 0, 0.005)
            
            for char_index, char in enumerate(line.text):
                if line._offsets[char_index] > ANIM_END_OFFSET:
                    line._offsets[char_index] -= ANIM_OFFSET_STEP
                if line._alphas[char_index] < ANIM_END_ALPHA:
                    line._alphas[char_index] += ANIM_ALPHA_STEP

                # Отрисовка символа с эффектами
                sector = math.pi / 5
                char_color: pygame.Color
                char_position: Tuple[int, int]

                if line.rgb:
                    hue = (animation_step * 32 + line_size[0] / 4) % 360
                    char_color = pygame.Color.from_hsva(hue, 100, 100)
                elif line.angry: 
                    char_color = pygame.Color("Red")
                elif line.gradient_color:
                    char_color = line.color.lerp(line.gradient_color, (1 + pygame.math.Vector2(0, 1).rotate(pygame.time.get_ticks() / 2000 * 360 + line_size[0]).y) / 2)
                else: 
                    char_color = line.color

                if line.wave:
                    char_position = [anchor_x + BOX_PADDING[0] + 1 * math.cos(animation_step * 3 + sector * char_index), anchor_y + BOX_PADDING[1] + 2 * math.sin(animation_step * 3 + sector * char_index)] 
                elif line.shake:
                    char_position = [anchor_x + BOX_PADDING[0] + get_shake_amount(line.shake_amplitude), anchor_y + BOX_PADDING[1] + get_shake_amount(line.shake_amplitude)]
                elif line.wobble:
                    tick: int = pygame.time.get_ticks()
                    wobble_x: float = math.cos(tick / 75 + char_index) * 1
                    wobble_y: float = math.sin(tick / 50 + char_index) * 1
                    char_position = [anchor_x + BOX_PADDING[0] + wobble_x, anchor_y + BOX_PADDING[1] + wobble_y]
                else:
                    char_position = [anchor_x + BOX_PADDING[0], anchor_y + BOX_PADDING[1]]

                char_render = self.font.render(char, self.antialias, char_color)
                char_render.set_alpha(line._alphas[char_index])

                # Отрисовка
                surface.blit(char_render, (char_position[0] + line_size[0], char_position[1] + line_size[1] - line._offsets[char_index]))

                # Обновление позиционирования
                char_width, char_height = self.font.size(char)

                line_size[0] += char_width

                # Перенос на новую строку, если ширина строки больше лимита ширины
                if self.width_limit > 0 and line_size[0] > self.width_limit and char == SPACE:
                    line_size[0] = 0
                    line_size[1] += char_height               

        # Если всё отрисовано, то отрисовать указатель
        if self.finished:
            pos = (anchor_x + self._text_surface.get_width() + 5, anchor_y + self._text_surface.get_height() / 2)
            surface.blit(self._next_line_sprite, self._next_line_sprite.get_rect(**{"midleft": pos}))

    def skip_typing(self) -> None:
        """Пропуск появления символов, моментальный вывод всего текста."""
        self._previos_typing_tick = 0

        for line_index, line in enumerate(self._current_lines):
            if line_index >= len(self._displayed_lines):
                self._displayed_lines.append(copy.deepcopy(line))

            self._displayed_lines[line_index].text = line.text

            if line.angry:
                self._displayed_lines[line_index].shake_amplitude = 0

            chars_left: int = len(line.text) - len(self._displayed_lines[line_index]._offsets)
            if chars_left > 0:
                self._displayed_lines[line_index]._offsets.extend([ANIM_START_OFFSET] * chars_left)
                self._displayed_lines[line_index]._alphas.extend([ANIM_START_ALPHA] * chars_left)

def get_shake_amount(amplitude: float) -> float:
    return round(random.uniform(-amplitude, amplitude))

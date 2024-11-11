import os
import math
import random
import pygame
from src.components.scene import Scene
from src.components.sprite import Sprite
from src.components.player import Player
from src.components.cursor import Cursor
from src.components.label import Label, FontParams

class Intro(Scene):
    def __init__(self) -> None:
        super().__init__()

        etu_img = pygame.image.load("assets/images/etu_1.png")
        etu_img.set_colorkey("Black")
        self.sprite = Sprite(etu_img, (250, 250), "center")
        self.sprite.add(self.sprites)

        etu_img2 = pygame.image.load("assets/images/etu_0.png")
        etu_img2.set_colorkey("Black")
        self.player = Player(etu_img2, (30, 30), "center")
        self.player.add(self.sprites)

        hand = pygame.image.load("content/images/hand_1.png")
        hand.set_colorkey("Black")
        self.player = Cursor(hand, (0, 0), "topleft")
        self.player.add(self.sprites)       

        self.fontparams = FontParams()
        self.fontparams.size += 10
        self.fontparams.fontpath = os.path.join("content", "fonts", "Ramona-Bold.ttf")
        self.fontparams.color = (255, 0, 200)
        self.fontparams.align = 1
        self.fontparams.wraplength = 0

        self.label = Label("Hello World!", self.fontparams, (100, 100), "center")
        self.label.add(self.sprites)

        self.font = pygame.font.Font(None, 24)
        self._prev_text = None
        self._prev_tags = None

    def renderCharacter(self, char, color):
        return self.font.render(char, True, color)


    def clamp(self, v, _min, _max):
        return max(_min, min(v, _max))

    def parse_text(self, text: str):
        result_text = ""
        result_tags = []
        total_skips = 0
        skips = 0
        
        for index, char in enumerate(text):
            if skips > 0:
                skips -= 1
                continue

            if text[index:index+5] == "[rgb]":
                result_tags.append([index - total_skips, 1])
                skips = 4
                total_skips += 5
                continue
            if text[index:index+7] == "[shake]":
                result_tags.append([index - total_skips, 2])
                skips = 6
                total_skips += 7
                continue
            if text[index:index+3] == "[/]":
                result_tags.append([index - total_skips, 0])
                skips = 2
                total_skips += 3
                continue
            
            result_text += char
            
        return result_text, result_tags

    def renderText(self, text: str, surface: pygame.Surface):
        if self._prev_text is None and self._prev_tags is None:
            self._prev_text, self._prev_tags = self.parse_text(text)
            #print(self._prev_text, self._prev_tags)

        r_size = self.font.size(self._prev_text)
        ix = 640 / 2 - r_size[0] / 2
        iy = 360 / 2 - r_size[1] / 2

        w_acc = 0
        h_acc = 0
        sector = 360 / 64

        step = (pygame.time.get_ticks() / 1000.0) * 4.0

        mode = 0

        for index, char in enumerate(self._prev_text):
            for pos, new_mode in self._prev_tags:
                if index == pos:
                    mode = new_mode

            # Отрисовка на основе выбранного "Режима"
            if mode == 0:
                r_char = self.renderCharacter(char, (0, 0, 0)) 
                x = ix
                y = iy
            elif mode == 1:
                hue = (step * 32 + sector + index) % 360
                r_char = self.renderCharacter(char, pygame.Color.from_hsva(hue, 100, 100))
                x = ix + 1 * math.cos(step + sector * index)
                y = iy + 2 * math.sin(step + sector * index)
            elif mode == 2:
                r_char = self.renderCharacter(char, (255, 0, 20))
                x = ix + random.uniform(-1, 1)
                y = iy + random.uniform(-1, 1)         

            surface.blit(r_char, (x + w_acc, y + h_acc))
            w_acc += r_char.get_size()[0] 
            if w_acc > 2 and char == " ":
                h_acc += r_char.get_size()[1]
                w_acc = 0

    def on_enter(self) -> None:
        pass

    def update(self, delta: float) -> None:
        super().update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((180, 180, 180))
        #self.renderText("Привет, [rgb]а ты кто?[/] Мы [shake]знакомы?[/] [rgb]Чеее...[/] лл.", surface)
        self.renderText("[rgb]Привет![/] У меня всё [rgb]крутяк! [shake]ЧЕЕЕ...[/]", surface)
        super().draw(surface)

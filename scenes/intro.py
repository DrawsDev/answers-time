import os
import random
import pygame
from pygame.math import Vector2
from src.components.scene import Scene
from src.components.sprite import Sprite
from src.components.player import Player
from src.components.cursor import Cursor
from src.components.dialogue import Dialogue, Line
from src.components.label import Label, FontParams

class Intro(Scene):
    def __init__(self) -> None:
        super().__init__()

        etu_img = pygame.image.load("assets/images/etu_1.png")
        etu_img.set_colorkey("Black")
        self.sprite = Sprite(etu_img, (350, 250), "center")
        self.sprite.add(self.sprites)

        etu_img2 = pygame.image.load("assets/images/etu_0.png")
        etu_img2.set_colorkey("Black")
        self.player = Player(etu_img2, (30, 30), "center")
        self.player.add(self.sprites)

        hand = pygame.image.load("content/images/hand_1.png")
        hand.set_colorkey("Black")
        self.cursor = Cursor(hand, (0, 0), "topleft")
        self.cursor.add(self.sprites)       

        self.fontparams = FontParams()
        self.fontparams.size += 10
        self.fontparams.fontpath = os.path.join("content", "fonts", "Ramona-Bold.ttf")
        self.fontparams.color = (255, 0, 200)
        self.fontparams.align = 1
        self.fontparams.wraplength = 0

        self.label = Label("Hello World!", self.fontparams, (100, 100), "center")
        self.label.add(self.sprites)

        self.dialogue = Dialogue()
        self.test_dialogue_pos = Vector2(640 / 2, 360 / 2)
        self.test_dialogue_index = 0
        self.test_dialogue = [
            [Line("Привет!", rgb=True), 
             Line(" Как ", color="White", speed=0.3), 
             Line("дела", color="Lime"), 
             Line("?", color="White", speed=0.5)],

            [Line("Погоди... ", color="Red", speed=0.1), 
             Line("ТЫ... ", angry=True, speed=0, pause=0.5), 
             Line("КТО???", angry=True, shake_amplitude=2, speed=0, pause=0.75)],

            [Line("ЧЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ", rgb=True, speed=0)],

            [Line("Ладно... ", color="White", speed=0.1), 
             Line("ЛАДНО. ", angry=True, pause=0.3), 
             Line("КАК ", angry=True, pause=0.5),
             Line("дела", rgb=True, pause=0.5), 
             Line("?", color="White")],

            [Line("О! ", rgb=True),
             Line("Тут есть некоторые диалоги из ", color="White", pause=1),
             Line("Katana ZERO", color="Cyan", wave=True)],

            [Line("На месте?", color="White")],

            [Line("Такого шанса ", color="Orange", speed=0.02),
             Line("второй раз не будет. ", color="White", speed=0.02),
             Line("Действовать нужно ", color="White", speed=0.02, pause=0.3),
             Line("максимально быстро.", color="Yellow", speed=0.02)],

            [Line("Самое главное. ", color="White"),
             Line("Не ", angry=True, pause=0.5),
             Line("должно ", angry=True, pause=0.2),
             Line("быть ", angry=True, pause=0.45),
             Line("никаких ", angry=True, pause=0.75),
             Line("свидетелей. ", angry=True, pause=0.5)],
            
            [Line("Да, ", color="White"),
             Line("там что-то про ", color="White", pause=0.3),
             Line("заговоры, хунту, такое, ", color="Red", wave=True),
             Line("да?", color="White",  pause=0.3)],

            [Line("Вроде как дело-то серьёзное... ", color="Cyan", shake=True, shake_amplitude=0.55, speed=0.02),
             Line("Может, надо ", color="White", pause=0.3, speed=0.02),
             Line("удвоить патрулирование", color="Orange", speed=0.02),
             Line("?", color="White", speed=0.02)],

            [Line("Да ладно, ", color="White"),
             Line("что может пойти не так?", color="Cyan", pause=0.3)],
            
            [Line("(Если че их потом дакнули :P )", color="#505050", quiet=True, speed=0)],

            [Line("А ", color="White"),
             Line("всё! ", rgb=True),
             Line("Больше ничего не скажу.", color="White", pause=0.5)],
            
            [Line("ы", angry=True)]
        ]

    def update(self, delta: float) -> None:
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_RETURN]:
            finished = self.dialogue.is_typing_finished()
            
            if finished:
                self.test_dialogue_index += 1
                if self.test_dialogue_index > len(self.test_dialogue) - 1:
                    self.test_dialogue_index = 0
            else:
                self.dialogue.skip_typing()

        super().update(delta)

    def draw(self, surface: pygame.Surface) -> None:
        surface.fill((180, 180, 180))

        super().draw(surface)

        self.dialogue.render_lines(self.test_dialogue[self.test_dialogue_index], (self.sprite.position[0], self.sprite.position[1] - self.sprite.image.get_height() / 2), surface)

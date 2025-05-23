import os
import sys
from src.core.game import Game
from content.scenes.menu import Menu
from content.scenes.intro import Intro
from content.scenes.tutorial import Tutorial

if __name__ == "__main__":
    if hasattr(sys, "_MEIPASS"):
        sys.stderr = open(os.path.join(os.getcwd(), "error.log"), "w")
    
    game = Game()
    game.add_scene("Menu", Menu)
    game.add_scene("Intro", Intro)
    game.add_scene("Tutorial", Tutorial)
    game.change_scene("Menu")
    game.run()

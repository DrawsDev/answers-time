import os
import sys
from src.core.game import Game
from content.scenes.menu import Menu
from content.scenes.quiz import Quiz
from content.scenes.editor import Editor
from content.scenes.tutorial import Tutorial

if __name__ == "__main__":
    if hasattr(sys, "_MEIPASS"):
        sys.stderr = open(os.path.join(os.getcwd(), "error.log"), "w")
    
    game = Game()
    game.add_scene("Menu", Menu)
    game.add_scene("Quiz", Quiz)
    game.add_scene("Editor", Editor)
    game.add_scene("Tutorial", Tutorial)
    game.change_scene("Menu")
    game.run()

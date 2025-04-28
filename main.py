from src.core.game import Game
from content.scenes.menu import Menu
from content.scenes.intro import Intro

if __name__ == "__main__":
    game = Game()
    game.add_scene("Menu", Menu)
    game.add_scene("Intro", Intro)
    game.change_scene("Menu")
    game.run()

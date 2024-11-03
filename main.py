from src.core.game import Game
from scenes.intro import Intro

if __name__ == "__main__":
    game = Game()
    game.add_scene("Intro", Intro)
    game.change_scene("Intro")
    game.run()

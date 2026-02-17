from src.core import Application
from src.answerstime import Test

VERSION = "2.0.0.alpha.official"
TITLE = "Answers Time"
WIDTH = 1280
HEIGHT = 720

if __name__ == "__main__":
    application = Application(TITLE, WIDTH, HEIGHT)
    application.version = VERSION
    application.scene.load(Test)
    application.run()

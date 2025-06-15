import os
import sys
from src.framework.application import *
from src.answerstime.scenes import *

if __name__ == "__main__":
    if hasattr(sys, "_MEIPASS"):
        sys.stderr = open(os.path.join(os.getcwd(), "error.log"), "w")
    app = Application()
    app.insert_scene("Menu", Menu)
    app.insert_scene("Quiz", Quiz)
    app.insert_scene("Editor", Editor)
    app.insert_scene("Tutorial", Tutorial)
    app.change_scene("Menu")
    app.run()

from src.core import Scene

class Test(Scene):
    def on_enter(self, **kwargs):
        print("enter")
    
    def on_exit(self):
        print("exit")
    
    def process(self, delta):
        if self.app.keyboard.is_just_pressed("space"):
            print("current delta:", delta)

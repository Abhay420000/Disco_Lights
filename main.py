from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import Clock
from kivy.core.window import Window

import random

Window.fullscreen = True


class ss(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1/10)#10 fps
        Window.size = (1366, 768)
        

    def update(self,*args):
        a = 1/random.randint(1,10)
        b = 1/random.randint(1,10)
        c = 1/random.randint(1,10)

        self.ids.bci.color = (a,b,c)#,d)
    
        
        

class Disco_LightsApp(App):
    pass

if __name__ == "__main__":
    Disco_LightsApp().run()

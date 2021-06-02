from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

class CntossBoxLayout(BoxLayout):
    def choice(self,guess):
        output = "Your choice was: "+guess
        self.ids.result.text=output

class CntossApp(App):
    def build(self):
        return CntossBoxLayout()

if __name__ == "__main__":
    CntossApp().run()
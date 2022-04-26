from kivy.app import App
from kivy.uix.widget import Widget

from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics import Rectangle

class CraneGui(Widget):
    Window.clearcolor = (236, 226, 226, 1)

class CraneApp(App):
    def build(self):
        return CraneGui()

class CraneImage(Image):
    pass

if __name__ == '__main__':
    CraneApp().run()
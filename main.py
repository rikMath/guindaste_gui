from kivy.app import App
from kivy.uix.widget import Widget

from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics import Rectangle

from Modules.GuiInterface.GuiAdapter import GuiAdapterKivy

class CraneGui(Widget):
    Window.clearcolor = (236, 226, 226, 1)

class CraneApp(App):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(self, *args, **kwargs)

    def build(self):
        return CraneGui()

    def move_arm(self):
        adapter = GuiAdapterKivy()
        # degrees_to_move = Achar Graus do input
        adapter.move_arm()

    def clean_arm_input(self):
        ...

class CraneImage(Image):
    pass

if __name__ == '__main__':
    CraneApp().run()

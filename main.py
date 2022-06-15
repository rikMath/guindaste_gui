from kivy.app import App
from kivy.uix.widget import Widget

from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.uix.textinput import TextInput

from kivymd.app import MDApp

from Modules.GuiInterface.GuiAdapter import GuiAdapterKivy

import re

class CraneGui(Widget):
    Window.clearcolor = (236, 226, 226, 1)

class CraneApp(MDApp):

    def build(self):
        self.adapter = GuiAdapterKivy()

        return CraneGui()

    def move_arm(self, root):
        adapter = self.adapter

        try:
            degrees_to_move = round(float(root.ids["input_rotation"].text), 2)
        except:
            # Mensagem de erro
            pass

        adapter.move_arm(degrees_to_move)

    def clean_arm_input(self, root):
        adapter = self.adapter
        adapter.reset_arm_value()
        root.ids["input_rotation"].text = "0"

    def move_hoist(self, root):
        adapter = self.adapter

        try:
            cm_to_move = round(float(root.ids["input_down"].text), 2)
        except:
            # Mensagem de erro
            ...

        adapter.move_hoist(cm_to_move)

    def clean_hoist_input(self, root):
        adapter = self.adapter
        adapter.reset_hoist_value()
        root.ids["input_down"].text = "0"

    def activate_magnet(self):
        self.adapter.activate_magnet()

    def deactivate_magnet(self):
        self.adapter.deactivate_magnet()

class CraneImage(Image):
    pass

class FloatInput(TextInput):

    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat

        if len(self.text) == 0 and substring[0] == "-":
            append_minus = True
            substring = substring[1:]
        else:
            append_minus = False

        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join(
                re.sub(pat, '', s)
                for s in substring.split('.', 1)
            )

        if append_minus:
            s = "-" + s

        return super().insert_text(s, from_undo=from_undo)

if __name__ == '__main__':
    CraneApp().run()

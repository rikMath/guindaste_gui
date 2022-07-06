from kivy.app import App
from kivy.uix.widget import Widget

from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.uix.textinput import TextInput

from kivymd.app import MDApp

from kivy.clock import Clock

import sys

from Modules.GuiInterface.GuiAdapter import GuiAdapterKivy

import re

import logging


class CraneGui(Widget):
    Window.clearcolor = (236, 226, 226, 1)


class CraneApp(MDApp):
    def build(self):
        run_kind = sys.argv[1] if len(sys.argv) > 1 else "Sim"

        self.adapter = GuiAdapterKivy(run_kind, self)

        Clock.schedule_interval(self.update_label, 1)

        return CraneGui()

    def move_arm(self, root):
        adapter = self.adapter

        try:
            degrees_to_move = round(float(root.ids["input_rotation"].text), 2)
        except:
            ...
            # Mensagem de erro

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

    def update_label(self, dt):
        # root = self.crane_app.root

        # new_arm_position = self.crane_simulation.get_arm_angle()
        # new_hoist_position = self.crane_simulation.get_hoist_distance()
        new_sensor_position = self.adapter.get_proximity()

        # root.ids[
        #     "arm_state"
        # ].text = f"Posição Braço: {round(abs(new_arm_position)%360, 2)}"
        # root.ids[
        #     "hoist_state"
        # ].text = f"Posição Lança: {round(abs(new_hoist_position*10), 2)}"
        self.root.ids[
            "sensor_state"
        ].text = f"Posição Sensor: {round(abs(new_sensor_position)*10, 2)}"
        # state = "On" if self.magnet_state else "Off"
        # root.ids["magnet_state"].text = f"Estado Imã: {state}"

        # logging.info(f"Arm -> {new_arm_position} degrees, {root.ids['arm_state'].text}")
        # logging.info(f"Hoist -> {new_arm_position} cm, {root.ids['hoist_state'].text}")
        logging.info(
            f"Sensor -> {new_sensor_position} cm, {self.root.ids['sensor_state'].text}"
        )


class CraneImage(Image):
    pass


class FloatInput(TextInput):

    pat = re.compile("[^0-9]")

    def insert_text(self, substring, from_undo=False):
        pat = self.pat

        if len(self.text) == 0 and substring[0] == "-":
            append_minus = True
            substring = substring[1:]
        else:
            append_minus = False

        if "." in self.text:
            s = re.sub(pat, "", substring)
        else:
            s = ".".join(re.sub(pat, "", s) for s in substring.split(".", 1))

        if append_minus:
            s = "-" + s

        return super().insert_text(s, from_undo=from_undo)


if __name__ == "__main__":
    CraneApp().run()

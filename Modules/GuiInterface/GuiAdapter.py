from Modules.CraneOperation.CraneInterface import CraneInterfaceFacade

class GuiAdapterKivy:
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

    def __init__(self):
        self.crane = CraneInterfaceFacade()
        # Criar Coppelia e Arduino

    def move_arm(self, degrees_to_move):
        self.crane.move_arm(degrees_to_move, "Sim")

    def reset_arm_value(self):
        self.crane.reset_arm("Sim")

    def move_hoist(self, cm_to_move):
        self.crane.move_hoist(cm_to_move, "Sim")

    def reset_hoist_value(self):
        self.crane.reset_hoist("Sim")

    def activate_magnet(self):
        self.crane.activate_magnet("Sim")

    def deactivate_magnet(self):
        self.crane.deactivate_magnet("Sim")

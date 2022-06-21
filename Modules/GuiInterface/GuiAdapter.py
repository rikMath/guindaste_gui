from Modules.CraneOperation.CraneInterface import CraneInterfaceFacade

class GuiAdapterKivy:
    # _instance = None
    # def __new__(class_, *args, **kwargs):
    #     if not isinstance(class_._instance, class_):
    #         class_._instance = object.__new__(class_, *args, **kwargs)
    #     return class_._instance

    def __init__(self, run_kind, crane_app):
        self.run_kind = run_kind

        self.crane = CraneInterfaceFacade(run_kind, crane_app)
        # Criar Coppelia e Arduino

    def move_arm(self, degrees_to_move):
        self.crane.move_arm(degrees_to_move, self.run_kind)

    def reset_arm_value(self):
        self.crane.reset_arm(self.run_kind)

    def move_hoist(self, cm_to_move):
        self.crane.move_hoist(cm_to_move, self.run_kind)

    def reset_hoist_value(self):
        self.crane.reset_hoist(self.run_kind)

    def activate_magnet(self):
        self.crane.activate_magnet(self.run_kind)

    def deactivate_magnet(self):
        self.crane.deactivate_magnet(self.run_kind)

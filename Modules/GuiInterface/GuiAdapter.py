from Modules.CraneOperation.CraneInterface import CraneInterfaceFacade

class GuiAdapterKivy:
    def __new__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super().__new__(cls, *args, **kwargs)

    def __init__(self):
        self.crane = CraneInterfaceFacade()
        # Criar Coppelia e Arduino

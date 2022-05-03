class GuiAdapterToKivy:
    def __new__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super().__new__(cls, *args, **kwargs)

    def __init__(self):
        ...
        # Criar Coppelia e Arduino

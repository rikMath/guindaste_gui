from Modules.CraneOperation.Coppelia import CraneSimulation

class CraneCreator:
    def __init__(self):
        raise NotImplementedError

    @staticmethod
    def create_crane_operation_instance(kind: str):
        if kind == "Coppelia":
            return CraneSimulation()
        elif kind == "Arduino":
            return ...

        raise UserWarning("Tipo Não Existente - Kind deve ser 'Coppelia' ou 'Arduino'")

from Modules.Coppelia.zmqRemoteApi import RemoteAPIClient
import numpy as np


class CoppeliaSimulation:
    try:
        sim = RemoteAPIClient().getObject("sim")
        print("The connection to simulation was established.")
    except:
        print("The connection to simulation could not be established.")

    def start(self):
        self.sim.startSimulation()


class Joint(CoppeliaSimulation):
    def __init__(self, path: str, is_revolution: bool = False):
        self.path = self.set_format(path)
        self.handle = self.sim.getObject(self.path)
        self.is_revolution = is_revolution

    @staticmethod
    def set_format(path: str):
        return "/" + path if not path.startswith("/") else path

    def set_velocity(self, velocity: int):
        if self.is_revolution:
            self.sim.setJointTargetVelocity(self.handle, np.deg2rad(velocity))
        else:
            self.sim.setJointTargetVelocity(self.handle, velocity)

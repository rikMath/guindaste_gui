from shutil import disk_usage
from External.zmqRemoteApi import RemoteAPIClient
import numpy as np

maxPullForce = 3
maxShearForce = 1
maxPeelTorque = 0.1


class CoppeliaSimulation:
    try:
        sim = RemoteAPIClient().getObject("sim")
        print("The connection to simulation was established.")
    except:
        print("The connection to simulation could not be established.")

    def start(self):
        self.sim.startSimulation()

    @staticmethod
    def set_format(path: str):
        return "/" + path if not path.startswith("/") else path


class Joint(CoppeliaSimulation):
    def __init__(self, path: str, is_revolution: bool = False):
        self.path = self.set_format(path)
        self.handle = self.sim.getObject(self.path)
        self.is_revolution = is_revolution

    def set_position(self, new_position):
        print(f"\n\nChanging position: {new_position}\n\n")
        self.sim.setJointTargetPosition(self.handle, new_position)

    def set_velocity(self, velocity: int):
        if self.is_revolution:
            self.sim.setJointTargetVelocity(self.handle, np.deg2rad(velocity))
        else:
            self.sim.setJointTargetVelocity(self.handle, velocity)

    def get_position(self):
        return self.sim.getJointPosition(self.handle)


class Magnet(CoppeliaSimulation):
    def __init__(self, path: str):
        self.path = self.set_format(path)
        self.handle = self.sim.getObject(self.path)

    def actuate(self):
        self.sim.callScriptFunction("sysCall_cleanup", self.sim.scripttype_mainscript)


class Sensor(CoppeliaSimulation):
    def __init__(self, path: str) -> None:
        self.path = self.set_format(path)
        self.handle = self.sim.getObject(self.path)

    def get_proximity(self):
        response = self.sim.checkProximitySensor(self.handle, self.sim.handle_all)
        # response = self.sim.readProximitySensor(self.handle)
        if response:
            return response[1]
        else:
            return np.inf

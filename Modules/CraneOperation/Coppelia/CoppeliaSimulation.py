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

    def set_velocity(self, velocity: int):
        if self.is_revolution:
            self.sim.setJointTargetVelocity(self.handle, np.deg2rad(velocity))
        else:
            self.sim.setJointTargetVelocity(self.handle, velocity)


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
        self.sim.checkProximitySensor(self.handle, self.sim.handle_all)
        return self.sim.readProximitySensor(self.handle)

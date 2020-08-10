import numpy as np

class Point:
    def __init__(self, mass=1, position=(0, 0)):
        self.position = np.array(position)
        self.m = mass
        pass

    def get_force(self, body):
        r = body.position-self.position
        return r*self.m*body.m/(np.linalg.norm(r) ** 3)

    def move(self, vector):
        self.position = self.position + vector

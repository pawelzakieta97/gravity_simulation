import numpy as np

def rotate(vector, angle):
    c, s = np.cos(angle), np.sin(angle)
    R = np.array(((c, -s), (s, c)))
    return np.dot(R, vector)

class Body:
    def __init__(self):
        self.points = {}
        self.position = np.array([0,0])
        self.v = np.array([0,0])
        self.a = 0.0
        self.w = 0.0
        self.m = 1
        self.I = 1

    def add_points(self, *points):
        for point in points:
            self.points[point] = np.array((0,0))
        self.m = 0
        self.I = 0
        self.position = np.array([0, 0])
        for point in self.points.keys():
            self.m += point.m
            self.position += point.position*point.m
        self.position = self.position / self.m
        for point in self.points.keys():
            self.points[point] = point.position-self.position
            self.I += np.linalg.norm(self.points[point])**2*point.m
        if self.I == 0:
            self.I = 1
        self.a = 0

    def move(self, vector):
        self.position += vector
        for point in self.points.keys():
            point.move(vector)

    def rotate(self, angle):
        self.a += angle

    def update_points(self):
        for point in self.points.keys():
            point.position = self.position + rotate(self.points[point], self.a)

    def gravity(self, body, dt=0.1):
        for this_point in self.points:
            force = np.array([0, 0])
            for other_point in body.points:
                force = force + this_point.get_force(other_point)
                self.apply_impulse(force*dt, this_point.position)

    def apply_impulse(self, impulse, location):
        location = np.array(location)
        impulse = np.array(impulse)
        r = location - self.position
        torque = np.cross(r, impulse)
        self.w += torque/self.I
        self.v = self.v + impulse/self.m
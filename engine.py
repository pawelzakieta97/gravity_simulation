from body import Body

class Engine:
    def __init__(self, *bodies):
        self.bodies = []
        for body in bodies:
            self.bodies.append(body)

    def update(self, dt=0.1):
        for body in self.bodies:
            body.move(body.v * dt)
            body.rotate(body.w * dt)
            body.update_points()

    def gravity(self):
        for body in self.bodies:
            for other_body in self.bodies:
                if body == other_body:
                    continue
                body.gravity(other_body, dt=0.1)

import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sub(self, no):
        return Point(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        return Point(self.y * no.z - self.z * no.y,
                     self.z * no.x - self.x * no.z,
                     self.x * no.y - self.y * no.x)

    def absolute(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

def plane_angle(a, b, c, d):
    X = b.sub(a).cross(c.sub(b))
    Y = c.sub(b).cross(d.sub(c))
    angle_cos = X.dot(Y) / (X.absolute() * Y.absolute())
    angle_deg = math.acos(angle_cos) * (180 / math.pi)
    return round(angle_deg, 2)
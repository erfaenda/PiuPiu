class vectorClass:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        return vectorClass(
                self.x * other.x,
                self.y * other.y,
                self.z * other.z)

v1 = vectorClass()
v2 = vectorClass()

v3 = v1 * v2

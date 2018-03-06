class vectorClass:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def __mul__(self, other):
        self.x = self.x * other.x
        self.y = self.y * other.y
        self.z = self.z * other.z

v1 = vectorClass()
v2 = vectorClass()

v3 = v1 * v2

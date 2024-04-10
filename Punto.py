class Punto3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.coordenadas = [x, y, z]

    def __str__(self):
        return f"({self.x}; {self.y}; {self.z})"

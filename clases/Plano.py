import clases.Ecuacion as e
import clases.Vector as v

class Plano:
    def __init__(self, input_str):
        self.ecuacion = e.Ecuacion(input_str)
        self.normal = v.Vector3D(x=self.ecuacion.a, y=self.ecuacion.b, z=self.ecuacion.c)

    def __str__(self):
        return self.ecuacion.__str__()

    def getCoeficientes(self):
        return self.ecuacion.getCoeficientes()

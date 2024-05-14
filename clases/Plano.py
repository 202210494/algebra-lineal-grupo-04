import clases.Ecuacion as e
class Plano:
    def __init__(self, input):
        self.ecuacion = e.Ecuacion(input)

    def __str__(self):
        return self.ecuacion.__str__()
    
    def getCoeficientes(self):
        return self.ecuacion.getCoeficientes()

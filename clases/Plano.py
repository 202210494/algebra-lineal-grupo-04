import clases.Ecuacion # Se importa en referencia al main.py
class Plano:
    def __init__(self, input):
        self.ecuacion = Ecuacion(input)

    def __str__(self):
        return self.ecuacion.__str__()
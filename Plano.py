class Ecuacion:
    def __init__(self, ecuacion_input):
        self.input = ecuacion_input
        coeficientes = self._parsear_ecuacion()

        if coeficientes and len(coeficientes) == 5:
            self.a, self.b, self.c, self.d = coeficientes[:4]
            self.igual = coeficientes[4]

            self.d -= self.igual
            self.igual = 0

    def _parsear_ecuacion(self) -> list[int]:
        terminos = self.input.split("+")
        coeficientes = []

        for termino in terminos:
            valor = self._extraer_coeficientes(termino)

            try:
                coeficientes.append(int(valor))
            except:
                continue

        igual = self._extraer_igualdad(terminos[-1])
        coeficientes.extend(map(int, igual))

        return coeficientes

    def _extraer_coeficientes(self, termino):
                variables = ['x', 'y', 'z']

                for variable in variables:
                    if variable in termino:
                        constante = termino.split(variable)
                        return constante[0].strip()

                return termino.strip() if termino else None

    def _extraer_igualdad(self, termino_igualdad) -> list[int]:
            terminos = termino_igualdad.split("=")
            return [termino.strip() for termino in terminos]

    def __str__(self):
        return f"{self.a}x + {self.b}y + {self.c}z + {self.d} = {self.igual}"

class Plano:
    def __init__(self, input):
        self.ecuacion = Ecuacion(input)

    def __str__(self):
        return self.ecuacion.__str__()

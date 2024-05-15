import re

class Ecuacion:
    def __init__(self, ecuacion_input):
        self.input = ecuacion_input
        resultado_parser = self.__parsear_input(ecuacion_input)

        if resultado_parser and len(resultado_parser) == 5:
            self.a, self.b, self.c, self.d = resultado_parser[:4]
            self.d -= resultado_parser[4]


    def __parsear_input(self, input: str) -> list[float] | None:
        try:
            regex_pattern = r"([-+]?\s*\d+(?:\.\d+)?)\s*x\s*([-+]?\s*\d+(?:\.\d+)?)\s*y\s*([-+]?\s*\d+(?:\.\d+)?)\s*z\s*([-+]?\s*\d+(?:\.\d+)?)\s*=\s*([-+]?\s*\d+(?:\.\d+)?)"

            match = re.match(regex_pattern, input)

            if match:
                a, b, c, d, igual = map(lambda x: float(x.replace(" ", "")), match.groups())
                return [a, b, c, d, igual]
        except:
            raise ValueError("Input invalido.")


    def __str__(self):
        return f"{self.a}x + {self.b}y + {self.c}z + {self.d} = 0"


    def getCoeficientes(self):
        return [self.a, self.b, self.c, self.d]

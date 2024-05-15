import re
import math

class Vector3D:
    def __init__(
        self,
        input_str: str | None = None,
        i: float | None = None,
        j: float | None = None,
        k: float | None = None
    ):
        if i is not None and j is not None and k is not None:
            self.coordenadas = [i, j, k]
            self.i, self.j, self.k = self.coordenadas

        elif input_str:
            resultado_parser = self.__parsear_input(input_str)

            if resultado_parser and len(resultado_parser) == 3:
                self.coordenadas = resultado_parser
                self.i, self.j, self.k = self.coordenadas

                self.magnitud = math.sqrt(pow(self.i, 2) + pow(self.j, 2) + pow(self.k, 2))

        else:
            raise ValueError("Input o valores de (x; y; z) no proporcionados.")



    def __parsear_input(self, input: str) -> list[float] | None:
        try:
            regex_pattern = r"[(<]?\s*([-+]?\s*\d+(?:\.\d+)?)[,;\s]+([-+]?\s*\d+(?:\.\d+)?)[,;\s]+([-+]?\s*\d+(?:\.\d+)?)\s*[>)]?"
            match = re.match(regex_pattern, input)

            if match:
                x, y, z = map(lambda x: float(x.replace(" ", "")), match.groups())
                return [x, y, z]

        except:
            raise ValueError("Input invalido.")


    def __str__(self):
        return f"<{self.i}; {self.j}; {self.k}>"

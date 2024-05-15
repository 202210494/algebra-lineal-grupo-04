import re

class Vector3D:
    def __init__(
        self,
        input_str: str | None = None,
        x: float | None = None,
        y: float | None = None,
        z: float | None = None
    ):
        if x is not None and y is not None and z is not None:
            self.coordenadas = [x, y, z]
            self.x, self.y, self.z = self.coordenadas

        elif input_str:
            resultado_parser = self.__parsear_input(input_str)

            if resultado_parser and len(resultado_parser) == 3:
                self.coordenadas = resultado_parser
                self.x, self.y, self.z = self.coordenadas

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
        return f"<{self.x}; {self.y}; {self.z}>"

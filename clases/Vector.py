import re

class Vector3D:
    def __init__(self, input):
        resultado_parser = self.__parsear_input(input)

        if resultado_parser:
            self.coordenadas = resultado_parser
            self.x, self.y, self.z = self.coordenadas



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

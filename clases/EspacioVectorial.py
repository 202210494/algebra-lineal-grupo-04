'''
Primero, debemos definir qué es la base de un espacio vectorial. 
Según Campos (s.f.), una base de un espacio o subespacio vectorial 
es un conjunto linealmente independiente y que sirve de generador de este mismo, 
puesto que gracias a este podemos expresar todos sus vectores como una combinación lineal de la base. 

'''

class EspacioVectorial:
    def __init__(self, base):
        self.base = base
        self.dimension = len(base) # La dimensión de un espacio vectorial es el número de elementos de su base
        self.vectores = [] # Vectores generados a partir de la base



    # Producto cartesiano de la base
    def generar_vectores(self): # Posibles mejoras marcianas: https://stackoverflow.com/questions/11144513/cartesian-product-of-multiple-lists
        for i in range(self.dimension):
            for j in range(self.dimension):
                for k in range(self.dimension):
                    self.vectores.append([i, j, k])

    # encapsulaciones 
    def __str__(self):
        return f"Base: {self.base}\nVectores: {self.vectores}\nDimensión: {self.dimension}"

    def __contains__(self, vector):
        return vector in self.vectores

    def __getitem__(self, index):
        return self.vectores[index]
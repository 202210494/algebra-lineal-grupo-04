import numpy as np

class Punto:
    def __init__(self, P):
        self.P = P

    def dibujar(self, ax, color='yellow', size=10):
        ax.scatter(self.P[0], self.P[1], self.P[2], c=color, s=size)
        ax.text(self.P[0], self.P[1], self.P[3], f'P ({round(self.P[0],2)}, {round(self.P[1],2)}, {round(self.P[2],2)})', 
                fontsize=8, ha='center', va='bottom', color='black')

class Vector:
    # Recibe dos puntos np 
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

    def to_numpy(self):
        return self.fin - self.inicio
    

    def dibujar(self, ax, color='purple', arrow_length_ratio=0.1):
        vec = self.to_numpy()
        ax.quiver(self.inicio.P[0], self.inicio.P[1], self.inicio.P[2], vec[0], vec[1], vec[2], 
                  color=color, arrow_length_ratio=arrow_length_ratio)
import numpy as np



class Punto:
    def __init__(self, P):
        self.P = P
        self.matriz_rotacion = None

    def to_numpy(self):
        return self.P
    
    def parsed_point(self):
        return "(" + ", ".join([str(round(x, 2)) for x in self.P]) + ")"

    def dibujar(self, ax, color='yellow', size=18):
        ax.scatter(self.P[0], self.P[1], self.P[2], c=color, s=size)
        ax.text(self.P[0], self.P[1], self.P[2], f'P ({round(self.P[0],2)}, {round(self.P[1],2)}, {round(self.P[2],2)})', 
                fontsize=8, ha='center', va='bottom', color='black')
       

        

class Vector:
    # Recibe dos puntos np 
    def __init__(self, inicio, fin):
        self.inicio = inicio.P
        self.fin = fin.P
        self.matriz_escalamiento = None

    def to_numpy(self): # vector como mates
        return self.fin - self.inicio 
    
    def parsed_vector(self):
        return "<" + ", ".join([str(round(x, 2)) for x in self.to_numpy()]) + ">"

    def dibujar(self, ax, color='purple', arrow_length_ratio=0.01):
        vec = self.to_numpy()
        ax.quiver(self.inicio[0], self.inicio[1], self.inicio[2], vec[0], vec[1], vec[2], 
                  color=color, arrow_length_ratio=arrow_length_ratio)
        
    def dibujar(self, ax, color='purple', arrow_length_ratio=0.01, frame =0, f_inicio = 0, f_dur = 0):
        
        vec = self.to_numpy()
        
        # Escalamiento del vector en el tiempo
        if(self.matriz_escalamiento is None):
            self.matriz_escalamiento = np.linspace(0, 1, f_dur)

        if (frame < f_inicio + f_dur):
            vec = vec * self.matriz_escalamiento[frame - f_inicio]

        # Dibujar vector (escalado o no)  
        ax.quiver(self.inicio[0], self.inicio[1], self.inicio[2], vec[0], vec[1], vec[2], 
                  color=color, arrow_length_ratio=arrow_length_ratio)
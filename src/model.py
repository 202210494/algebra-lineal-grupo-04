import numpy as np
from mates import Punto, Vector

class ProyeccionModel:
    def __init__(self):
        self.puntos = {}
        self.vectores = {}
    
    # TODO Pasar a las clases
    def parsed_vector(self, vector):
        return "<" + ", ".join([str(round(x, 2)) for x in vector]) + ">"
    
    def parsed_point(self, point):
        return "(" + ", ".join([str(round(x, 2)) for x in point]) + ")"


    def describir_proyeccion(self, PL_M):
        # Descripcion del proceso (para interpretar el grafico)
        desc = ''

        desc += ("Ecuacion del plano:\n")
        desc += ("------------------\n")
        desc += (f"{PL_M[0]}x + {PL_M[1]}y + {PL_M[2]}z + {PL_M[3]} = 0\n")

        desc += (f"Punto a proyectar:\n")
        desc += ("------------------\n")
        desc += (self.parsed_point(self.puntos["P"]) + "\n")

        desc += ("1. Hallar vector u (P-P0):\n")
        desc += ("-----------------------------\n")
        desc += ("Hallaremos el vector u (P-P0) , donde P es el punto a proyectar y P0 es el punto de origen del plano\n\n")
        desc += ("\n\n")
        desc += ('1.a.Punto origen en el plano:\n')
        desc += ("-----------------------------\n")
        desc += ("Para hallar P0 tendremos que hallar el corte del plano con el eje z, x = 0, y = 0\n")
        desc += ("en este caso:\n")
        desc += (f"x = 0, y = 0, z = -d/c = -{PL_M[3]}/{PL_M[2]} = {round(self.puntos["P_0"][2],2)}\n\n")
        desc += (f"Punto origen en el plano: \n" + self.parsed_point(self.puntos["P_0"]) + "\n\n")
        desc += ("\n\n\n")
        desc += ('1.b.Vector u (P-P0):\n')
        desc += ("---------------------\n")
        desc += ("Para hallar el vector u (P-P0) solo calculamos el vector que va de P a P0\n\n")
        desc += ("en este caso:\n")
        desc += (f"<P-P0> = P - P0 = {self.parsed_point(self.puntos["P"])} - {self.parsed_point(self.puntos["P_0"])} =",
               f"{self.parsed_vector(self.vectores["u"][3:])}\n\n")
        desc += ("\n\n\n")
        desc += ("2. Hallar vector n (normal al plano):\n")
        desc += ("--------------------------------------\n")
        desc += ("ya que el vector n es paralelo a la proyeccion, \n")
        desc += ("simplemente tomamos los coeficientes del plano y los normalizamos\n\n")
        desc += ("en este caso:\n")
        desc += (f"Plano: {PL_M[0]}x + {PL_M[1]}y + {PL_M[2]}z + {PL_M[3]} = 0\n")
        desc += (f"Vector n = <{PL_M[0]}, {PL_M[1]}, {PL_M[2]}> / ||n||\n")
        desc += (f"||n|| = sqrt({PL_M[0]}^2 + {PL_M[1]}^2 + {PL_M[2]}^2)", 
              f"= {round(np.linalg.norm(self.vectores["n"][3:]), 2)}\n\n")
        desc += (f"Vector n (normal al plano): \n{self.parsed_vector(self.vectores["n"][3:])}\n\n")
        desc += ("\n\n\n")
        desc += ("3. Hallar vector P-P' [proyeccion ortogonal]:\n")
        desc += ("---------------------------------------------\n")
        desc += ("Para hallar el vector P-P' (proyeccion ortogonal) proyectamos el vector u sobre el vector n\n\n")
        desc += ("en este caso:\n")
        desc += (f"P-P' = (u . n / ||n||^2) * -n = (",
              f"{self.parsed_vector(self.vectores["u"][3:])} . {self.parsed_vector(self.vectores["n"][3:])} /", 
              f"||{self.parsed_vector(self.vectores["n"][3:])}||^2) * {self.parsed_vector(-self.vectores["n"][3:])}",
               f" = {self.parsed_vector(self.vectores["proy_n_u"][3:])}\n") 
        desc += ("\n\n\n")
        desc += ("4. Hallar punto proyectado P':\n")
        desc += ("------------------------------\n")
        desc += ("Para hallar el punto proyectado P' nos moveremos P_P` desde P\n\n")
        desc += (f"P = P + P-P' = {self.parsed_point(self.puntos["P"])} +", 
              f"{self.parsed_vector(self.vectores["proy_n_u"][3:])} = {self.puntos["P_"]}\n\n")
        desc += (f"Punto proyectado: \n{self.parsed_point(self.puntos["P"])}\n\n")
        desc += ("En la animacion puedes ver como se proyecta el punto P sobre el plano\n")
        return desc

    '''
    Logica del m para calcular la proyeccion de un punto sobre un plano
    nos devuelve el plano, los vectores y los puntos
    '''
    def calcular_proyeccion(self, P_P, PL_M):

        self.puntos["P"] = P_P # punto a proyectar
        P_P0 = np.array([0, 0, -1 * PL_M[3] / PL_M[2]]) # punto de origen del plano
        self.puntos["P_0"] = P_P0 

        # hallar vector P-P0 (u)
        vec_u = P_P0 - P_P # vector P-P0 (u)
        self.vectores["u"] = np.concatenate([P_P, vec_u])

        # hallar vector normal del plano N (n), paralelo a la proyeccion
        vec_n = PL_M[:3]
        vec_n / np.linalg.norm(vec_n)
        self.vectores["n"] = np.concatenate([P_P0, vec_n ])
        self.vectores["-n"] = np.concatenate([P_P0, -vec_n ])   
        
        # hallar vector P-P'(proy_n_u) [proyeccion ortogonal]
        proy_n_u = np.dot(vec_u, -vec_n) / np.linalg.norm(-vec_n) ** 2 * -vec_n
        self.vectores["proy_n_u"] = np.concatenate([P_P, proy_n_u])
        # hallar punto proyectado P'
        P_P_ = P_P + proy_n_u
        self.puntos["P_"] = P_P_
        
        # mandamos el plano, los vectores y los puntos
        return PL_M, self.vectores, self.puntos 


    def rotar_punto(self, punto, rotacion):

        Rx = np.array([[1, 0, 0],
                       [0, np.cos(rotacion[0]), -np.sin(rotacion[0])], 
                       [0, np.sin(rotacion[0]), np.cos(rotacion[0])]])
        
        Ry = np.array([[np.cos(rotacion[1]), 0, np.sin(rotacion[1])],
                       [0, 1, 0],
                       [-np.sin(rotacion[1]), 0, np.cos(rotacion[1])]])
        
        Rz = np.array([[np.cos(rotacion[2]), -np.sin(rotacion[2]), 0],
                       [np.sin(rotacion[2]), np.cos(rotacion[2]), 0],
                       [0, 0, 1]])
        
        R = np.dot(Rz, np.dot(Ry, Rx)) # Rotamos en x, luego en y luego en z

        return np.dot(R, punto) # Devolvemos el punto rotado en los 3 ejes

    def calc_con_rotacion(self, P_P, PL_M, rotacion):
        # Rotamos el punto inicial y lo guardamos como punto a proyectar
        self.puntos["P"] = self.rotar_punto(P_P, rotacion)

        self.puntos["P_Rotar"] = P_P

        # calculamos la proyeccion desde el nuevo punto 
        self.calcular_proyeccion(self.puntos["P"], PL_M)
       
        desc = '' 

        desc += ("Rotacion en rad del punto a proyectar:\n")
        desc += ("------------------------------\n")
        desc += (f"Rotacion en X: {rotacion[0]}\n")
        desc += (f"Rotacion en Y: {rotacion[1]}\n")
        desc += (f"Rotacion en Z: {rotacion[2]}\n\n")
        desc += (f"Punto ha rotar: {self.parsed_point(P_P)}\n")
        desc += (f"Punto proyectado rotado: \n{self.parsed_point(self.puntos['P'])}\n")
        
        desc += self.describir_proyeccion(PL_M)
        print(desc)
        #desc += ("En la animacion puedes ver como se proyecta el punto P sobre el plano y luego se rota\n")

        return PL_M, self.vectores, self.puntos

    def calc_max_v(self):
        m_s = 0
        for v in self.vectores.values():
            c_s = np.sqrt(v[3]**2 + v[4]**2 + v[5]**2) # get modulo
            if(c_s > m_s):
                m_s = c_s

        return m_s


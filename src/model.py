import numpy as np

class ProyeccionModel:
    def __init__(self):
        self.puntos = {}
        self.vectores = {}
    
    def parsed_vector(self, vector):
        return "<" + ", ".join([str(round(x, 2)) for x in vector]) + ">"
    
    def parsed_point(self, point):
        return "(" + ", ".join([str(round(x, 2)) for x in point]) + ")"


    def describir_proyeccion(self, PL_M):
        # Descripcion del proceso (para interpretar el grafico)
        print("Ecuacion del plano:")
        print("------------------")
        print(f"{PL_M[0]}x + {PL_M[1]}y + {PL_M[2]}z + {PL_M[3]} = 0\n")

        print(f"Punto a proyectar:")
        print("------------------")
        print(self.parsed_point(self.puntos["P"]) + "\n")

        print("1. Hallar vector u (P-P0):")
        print("-----------------------------")
        print("Hallaremos el vector u (P-P0) , donde P es el punto a proyectar y P0 es el punto de origen del plano\n")
        print("\n")
        print('1.a.Punto origen en el plano:')
        print("-----------------------------")
        print("Para hallar P0 tendremos que hallar el corte del plano con el eje z, x = 0, y = 0")
        print("en este caso:")
        print(f"x = 0, y = 0, z = -d/c = -{PL_M[3]}/{PL_M[2]} = {round(self.puntos["P_0"][2],2)}\n")
        print(f"Punto origen en el plano: \n" + self.parsed_point(self.puntos["P_0"]) + "\n")
        print("\n\n")
        print('1.b.Vector u (P-P0):')
        print("---------------------")
        print("Para hallar el vector u (P-P0) solo calculamos el vector que va de P a P0\n")
        print("en este caso:")
        print(f"<P-P0> = P - P0 = {self.parsed_point(self.puntos["P"])} - {self.parsed_point(self.puntos["P_0"])} =",
               f"{self.parsed_vector(self.vectores["u"][3:])}\n")
        print("\n\n")
        print("2. Hallar vector n (normal al plano):")
        print("--------------------------------------")
        print("ya que el vector n es paralelo a la proyeccion, ")
        print("simplemente tomamos los coeficientes del plano y los normalizamos\n")
        print("en este caso:")
        print(f"Plano: {PL_M[0]}x + {PL_M[1]}y + {PL_M[2]}z + {PL_M[3]} = 0")
        print(f"Vector n = <{PL_M[0]}, {PL_M[1]}, {PL_M[2]}> / ||n||")
        print(f"||n|| = sqrt({PL_M[0]}^2 + {PL_M[1]}^2 + {PL_M[2]}^2)", 
              f"= {round(np.linalg.norm(self.vectores["n"][3:]), 2)}\n")
        print(f"Vector n (normal al plano): \n{self.parsed_vector(self.vectores["n"][3:])}\n")
        print("\n\n")
        print("3. Hallar vector P-P' [proyeccion ortogonal]:")
        print("---------------------------------------------")
        print("Para hallar el vector P-P' (proyeccion ortogonal) proyectamos el vector u sobre el vector n\n")
        print("en este caso:")
        print(f"P-P' = (u . n / ||n||^2) * -n = (",
              f"{self.parsed_vector(self.vectores["u"][3:])} . {self.parsed_vector(self.vectores["n"][3:])} /", 
              f"||{self.parsed_vector(self.vectores["n"][3:])}||^2) * {self.parsed_vector(-self.vectores["n"][3:])}",
               f" = {self.parsed_vector(self.vectores["proy_n_u"][3:])}\n") 
        print("\n\n")
        print("4. Hallar punto proyectado P':")
        print("------------------------------")
        print("Para hallar el punto proyectado P' nos moveremos P_P` desde P\n")
        print(f"P = P + P-P' = {self.parsed_point(self.puntos["P"])} +", 
              f"{self.parsed_vector(self.vectores["proy_n_u"][3:])} = {self.puntos["P_"]}\n")
        print(f"Punto proyectado: \n{self.parsed_point(self.puntos["P"])}\n")
        print("En la animacion puedes ver como se proyecta el punto P sobre el plano\n")

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

        self.describir_proyeccion(PL_M)
        
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
        # calculamos la proyeccion
        PL_M, vectores, puntos = self.calcular_proyeccion(P_P, PL_M)
        # rotamos el punto proyectado
        puntos["P_r"] = self.rotar_punto(puntos["P_"], rotacion)
        print("Rotacion del punto proyectado:")
        print("------------------------------")
        print(f"Rotacion en X: {rotacion[0]}")
        print(f"Rotacion en Y: {rotacion[1]}")
        print(f"Rotacion en Z: {rotacion[2]}\n")
        print(f"Punto proyectado rotado: \n{self.parsed_point(puntos['P_r'])}\n")
        #print("En la animacion puedes ver como se proyecta el punto P sobre el plano y luego se rota\n")

        return PL_M, vectores, puntos


import numpy as np

class ProyeccionModel:
    def __init__(self):
        self.puntos = {}
        self.vectores = {}
    

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
        vec_n = PL_M[:3]

        # hallar vector normal del plano N (n), paralelo a la proyeccion
        self.vectores["n"] = np.concatenate([P_P0, vec_n / np.linalg.norm(vec_n)])
        self.vectores["-n"] = np.concatenate([P_P0, -vec_n / np.linalg.norm(vec_n)])
        
        # hallar vector P-P'(proy_n_u) [proyeccion ortogonal]
        proy_n_u = np.dot(vec_u, -vec_n) / np.linalg.norm(-vec_n) ** 2 * -vec_n
        self.vectores["proy_n_u"] = np.concatenate([P_P, proy_n_u])
        # hallar punto proyectado P'
        P_P_ = P_P + proy_n_u
        self.puntos["P_"] = P_P_

        # mandamos el plano, los vectores y los puntos
        return PL_M, self.vectores, self.puntos 

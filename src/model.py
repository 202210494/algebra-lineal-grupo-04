import numpy as np

class ProyeccionModel:
    def __init__(self):
        self.puntos = {}
        self.vectores = {}
    
    def calcular_proyeccion(self, P_P, PL_M):
        self.puntos["P"] = P_P
        P_P0 = np.array([0, 0, -1 * PL_M[3] / PL_M[2]])
        self.puntos["P_0"] = P_P0
        vec_u = P_P0 - P_P
        self.vectores["u"] = np.concatenate([P_P, vec_u])
        vec_n = PL_M[:3]
        self.vectores["n"] = np.concatenate([P_P0, vec_n / np.linalg.norm(vec_n)])
        self.vectores["-n"] = np.concatenate([P_P0, -vec_n / np.linalg.norm(vec_n)])
        proy_n_u = np.dot(vec_u, -vec_n) / np.linalg.norm(-vec_n) ** 2 * -vec_n
        self.vectores["proy_n_u"] = np.concatenate([P_P, proy_n_u])
        P_P_ = P_P + proy_n_u
        self.puntos["P_"] = P_P_
        
        return PL_M, self.vectores, self.puntos

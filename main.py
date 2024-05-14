import numpy as np
import matplotlib.pyplot as plt

def main():
    # get punto a proyectar P (x, y, z)
    P_P = np.array([-1, 2, 0])
    print("Punto a proyectar:\n", P_P)

    # get plano donde se proyectará el punto PL_M (ax + by + cz + d = 0)
    PL_M = np.array([2, -3, 1, 2])
    print("Plano donde se proyectará el punto:\n", PL_M)

    # calcular proyeccion ortogonal
       # calcular punto de origen del plano P0 (interseccion con el eje z)
         # cz + d = 0 -> z = -d/c -> P0 = (0, 0, -d/c)
 
    P_P0 = np.array([0, 0, -PL_M[3]/PL_M[2]])  # TODO: MATEMATIZAR  
    print("Punto de origen del plano:\n", P_P0)
    
       # calcular vector P-P0 (u)
    vec_u = P_P0 - P_P
    print("Vector u:\n", vec_u)
       # calular vector normal del plano N (n) 
    vec_n = PL_M[:3]
    print("Vector n:\n", vec_n)
        # vector P-P'(proy_n_u)
    proy_n_u = np.dot(vec_u, -vec_n)/ np.linalg.norm(-vec_n)**2 * -vec_n
    print("Vector proyeccion ortogonal:\n", proy_n_u)
       # calcular punto proyectado P'
       # P' = P + proy_n_u
    P_P_ = P_P + proy_n_u

    # mostrar resultado
    print("Punto proyectado:\n", P_P_) 

    

# Si no se coloca el __name__ = "__main__", te ejecutas todos los .py importados      
if __name__ == "__main__":
    main()



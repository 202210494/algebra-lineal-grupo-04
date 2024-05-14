import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


def graficar(plano, vectores, puntos):
    fig = plt.figure() #creamos el figure
    ax = fig.add_subplot(111, projection="3d") #de tipo 3d!

    X, Y = np.meshgrid(np.linspace(-5, 5), np.linspace(-5, 5)) #creacion del meshgrid (rango de valores que tomaran X e Y)
   
    # graficar plano
    Z = -(plano[0]*X + plano[1]*Y + plano[3])/plano[2]  #aca simplemente igualamos Z igual a la funcion
    ax.plot_surface(X, Y, Z, color="yellow", alpha=0.5) #creamos la superficie del plano
    
    # graficar puntos y vectores
    for tag, punto in puntos.items():
        ax.scatter(punto[0], punto[1], punto[2], c='blue', s=10, label = tag) #colocamos los puntos en el grafico
    for tag, vector in vectores.items():
        if (tag == "n" or tag == "-n"):
            color = "orange"
        elif (tag == "proy_n_u"):
            color = "green"
        else:
            color = "purple"

        ax.quiver(vector[0], vector[1], vector[2],                  #origen x, origen y, origen z
                    vector[3], vector[4], vector[5],
                    color=color,  
                     arrow_length_ratio=0)    #destino x, destino y, destino z

    plt.show()




def main():
   
    puntos = {}
    vectores = {}

    # get punto a proyectar P (x, y, z)
    P_P = np.array([-1, 2, 0])
    puntos["P"] = P_P
    print("Punto a proyectar:\n", P_P)
    
    # get plano donde se proyectará el punto PL_M (ax + by + cz + d = 0)
    PL_M = np.array([2, -3, 1, 2])
    print("Plano donde se proyectará el punto:\n", PL_M)

    # calcular proyeccion ortogonal
       # calcular punto de origen del plano P0 (interseccion con el eje z)
         # cz + d = 0 -> z = -d/c -> P0 = (0, 0, -d/c)
 
    P_P0 = np.array([0, 0, -1 * PL_M[3]/PL_M[2]])  # TODO: MATEMATIZAR  
    print("Punto de origen del plano:\n", P_P0)
    puntos["P_0"] = P_P0
    
       # calcular vector P-P0 (u)
    vec_u = P_P0 - P_P
    vectores["u"] = np.concatenate([P_P, vec_u])

    print("Vector u:\n", vec_u)
       # calular vector normal del plano N (n) 
    vec_n = PL_M[:3]
    vectores["n"] = np.concatenate([P_P0, vec_n / np.linalg.norm(vec_n)])
    vectores["-n"] = np.concatenate([P_P0, -vec_n/ np.linalg.norm(vec_n)])

    print("Vector n:\n", vec_n)
        # vector P-P'(proy_n_u)
    proy_n_u = np.dot(vec_u, -vec_n)/ np.linalg.norm(-vec_n)**2 * -vec_n
    vectores["proy_n_u"] = np.concatenate([P_P, proy_n_u])

    print("Vector proyeccion ortogonal:\n", proy_n_u)
       # calcular punto proyectado P'
       # P' = P + proy_n_u
    P_P_ = P_P + proy_n_u
    puntos["P_"] = P_P_

    # mostrar resultado
    print("Punto proyectado:\n", P_P_) 

    graficar(plano=PL_M, vectores=vectores, puntos=puntos)

    

# Si no se coloca el __name__ = "__main__", te ejecutas todos los .py importados      
if __name__ == "__main__":
    main()



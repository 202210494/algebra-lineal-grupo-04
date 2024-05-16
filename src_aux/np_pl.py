import numpy as np
import matplotlib.pyplot as plt    


def vectores():
    matriz =np.array([[2,2,2],[6,2,6],[7,2,9]])
    vector =np.array([1,2,3])
    print(vector)
    print('Matriz', matriz)
    #plt.imshow(matriz, interpolation='nearest')
    #plt.show()
    print(vector.shape)
    print(matriz.shape)

def graficar():

    x = np.arange(-5,6) # dominio
    print(x)	
    y_1 = 3*x + 5 # rango
    y_2 = 2*x + 3 # rango
    print(y_1)

    plt.figure() # crea una figura (ventana)
    plt.plot(x, y_1) # grafica f(x) = 3x + 5 en el intervalo [-5,5]
    plt.plot(x, y_2) # grafica f(x) = 2x + 3 en el intervalo [-5,5]

    plt.xlim(-5,5) # limita el eje x de -5 a 5 (intervalo de graficación (ilusion))
    plt.ylim(-5,5)

    # coords ejes
    plt.axvline(x=0, color='grey') 
    plt.axhline(y=0, color='grey') 

    plt.show() # no olvidar MOSTRAR la ventana

def sistema_ecuaciones():
    ig = np.array([1,0]) # vector independiente
    coe = np.array([[3,1],[1,2]]) # matriz de coeficientes

    solv = np.linalg.solve(coe, ig) # resuelve el sistema de ecuaciones

    print(solv) # solucion 


def graficar_vectores(vecs, colors, alpha=1):
    # Accisas
    plt.figure()
    plt.axvline(x=0, color='grey', zorder=0)
    plt.axhline(y=0, color='grey', zorder=0)

    # Graficar vectores
    for i in range(len(vecs)):
        x = np.concatenate([[0,0], vecs[i]])
        plt.quiver([x[0]], # origen x
                   [x[1]], # origen y
                   [x[2]], # destino x
                   [x[3]], # destino y
                   angles='xy', scale_units='xy', scale=1, color=colors[i],
                   alpha=alpha)



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def graficar(plano, vectores, puntos):
    fig = plt.figure()  # creamos el figure
    ax = fig.add_subplot(111, projection="3d")  # de tipo 3d!

    X, Y = np.meshgrid(np.linspace(-5, 5), np.linspace(-5, 5))  # creacion del meshgrid (rango de valores que tomaran X e Y)

    # graficar plano
    Z = -(plano[0]*X + plano[1]*Y + plano[3])/plano[2]  # aca simplemente igualamos Z igual a la funcion
    ax.plot_surface(X, Y, Z, color="yellow", alpha=0.5)  # creamos la superficie del plano

    # graficar puntos y vectores
    for tag, punto in puntos.items():
        ax.scatter(punto[0], punto[1], punto[2], c='blue', s=10, label=tag)  # colocamos los puntos en el grafico

    for tag, vector in vectores.items():
        if (tag == "n" or tag == "-n"):
            color = "orange"
        elif (tag == "proy_n_u"):
            color = "green"
        else:
            color = "purple"

        # Suponiendo que vector es un array de 6 elementos [x_orig, y_orig, z_orig, x_dest, y_dest, z_dest]
        ax.quiver(vector[0], vector[1], vector[2],  # origen x, origen y, origen z
                  vector[3], vector[4], vector[5],  # destino x, destino y, destino z
                  color=color, arrow_length_ratio=0)  # sin flecha

    plt.show()

plano = [2, -3, 1, 2]
vectores = {'v1': [1, 2, 3, 4, 5, 6]}  # Ejemplo de vector con origen y destino
puntos = {'p1': [1, 2, 3], 'p2': [4, 5, 6]}  # Ejemplo de punto

graficar(plano, vectores, puntos)
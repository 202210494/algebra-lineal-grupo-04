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

    plt.xlim(-1,60)
    plt.ylim(-1,60)
    plt.show()

v1 = np.array([2,5])
v2 = np.array([3,2])

cmbl = 2 * v1 + 1 * v2

graficar_vectores([v1,v2, cmbl], ['green','orange', 'purple'])
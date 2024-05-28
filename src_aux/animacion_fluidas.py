# TODO 
# 1 Animar vector
# que textos van a ir
# agregar explicacion en .md
# agregar descripcion en latex


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from mates import Vector, Punto


def animar(plano, vectores, puntos, size):
    plt.style.use("tableau-colorblind10")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    X, Y = np.meshgrid(np.linspace(-size, size), np.linspace(-size, size))
    Z = -(plano[0] * X + plano[1] * Y + plano[3]) / plano[2] # Ecuacion del plano (tomamos z como la variable dependiente)

    ax.plot_surface(X, Y, Z, color="yellow", alpha=0.5)

    def _update_proyeccion(frame):

                ax.clear()
                ax.plot_surface(X, Y, Z, color="yellow", alpha=0.5)

                ### parte debil (en proceso) ###
                vecs = {
                     "n" : (20,"red")
                }
                points = {
                        "P" : (0, "blue"),
                        "P_" : (20, "orange")
                    }
                
                for key, v in points.items():
                    if frame >= v[0]:
                        punto = puntos[key]
                        punto.dibujar(ax, color=v[1])
                        print(frame)

                for key, v in vecs.items():
                    
                    np.linspace(0,1, 99)
                    if frame >= v[0]:
                        vector = vectores[key]
                        vector.dibujar(ax, color=v[1])
                        print(frame)

                

    ax.set_xlim([-size, size])
    ax.set_ylim([-size, size])
    ax.set_zlim([-size, size])
                
    sep = 2
    ext_int = 2

    ani = FuncAnimation(fig, _update_proyeccion, frames=range(200), interval=100)
    plt.show()


plano = np.array([1,2,3,4])
vectores = {}
puntos = {}

size = 5

puntos["P"] = Punto(np.array([1,2,3]))
puntos["P_"] = Punto(np.array([4,5,6]))
vectores["n"] = Vector(puntos["P"], puntos["P_"])

animar(plano, vectores, puntos, size)


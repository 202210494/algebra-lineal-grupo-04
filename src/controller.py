from model import ProyeccionModel
from view import ProyeccionView
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

class ProyeccionController:
    def __init__(self, root):
        self.model = ProyeccionModel()
        self.view = ProyeccionView(root)
        self.view.calc_button.config(command=self.calcular_proyeccion)

    def calcular_proyeccion(self):
        P_P = self.view.get_punto()
        PL_M = self.view.get_plano()
        if P_P is not None and PL_M is not None:
            plano, vectores, puntos = self.model.calcular_proyeccion(P_P, PL_M)
            self.animar(plano, vectores, puntos)

    def animar(self, plano, vectores, puntos):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        X, Y = np.meshgrid(np.linspace(-5, 5), np.linspace(-5, 5))
        Z = -(plano[0] * X + plano[1] * Y + plano[3]) / plano[2]

        ax.plot_surface(X, Y, Z, color="yellow", alpha=0.5)

        def update(frame):
            ax.clear()
            ax.plot_surface(X, Y, Z, color="yellow", alpha=0.5)


            if frame >= .5:
                punto = puntos["P"]
                ax.scatter(punto[0], punto[1], punto[2], c='blue', s=10,
                            label="Punto a proyectar")

            if frame >= 1 + sep:
                punto = puntos["P_0"]
                ax.scatter(punto[0], punto[1], punto[2], c='blue', s=10,
                            label="Punto origen en el plano")

            if frame >= 1 + 2 * sep:
                vector = vectores["u"]
                ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], 
                          vector[5], color="purple", arrow_length_ratio=0, 
                          label="Vector u (P-P0)")

            if frame >= 1 + 3 * sep:
                vector = vectores["n"]
                ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5], color="orange", arrow_length_ratio=0,
                          label="vector n (normal al plano)")
                vector = vectores["-n"]
                ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5], color="orange", arrow_length_ratio=0)

            if frame >= 1 + 4 * sep:
                vector = vectores["proy_n_u"]
                ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5], color="green", arrow_length_ratio=0,
                          label="Proyeccion ortogonal")

            if frame >= 1 + 5 * sep:
                punto = puntos["P_"]
                ax.scatter(punto[0], punto[1], punto[2], c='red', s=10, 
                           label="Punto proyectado")


        sep = 2
        ext_dur = 6

        ani = FuncAnimation(fig, update, frames=range(1 + (6+ext_dur) * sep), interval=1000)
        ani.save("proyeccion.gif", fps=10)
        plt.show()

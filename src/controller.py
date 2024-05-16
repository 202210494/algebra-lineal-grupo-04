from model import ProyeccionModel
from view import ProyeccionView
import matplotlib.pyplot as plt
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
            self.graficar(plano, vectores, puntos)

    def graficar(self, plano, vectores, puntos):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        X, Y = np.meshgrid(np.linspace(-5, 5), np.linspace(-5, 5))
        Z = -(plano[0] * X + plano[1] * Y + plano[3]) / plano[2]
        ax.plot_surface(X, Y, Z, color="yellow", alpha=0.5)

        for tag, punto in puntos.items():
            ax.scatter(punto[0], punto[1], punto[2], c='blue', s=10, label=tag)
        for tag, vector in vectores.items():
            color = "orange" if (tag == "n" or tag == "-n") else "green" if tag == "proy_n_u" else "purple"
            ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5], color=color, arrow_length_ratio=0)

        plt.show()

from model import ProyeccionModel
from view import ProyeccionView
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time

class ProyeccionController:
    def __init__(self, root):
        self.model = ProyeccionModel()
        self.view = ProyeccionView(root)
        self.view.calc_button.config(command=self.calcular_proyeccion)
        self.view.calc_button_rot.config(command=self.calcular_proyeccion_rotacion)

    def calcular_proyeccion(self):
        P_P = self.view.get_punto()
        PL_M = self.view.get_plano()
        if P_P is not None and PL_M is not None:
            plano, vectores, puntos = self.model.calcular_proyeccion(P_P, PL_M)
            self.animar(plano, vectores, puntos)

    def calcular_proyeccion_rotacion(self):
        P_P = self.view.get_punto()
        PL_M = self.view.get_plano()
        rotacion = self.view.get_rotaciones()
        if P_P is not None and PL_M is not None and rotacion is not None:
            plano, vectores, puntos = self.model.calcular_proyeccion(P_P, PL_M)
            self.animar(plano, vectores, puntos, rotacion)


    '''
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
    '''
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
        R = Rz @ Ry @ Rx
        return R @ punto

    def animar(self, plano, vectores, puntos, rotacion=None):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        # pintamos plano con meshgrid

        X, Y = np.meshgrid(np.linspace(-5, 5), np.linspace(-5, 5))
        Z = -(plano[0] * X + plano[1] * Y + plano[3]) / plano[2] # Ecuacion del plano 

        ax.plot_surface(X, Y, Z, color="yellow", alpha=0.5)

        def update_s_r(frame):
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
                
        def update_con_rotacion(frame):
            ax.clear()
            ax.plot_surface(X, Y, Z, color="yellow", alpha=0.5)

            if frame >= .5:
                punto = self.rotar_punto(puntos["P"], rotacion)
                ax.scatter(punto[0], punto[1], punto[2], c='blue', s=10, label="P")

            if frame >= 1 + sep:
                punto = self.rotar_punto(puntos["P_0"], rotacion)
                ax.scatter(punto[0], punto[1], punto[2], c='blue', s=10, label="P_0")

            if frame >= 2 + sep:
                vector = vectores["u"]
                origen = self.rotar_punto(vector[:3], rotacion)
                destino = self.rotar_punto(vector[:3] + vector[3:], rotacion)
                ax.quiver(origen[0], origen[1], origen[2], destino[0]-origen[0], destino[1]-origen[1], destino[2]-origen[2], color="purple", arrow_length_ratio=0)

            if frame >= 3 + sep:
                vector = vectores["n"]
                origen = self.rotar_punto(vector[:3], rotacion)
                destino = self.rotar_punto(vector[:3] + vector[3:], rotacion)
                ax.quiver(origen[0], origen[1], origen[2], destino[0]-origen[0], destino[1]-origen[1], destino[2]-origen[2], color="orange", arrow_length_ratio=0)

                vector = vectores["-n"]
                origen = self.rotar_punto(vector[:3], rotacion)
                destino = self.rotar_punto(vector[:3] + vector[3:], rotacion)
                ax.quiver(origen[0], origen[1], origen[2], destino[0]-origen[0], destino[1]-origen[1], destino[2]-origen[2], color="orange", arrow_length_ratio=0)

            if frame >= 4 + sep:
                vector = vectores["proy_n_u"]
                origen = self


        sep = 2
        ext_dur = 6

        ani = FuncAnimation(fig, update_s_r, frames=range(1 + (7+ext_dur) * sep), interval=1000)
        #delay =  (1 + (7 + ext_dur) * sep)
        delay =(.5) # por mientras
        time.sleep(delay) # Esperamos a que termine la animacion, pero crashea

        if rotacion.any():
            ani = FuncAnimation(fig, update_con_rotacion, frames=range(1 + 5 * sep), interval=1000)

        ani.save("proyeccion.gif", fps=10)
        plt.show()

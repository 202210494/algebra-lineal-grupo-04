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
            plano, vectores, puntos = self.model.calc_con_rotacion(P_P, PL_M, rotacion)
            self.animar(plano, vectores, puntos, rotacion)


    def animar(self, plano, vectores, puntos, rotacion=None):
        #mpl.rcParams.update(mpl.rcParamsDefault)
        #plt.style.use("default")
        plt.style.use("tableau-colorblind10")
        #plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
        #plt.style.use("bmh") # https://python-charts.com/es/matplotlib/estilos/#google_vignette
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d", autoscale_on=True)

        # pintamos plano con meshgrid

        X, Y = np.meshgrid(np.linspace(-5, 5), np.linspace(-5, 5))
        Z = -(plano[0] * X + plano[1] * Y + plano[3]) / plano[2] # Ecuacion del plano (tomamos z como la variable dependiente)

        ax.plot_surface(X, Y, Z, color="yellow", alpha=0.5)

        def update_s_r(frame):
                          
            ax.clear()
            ax.plot_surface(X, Y, Z, color="yellow", alpha=0.5)


            if frame >= .5:
                punto = puntos["P"]
                ax.scatter(punto[0], punto[1], punto[2], c='yellow', s=10)
                ax.text(punto[0], punto[1], punto[2], f'P ({round(punto[0],2)}, {round(punto[1],2)}, {round(punto[2],2)})', # 
                        fontsize=8, ha='center', va='bottom', color='black')
                

            if frame >= 1 + sep:
                punto = puntos["P_0"]
                ax.scatter(punto[0], punto[1], punto[2], c='blue', s=10)
                ax.text(punto[0], punto[1], punto[2], f'P ({round(punto[0],2)}, {round(punto[1],2)}, {round(punto[2],2)})', #                         
                        fontsize=8, ha='center', va='bottom', color='black')

            if frame >= 1 + 2 * sep:
                vector = vectores["u"]
                ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], 
                          vector[5], color="purple", arrow_length_ratio=0.1,
                          label="Vector u (P-P0)")

            if frame >= 1 + 3 * sep:
                vector = vectores["n"]
                ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5], color="orange", arrow_length_ratio=0.1,
                          label="vector n (normal al plano)")
                vector = vectores["-n"]
                ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5], color="orange", arrow_length_ratio=0.1)

            if frame >= 1 + 4 * sep:
                vector = vectores["proy_n_u"]
                ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5], color="green", arrow_length_ratio=0.1,
                          label="Proyeccion ortogonal")

            if frame >= 1 + 5 * sep:
                punto = puntos["P_"]
                ax.scatter(punto[0], punto[1], punto[2], c='red', s=10)        
                ax.text(punto[0], punto[1], punto[2], f'P ({round(punto[0],2)}, {round(punto[1],2)}, {round(punto[2],2)})', #                         
                        fontsize=8, ha='center', va='bottom', color='black')    
            #ax.legend(loc='lower left') no se puede colocar indice sin warning

        def update_con_rotacion(frame):
                ax.clear()
                ax.plot_surface(X, Y, Z, color="yellow", alpha=0.5)

                if frame >= .5:
                    punto = puntos["P"]
                    ax.scatter(punto[0], punto[1], punto[2], c='yellow', s=10)
                    ax.text(punto[0], punto[1], punto[2], f'P ({round(punto[0],2)}, {round(punto[1],2)}, {round(punto[2],2)})', # 
                            fontsize=8, ha='center', va='bottom', color='black')

                if frame >= 1 + sep:
                    punto = puntos["P_0"]
                    ax.scatter(punto[0], punto[1], punto[2], c='blue', s=10)
                    ax.text(punto[0], punto[1], punto[2], f'P ({round(punto[0],2)}, {round(punto[1],2)}, {round(punto[2],2)})', #                         
                            fontsize=8, ha='center', va='bottom', color='black')

                if frame >= 1 + 2 * sep:
                    vector = vectores["u"]
                    ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], 
                              vector[5], color="purple", arrow_length_ratio=0.1,
                              label="Vector u (P-P0)")

                if frame >= 1 + 3 * sep:
                    vector = vectores["n"]
                    ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5], color="orange", arrow_length_ratio=0.1,
                              label="vector n (normal al plano)")
                    vector = vectores["-n"]
                    ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5], color="orange", arrow_length_ratio=0.1)

                if frame >= 1 + 4 * sep:
                    vector = vectores["proy_n_u"]
                    ax.quiver(vector[0], vector[1], vector[2], vector[3], vector[4], vector[5], color="green", arrow_length_ratio=0.1,
                              label="Proyeccion ortogonal")

                if frame >= 1 + 5 * sep:
                    punto = puntos["P_"]
                    ax.scatter(punto[0], punto[1], punto[2], c='red', s=10)        
                    ax.text(punto[0], punto[1], punto[2], f'P ({round(punto[0],2)}, {round(punto[1],2)}, {round(punto[2],2)})', #                         
                            fontsize=8, ha='center', va='bottom', color='black')   

                if frame >= 1 + 6 * sep:
                    punto = puntos["P_r"]
                    ax.scatter(punto[0], punto[1], punto[2], c='green', s=10)        
                    ax.text(punto[0], punto[1], punto[2], f'P ({round(punto[0],2)}, {round(punto[1],2)}, {round(punto[2],2)})', #                         
                            fontsize=8, ha='center', va='bottom', color='black') 

        sep = 2
        ext_int = 2

        if rotacion is not None:
            ani2 = FuncAnimation(fig, update_con_rotacion, frames=range((8+ext_int) * sep), interval=1000)
            ani2.save("proyeccion_rotacion.gif", fps=10)
        else:
            ani = FuncAnimation(fig, update_s_r, frames=range((7+ext_int) * sep), interval=1000)
            ani.save("proyeccion.gif", fps=10)
        
        plt.show()

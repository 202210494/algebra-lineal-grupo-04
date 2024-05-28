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
            size = self.model.calc_max_v()
            self.model.describir_proyeccion(PL_M)
            self.animar(plano, vectores, puntos, size)

    def calcular_proyeccion_rotacion(self):
        P_P = self.view.get_punto()
        PL_M = self.view.get_plano()
        rotacion = self.view.get_rotaciones()
        
        if P_P is not None and PL_M is not None and rotacion is not None:
            plano, vectores, puntos = self.model.calc_con_rotacion(P_P, PL_M, rotacion)
            size = self.model.calc_max_v()
            self.model.describir_proyeccion(PL_M)
            self.animar(plano, vectores, puntos, size, rotacion)


    def animar(self, plano, vectores, puntos, size ,rotacion=None):
        #mpl.rcParams.update(mpl.rcParamsDefault)
        #plt.style.use("default")
        plt.style.use("tableau-colorblind10")
        #plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
        #plt.style.use("bmh") # https://python-charts.com/es/matplotlib/estilos/#google_vignette
        
        fig = plt.figure()

        # PARA FIXEAR EL PROBLEMA DEL ZOOM ES POSIBLE QUE plt.xlim(izq,der) pueda ser util
        #  Le metes una ecuacion por toda la cara
        # texto1 = plt.text(0.5, 0.5, r'$E = \frac{V_0}{r*\ln(\frac{b}{a})}$', 
        #          ha="center", va="center",
        #          fontsize=17, transform=plt.gca().transAxes)


        if rotacion is not None:
            ax = fig.add_subplot(122, projection="3d")
            ax1 = fig.add_subplot(121, projection="3d")
        else:
            ax = fig.add_subplot(111, projection="3d", autoscale_on=True)

        X, Y = np.meshgrid(np.linspace(-size, size), np.linspace(-size, size))
        Z = -(plano[0] * X + plano[1] * Y + plano[3]) / plano[2] # Ecuacion del plano (tomamos z como la variable dependiente)

        ax.plot_surface(X, Y, Z, color="yellow", alpha=0.5)

        if rotacion is not None:
            ax1.plot_surface(X, Y, Z, color="yellow", alpha=.5)

        def _update_proyeccion(frame):
                          
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

        def _update_proyeccion_rotacion(frame):
                          
            _update_proyeccion(frame)
            ax1.clear()
            ax1.plot_surface(X, Y, Z, color="yellow", alpha=0.5)

            ####################################ADD Formulas en Latex####################

            #texto1 = ax1.text(0.5, 0.5, r'$E = \frac{V_0}{r*\ln(\frac{b}{a})}$', 
            #     ha="center", va="center", fontsize=17, transform=ax1.transAxes)
            #  text2d para 2d, text para 3d

            # ax espacio en los ejes
            #ax1.text(0.5, 0.5, 0, r'$E = \frac{V_0}{r*\ln(\frac{b}{a})}$', 
            # ha="left", va="bottom", fontsize=17)

            fig.text(0.5, 0.05, r'$E = \frac{V_0}{r*\ln(\frac{b}{a})}$', 
                ha="left", va="center", fontsize=17)
            
            ##########X#######
            #fig.text(0.8, 0.05, r'$E = \frac{V_0}{r*\ln(\frac{b}{a})}$', 
            #    ha="right", va="center", fontsize=17)

            if frame >= .5:
                punto = puntos["P_Rotar"]
                ax1.scatter(punto[0], punto[1], punto[2], c='red', s=20)
                ax1.text(punto[0], punto[1], punto[2], f'P ({round(punto[0],2)}, {round(punto[1],2)}, {round(punto[2],2)})', # 
                        fontsize=8, ha='center', va='bottom', color='black')
            
            if frame >= 1.5:
                punto = puntos["P"]
                ax1.scatter(punto[0], punto[1], punto[2], c='yellow', s=20)
                ax1.text(punto[0], punto[1], punto[2], f'P ({round(punto[0],2)}, {round(punto[1],2)}, {round(punto[2],2)})', # 
                        fontsize=8, ha='center', va='bottom', color='black')

        sep = 2
        ext_int = 2

        if rotacion is not None:
            ani1 = FuncAnimation(fig, _update_proyeccion_rotacion, frames=range((8+ext_int) * sep), interval=1000)
            ani1.save("proyeccion_rotacion.gif", fps=10)
        else:
            ani = FuncAnimation(fig, _update_proyeccion, frames=range((7+ext_int) * sep), interval=1000)
            ani.save("proyeccion.gif", fps=10)
        
        plt.show()

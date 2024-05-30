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

    def calcular_proyeccion_base(self, con_rotacion=False):
        P_P = self.view.get_punto()
        PL_M = self.view.get_plano()
        rotacion = self.view.get_rotaciones() if con_rotacion else None

        if P_P is not None and PL_M is not None and (not con_rotacion or rotacion is not None):
            if con_rotacion:
                plano, vectores, puntos = self.model.calc_con_rotacion(P_P, PL_M, rotacion)
                #self.model.describir_proyeccion(PL_M)
            else:
                plano, vectores, puntos = self.model.calcular_proyeccion(P_P, PL_M)
            size = self.model.calc_max_v()
            self.animar(plano, vectores, puntos, size, rotacion)

    def calcular_proyeccion(self):
        self.calcular_proyeccion_base(con_rotacion=False)

    def calcular_proyeccion_rotacion(self):
        self.calcular_proyeccion_base(con_rotacion=True)



    def animar(self, plano, vectores, puntos, size ,rotacion=None):

        ##################################### Configuracion Animacion ############################
        # Para resetear el estilo de matplotlib
        #mpl.rcParams.update(mpl.rcParamsDefault)
        #plt.style.use("default")


        plt.style.use("tableau-colorblind10")
        #plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
        #plt.style.use("bmh") # https://python-charts.com/es/matplotlib/estilos/#google_vignette
        

        # PARA FIXEAR EL PROBLEMA DEL ZOOM ES POSIBLE QUE plt.xlim(izq,der) pueda ser util
        #  Le metes una ecuacion por toda la cara
        # texto1 = plt.text(0.5, 0.5, r'$E = \frac{V_0}{r*\ln(\frac{b}{a})}$', 
        #          ha="center", va="center",
        #          fontsize=17, transform=plt.gca().transAxes)
        fig = plt.figure()

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

            ### parte debil (en proceso)
            # mejorar robustez y modularidad
            # ajustar duracion de los vectores
            vecs = {
                # key : (frame_inicio, color, duracion)
                    "u" : (60, "purple", 100),
                    "n" : (80, "orange", 1000),
                    "-n" : (80, "orange", 1000),
                    "proy_n_u" : (100, "green", 20),
            }
            points = {
                        "P" : (1, "blue"),
                        "P_0" : (20, "orange"),
                        "P_" : (100, "red")
            }
            
            for key, v in points.items():

                if frame >= v[0]:
                    punto = puntos[key] # validar 
                    punto.dibujar(ax, color=v[1])    


            for key, v in vecs.items():
                    
                if frame >= v[0]:
                    vector = vectores[key]
                    duration = v[2]
                    vector.dibujar(ax, color=v[1], frame =frame, f_inicio= v[0], f_dur = duration)
                    
            print(frame)
            

        def _update_proyeccion_rotacion(frame):
                          
            _update_proyeccion(frame) # actualiza el ax principal
            ax1.clear()
            ax1.plot_surface(X, Y, Z, color="yellow", alpha=0.5)

            points = {
                        "P_Rotar" : (1, "orange"),
                        "P_" : (20, "blue")
            }

            for key, v in points.items():
                if frame >= v[0]:
                    punto = puntos[key]
                    punto.dibujar(ax1, color=v[1])

            # mejorar la animacion
            # mejorar la rotacion
            # mejorar la proyeccion
            # mejorar la visualizacion
            # mejorar la descripcion
            # mejorar la interaccion
            # mejorar la documentacion
            # mejorar la presentacion
            # mejorar la eficiencia
            # mejorar la modularidad
            # mejorar la escalabilidad
            # mejorar la robustez
            # mejorar la usabilidad
            # mejorar la accesibilidad
            # mejorar la estabilidad
            # mejorar la compatibilidad
            # mejorar la confiabilidad
            # mejorar la seguridad
            # mejorar la privacidad
            # mejorar la integridad
            # mejorar la disponibilidad
            # mejorar la mantenibilidad
            # mejorar la portabilidad
            # llorar

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
            '''
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
            '''
    
        sep = 2
        ext_int = 2

        # cambiar frames
        if rotacion is not None:
            ani1 = FuncAnimation(fig, _update_proyeccion_rotacion, frames=range(1000), interval=100)
            #ani1.save("proyeccion_rotacion.gif", fps=10)
        else:
            ani = FuncAnimation(fig, _update_proyeccion, frames=range(1000), interval=100)
            #ani.save("proyeccion.gif", fps=60) # problema con los frames 
        
        plt.show()

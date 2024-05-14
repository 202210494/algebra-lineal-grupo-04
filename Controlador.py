import numpy as np
import matplotlib.pyplot as plt

class Controlador:
    def __init__(self, modelo):
        self.loop = True
        self.m = modelo
        #self.v = vista

    def Vizualizacion3D(self, plano,pt,tpt):
        #Formula plano: ax + by + cz + d = 0
        #Formula en funcion de z:  z = -(d + ax +by)/(c)

        #creamos el figure
        fig = plt.figure()
        #de tipo 3d!
        ax = fig.add_subplot(111,projection="3d")

        #limites inferiores y superiores para los ejes X e Y
        #dependen de los valores del punto y el Tpunto, para que siempre
        #esten dentro del figure
        limite_inferiorX = pt[0] - 5
        limite_superiorX = pt[0] + 5
        limite_inferiorY = tpt[1] - 5
        limite_superiorY = pt[1] + 5

        #creacion del meshgrid, en resumen es el rango de valores que tomaran X e Y
        X, Y = np.meshgrid(np.linspace(limite_inferiorX,limite_superiorX),np.linspace(limite_inferiorY,limite_superiorY))

        #aca simplemente igualamos Z igual a la funcion
        #si quisieramos, por ejemplo, representar x^2 + y^2 -z = 0
        #seria Z = -(x^2 + y^2)
        Z= -(plano[0]*X+plano[1]*Y+plano[3])/plano[2]

        #colocamos los puntos en el grafico
        ax.scatter(pt[0], pt[1], pt[2], c='blue', s=10)
        ax.scatter(tpt[0], tpt[1], tpt[2], c='red', marker="*", s=100)

        #creamos la superficie del plano
        ax.plot_surface(X, Y, Z)

        #aqui es donde empieza la magia
        plt.show()


    def iniciar_aplicacion(self):
        while self.loop:
            print("Proyección ortogonal de un punto en un plano en R3")
            print("-----------------------------------------------")

            # Solicitamos el plano donde se proyectará el punto
            ecuacion_plano = input("Ingrese los coeficientes de la ecuación del plano en la forma ax + by + cz + d = 0: ")
            plano = self.m.crear_plano(ecuacion_plano)
            print(f"Su funcion es: {plano.ecuacion.__str__()}")

            # Solicitamos las coordenadas del punto a proyectar
            print("\nIngrese las coordenadas del punto a proyectar")
            coordenadas_punto = input("Ingrese las coordenadas del punto (x; y; z): ")
            punto = self.m.crear_punto(coordenadas_punto)
            

            coeficientes_plano = plano.ecuacion.getCoeficientes()
            # Calcular la Proyeccion Ortogonal
            # verificamos si el punto esta en el plano -> si es asi, su proyeccion es el mismo punto
            # caso contrario, la calculamos
            
            if self.m.punto_en_planoR3(coeficientes_plano, punto.coordenadas):
                punto_proyeccion = punto
            else:
                punto_proyeccion = self.m.calcular_proyeccion_ortogonal(coeficientes_plano, punto.coordenadas)
            
                print(f"La proyección ortogonal del punto {punto} en el plano {plano.ecuacion.__str__()} es:")
                print(f"T(x; y; z) = {punto_proyeccion}")

                self.Vizualizacion3D(coeficientes_plano, punto.coordenadas, punto_proyeccion)
                #time.sleep(.5)

            if input("Otra vez? (Y/N): ") not in ["Y","y"]:
                self.loop = False




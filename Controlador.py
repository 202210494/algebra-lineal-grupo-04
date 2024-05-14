class Controlador:
    def __init__(self, modelo):
        self.loop = True
        self.m = modelo
        #self.v = vista


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

            if input("Otra vez? (Y/N): ") not in ["Y","y"]:
                self.loop = False




class Controlador:
    def __init__(self, modelo):
        self.loop = True
        self.m = modelo
        #self.v = vista


    def iniciar_aplicacion(self):
        while self.loop:
            print("Proyección ortogonal de un punto en un plano en R3")
            print("-----------------------------------------------")
            # Pedimos el plano donde se proyectará el punto
            print("Ingrese los coeficientes de la ecuación del plano en la forma ax + by + cz + d = n")
            enunciados_funcion = ["Ingresar a: ","Ingresar b: ","Ingresar c: ","Ingresar d: ", "Ingresar valor de igualdad (n): "]
            coeficientes_plano = []
            self.m.ingresar_valores_float(coeficientes_plano, enunciados_funcion)

                # d = (d-n) para que la funcion iguale a cero
                # pop() para eliminar (n) y nos quedamos con el vector normal :D
            coeficientes_plano[3] -= coeficientes_plano.pop()

            # Comunicamos la Ecuacion general del plano introducido
            texto_funcion = f"({coeficientes_plano[0]})x + ({coeficientes_plano[1]})y + ({coeficientes_plano[2]})z + ({coeficientes_plano[3]}) = 0"
            print(f"Su funcion es: {texto_funcion}")

            print("\nIngrese las coordenadas del punto a proyectar")
            coordenadas_punto = input("Ingrese las coordenadas del punto (x; y; z): ")
            punto = self.m.crear_punto(coordenadas_punto)

            # verificamos si el punto esta en el plano -> si es asi, su proyeccion es el mismo punto
            # caso contrario, la calculamos
            if self.m.punto_en_planoR3(coeficientes_plano, punto.coordenadas):
                punto_proyeccion = punto
            else:
                punto_proyeccion = self.m.calcular_proyeccion_ortogonal(coeficientes_plano, punto.coordenadas)
            
            print(f"La proyección ortogonal del punto {punto} en el plano {texto_funcion} es:")
            print(f"T(x; y; z) = {punto_proyeccion}")

            if input("Otra vez? (Y/N): ") not in ["Y","y"]:
                self.loop = False



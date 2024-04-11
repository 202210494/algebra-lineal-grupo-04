
class Controlador:
    def __init__(self, modelo):
        self.loop = True
        self.m = modelo
        #self.v = vista


    def iniciar_aplicacion(self):
        while self.loop:
            enunciados_funcion = ["Ingresar coeficiente de x: ","Ingresar coeficiente de y: ","Ingresar coeficiente de z: ","Ingresar valor constante: ", "Ingresar valor de igualdad: "]
            coeficientes_plano = []
            self.m.ingresar_valores_float(coeficientes_plano, enunciados_funcion)

            #restamos el valor de igualdad al valor constante para que la funcion iguale a cero
            #retiramos el valor de igualdad de la lista
            coeficientes_plano[3] -= coeficientes_plano.pop()

            texto_funcion = f"({coeficientes_plano[0]})x + ({coeficientes_plano[1]})y + ({coeficientes_plano[2]})z + ({coeficientes_plano[3]}) = 0"

            print(f"Su funcion es: {texto_funcion}")

            coordenadas_punto = input("Ingrese las coordenadas del punto (x; y; z): ")
            punto = self.m.crear_punto(coordenadas_punto)

            #si las coordenadas estan en el plano, su proyeccion es si misma
            if self.m.punto_en_planoR3(coeficientes_plano, punto.coordenadas):
                punto_proyeccion = punto
            else:
                punto_proyeccion = self.m.calcular_proyeccion_ortogonal(coeficientes_plano, punto.coordenadas)

            print(f"La proyección ortogonal del punto {punto} en el plano {texto_funcion} es:")
            print(f"T(x; y; z) = {punto_proyeccion}")

            if input("Otra vez? (Y/N): ") not in ["Y","y"]:
                self.loop = False

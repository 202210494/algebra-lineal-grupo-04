from Punto import Punto3D
from funciones import ingresar_valores_float, punto_en_planoR3, calcular_proyeccion_ortogonal

def main():
    loop = True

    while loop:
        print("Proyección ortogonal de un punto en un plano en R3")
        print("-----------------------------------------------")
        print("Ingrese los coeficientes de la ecuación del plano en la forma ax + by + cz + d = 0")
        enunciados_funcion = ["Ingresar coeficiente de x: ","Ingresar coeficiente de y: ","Ingresar coeficiente de z: ","Ingresar valor constante: ", "Ingresar valor de igualdad: "]

        coeficientes_plano = []

        ingresar_valores_float(coeficientes_plano, enunciados_funcion)

        #restamos el valor de igualdad al valor constante para que la funcion iguale a cero

        #retiramos el valor de igualdad de la lista
        coeficientes_plano[3] -= coeficientes_plano.pop()

        texto_funcion = f"({coeficientes_plano[0]})x + ({coeficientes_plano[1]})y + ({coeficientes_plano[2]})z + ({coeficientes_plano[3]}) = 0"

        print(f"Su funcion es: {texto_funcion}")

        print("\nIngrese las coordenadas del punto a proyectar")
        coordenadas_punto = input("Ingrese las coordenadas (x; y; z) separadas por una coma: ")
        punto = Punto3D(coordenadas_punto)

        # verificamos si el punto esta en el plano -> si es asi, su proyeccion es el mismo punto
        if punto_en_planoR3(coeficientes_plano, punto):
            punto_proyeccion = punto
        else:
            punto_proyeccion = calcular_proyeccion_ortogonal(coeficientes_plano, punto)

        print(f"La proyección ortogonal del punto {punto} en el plano {texto_funcion} es:")
        print(f"T(x; y; z) = {punto_proyeccion}")

        if input("Otra vez? (Y/N): ") not in ["Y","y"]:
            loop = False

main()

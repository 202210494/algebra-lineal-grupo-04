from funciones import ingresar_valores_float, punto_en_planoR3, calcular_proyeccion_ortogonal


enunciados_funcion = ["Ingresar coeficiente de x: ","Ingresar coeficiente de y: ","Ingresar coeficiente de z: ","Ingresar valor constante: ", "Ingresar valor de igualdad: "]
enunciados_punto = ["Ingresar coordenada x: ", "Ingresar coordenada y: ", "Ingresar coordenada z: "]


coeficientes_plano = []
coordenadas= []

ingresar_valores_float(coeficientes_plano, enunciados_funcion)

#restamos el valor de igualdad al valor constante para que la funcion iguale a cero
#retiramos el valor de igualdad de la lista
coeficientes_plano[3] -= coeficientes_plano.pop()

texto_funcion = f"({coeficientes_plano[0]})x + ({coeficientes_plano[1]})y + ({coeficientes_plano[2]})z + ({coeficientes_plano[3]}) = 0"

print("Su funcion es:",texto_funcion)


#Ingresando las coordenadas
ingresar_valores_float(coordenadas,enunciados_punto)

texto_coords = f"({coordenadas[0]}; {coordenadas[1]}; {coordenadas[2]})"

print("Sus coordenadas son:",texto_coords)

#array con las coordenadas de la proyeccion
Tcoords = []

#si las coordenadas estan en el plano, su proyeccion es si misma
if punto_en_planoR3(coeficientes_plano,coordenadas):
  Tcoords = coordenadas
else:
  Tcoords = calcular_proyeccion_ortogonal(coeficientes_plano,coordenadas)
  pass

texto_Tcoords = f"({Tcoords[0]}; {Tcoords[1]}; {Tcoords[2]})"

print(f"La proyección ortogonal del punto {texto_coords} en el plano {texto_funcion} es:")
print(f"T(x; y; z) = {texto_Tcoords}")

from Punto import Punto3D


def ingresar_valores_float(arr,questions):
  for question in questions:
    input_incorrecto = True

    while input_incorrecto:
      valor = input(f"{question}")

      try:
       valor = float(valor)

      except:
       print("Intentelo de nuevo")
       continue

      if valor.as_integer_ratio()[1] == 1:
        valor = int(valor)

      input_incorrecto = False
      arr.append(valor)

def punto_en_planoR3(coeficientes_plano, punto: Punto3D):

    coordenadas = punto.coordenadas
    coordenadas.append(1)
    sum = 0

    for coeficiente, coordenada in zip(coeficientes_plano, coordenadas):
        sum += coeficiente * coordenada

    coordenadas.pop()

    if sum == 0:
        print("El punto está en el mismo plano")
        return True

    else:
        return False

def calcular_lambda(coeficientes_plano, punto: Punto3D):

  sum_coefs_lambda = 0
  sum_indep_lambda = 0

  for i in range(3):
    sum_coefs_lambda += coeficientes_plano[i] ** 2
    sum_indep_lambda += punto.coordenadas[i] * coeficientes_plano[i]

  sum_indep_lambda = sum_indep_lambda + coeficientes_plano[3]

  return (-sum_indep_lambda) / sum_coefs_lambda

def calcular_proyeccion_ortogonal(coeficientes_plano, punto: Punto3D):
    lamb = calcular_lambda(coeficientes_plano, punto)

    proy_x = 0
    proy_y = 0
    proy_z = 0

    proyeccion = [proy_x,proy_y,proy_z]

    for i in range(3):
        proyeccion[i] = punto.coordenadas[i] + (coeficientes_plano[i] * lamb)

    return Punto3D(f"{proyeccion[0]} {proyeccion[1]} {proyeccion[2]}")

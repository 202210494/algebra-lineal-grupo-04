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

def punto_en_planoR3(coeficientes_plano, coordenadas_punto):

  coordenadas_punto.append(1)
  sum = 0

  for coeficiente, coordenada in zip(coeficientes_plano, coordenadas_punto):
    sum += coeficiente * coordenada

  trash = coordenadas_punto.pop()

  if sum == 0:
    print("El punto está en el mismo plano")
    return True

  else:
    return False

def calcular_lambda(arr_plano, coords):

  sum_coefs_lambda = 0
  sum_indep_lambda = 0

  for i in range(3):
    sum_coefs_lambda = sum_coefs_lambda + arr_plano[i]*arr_plano[i]
    sum_indep_lambda = sum_indep_lambda + coords[i]*arr_plano[i]

  sum_indep_lambda = sum_indep_lambda + arr_plano[3]

  return (sum_indep_lambda * -1)/sum_coefs_lambda

def calcular_proyeccion_ortogonal(arr_plano,coords):
  lamb = calcular_lambda(arr_plano,coords)

  proy_x = 0
  proy_y = 0
  proy_z = 0

  proyeccion = [proy_x,proy_y,proy_z]

  for i in range(3):
    proyeccion[i] = coords[i] + arr_plano[i] * lamb

  return proyeccion

from clases.Plano import Plano
from clases.Punto import Punto3D
from clases.Ecuacion import Ecuacion

class Modelo:
    def __init__(self):
        pass

    def crear_ecuacion(self, ecuacion):
      return Ecuacion(ecuacion)
    def crear_plano(self, ecuacion):
      return Plano(ecuacion)
    def crear_punto(self, coordenadas):
      return Punto3D(coordenadas)
    
    
    def ingresar_valores_float(self, arr, questions):
      for question in questions:
        input_incorrecto = True
        while input_incorrecto:
          valor = input(f"{question}")
          try:
            valor = float(valor)
          except ValueError:
            print("Intentelo de nuevo")
            continue

          if valor.is_integer():
            valor = int(valor)

          input_incorrecto = False
          arr.append(valor)
         
    
    # Funcion que determina si un punto está en un plano
    # Fuente: https://www.youtube.com/watch?v=riT4nl0T8_M
    def punto_en_planoR3(self, coeficientes_plano, coordenadas_punto):

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

    def calcular_lambda(self, arr_plano, coords):
      # Calculamos el valor de lambda para encontrar el punto proyectado
      sum_coefs_lambda = 0
      sum_indep_lambda = 0

      # Calculamos el valor de lambda
      # lamda = suma de coeficientes independientes / suma de coeficientes al cuadrado
      # λ = sum(-d - a*x - b*y - c*z) / sum(a^2 + b^2 + c^2)
      for i in range(3):
        sum_coefs_lambda += arr_plano[i] * arr_plano[i]
        sum_indep_lambda += coords[i] * arr_plano[i]

      sum_indep_lambda += arr_plano[3]

      return (sum_indep_lambda * -1) / sum_coefs_lambda

    def calcular_proyeccion_ortogonal(self, arr_plano, coords):
      # El nuevo punto proyectado se encuentra en la recta que pasa por el punto original y es perpendicular al plano
      # La ecuación de la recta es P = P + λV
      lamb = self.calcular_lambda(arr_plano, coords)

      proy_x = 0
      proy_y = 0
      proy_z = 0

      proyeccion = [proy_x,proy_y,proy_z] # P = (0,0,0)
    
      # P = (1,2,3) + λ(-1,-1,-1) = (1, 2, 3) + (-2, -2, -2) 
      for i in range(3):
        proyeccion[i] = coords[i] + arr_plano[i] * lamb
      # Retornamos el punto proyectado
      # P = (1,2,3) + (-2, -2, -2) = (-1,0,1)
      return proyeccion

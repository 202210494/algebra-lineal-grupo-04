from Plano import Plano
from EspacioVectorial import EspacioVectorial

#############################################################
ecuacion = "2x + 4y + 12z + 3 = 1"
# ecuacion = input()
plano = Plano(ecuacion)
print(f"Input: \"{ecuacion}\"\n")
print(f"Ecuacion: \"{plano.ecuacion}\"\n")
print(f"a: {plano.ecuacion.a}")
print(f"b: {plano.ecuacion.b}")
print(f"c: {plano.ecuacion.c}")
print(f"d: {plano.ecuacion.d}")
print(f"=: {plano.ecuacion.igual}")

#############################################################
base = [1, 0, 0], [0, 1, 0], [0, 0, 1]
espacio = EspacioVectorial(base)
espacio.generar_vectores()
print(espacio.__str__())
#2 - Diseñe un algoritmo que determine si ún número es o no es, par positivo.
def esPar(numero):
  return numero %2 == 0

numero = int(input("Ingrese un numero: "))
esPar(2)
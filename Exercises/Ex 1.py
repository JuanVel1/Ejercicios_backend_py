# 1 - Realice un programa que pida la edad de una persona en años. Si la edad es mayor o igual a 18, el programa debe
# imprimir la cadena: ‘ADULTO’. Si la edad es menor a 18 se debe imprimir: ‘MENOR DE EDAD’.
def mayorEdad(edad):
  if edad > 18:
    print('ADULTO')
  else:
    print('MENOR DE EDAD')

edad =int(input("Ingrese su edad: "))
mayorEdad(edad)
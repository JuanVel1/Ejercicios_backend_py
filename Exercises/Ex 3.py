# 3 Diseñe un algoritmo que lea un número de tres cifras y determine si es igual al revés del número
def esPalíndromo(numero):
    posicion_final = len(numero) - 1
    resultado = ''

    for i in range(posicion_final, -1, -1):
        resultado += numero[i]

    return numero == resultado


numero = input('Ingrese numero a evaluar: ')
esPalíndromo(numero)

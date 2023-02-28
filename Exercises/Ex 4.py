# 4 - Realice un programa que lea las notas de un estudiante, despues devolver el promedio, la mejor y la peor nota.
entradas = input("Ingrese las notas del estudiante separadas por coma (',') : ").split(',')
notas = []
total = 0
for entrada in entradas:
  notas.append(int(entrada))
  total += int(entrada)
notas.sort()
promedio =  total / len(notas)

print('Mejor nota : ',notas[len(notas)-1])
print('Peor nota : ',notas[0])
print('Promedio : ',promedio)
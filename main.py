import random, time
from Classes.Camion import Camion
from Classes.Coche import Coche
from Classes.Moto import Moto

if __name__ == '__main__':
    vehiculos = [Coche() for _ in range(3)] + [Moto() for _ in range(2)] + [Camion()]

print("¡Comienza la carrera!")
for _ in range(10):
    for vehiculo in vehiculos:
        velocidad_anterior = vehiculo.velocidad_actual
        aceleracion = random.randint(1, 20)
        vehiculo.acelerar(aceleracion)
        if vehiculo.velocidad_actual == vehiculo.velocidad_maxima:
            print(f"{type(vehiculo).__name__} llegó a su velocidad máxima de {vehiculo.velocidad_maxima} km/h")
        elif vehiculo.velocidad_actual > velocidad_anterior:
            print(f"{type(vehiculo).__name__} aceleró {aceleracion} km/h y ahora va a {vehiculo.velocidad_actual} km/h")
        else:
            print(
                f"{type(vehiculo).name} frenó {velocidad_anterior - vehiculo.velocidad_actual} km/h y ahora va a {vehiculo.velocidad_actual} km/h")
        time.sleep(0.5)

    print()  # línea en blanco para separar las iteraciones

    # ordenar vehículos por velocidad actual para determinar al ganador de la iteración
    vehiculos.sort(key=lambda v: v.velocidad_actual, reverse=True)
    print(
        f"En la iteración {_ + 1}, el ganador es el {type(vehiculos[0]).__name__} con una velocidad de {vehiculos[0].velocidad_actual} km/h")
    vehiculos[0].cambiar_aceite()
    vehiculos[0].acelerar(-vehiculos[0].velocidad_actual)  # frenar el vehículo ganador

    for vehiculo in vehiculos[1:]:
        vehiculo.acelerar(-vehiculo.velocidad_actual)  # frenar los demás vehículos

    print()  # línea en blanco para separar las iteraciones

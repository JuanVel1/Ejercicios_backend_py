import random
import time
class Vehiculo:
    def __init__(self, velocidad_maxima, capacidad_tanque):
        self.velocidad_maxima = velocidad_maxima
        self.capacidad_tanque = capacidad_tanque
        self.velocidad_actual = 0
        self.cantidad_combustible = capacidad_tanque

    def acelerar(self, cantidad):
        if self.cantidad_combustible > 0:
            if self.velocidad_actual + cantidad > self.velocidad_maxima:
                self.velocidad_actual = self.velocidad_maxima
            else:
                self.velocidad_actual += cantidad
            self.cantidad_combustible -= cantidad / 10  # consume 10% de combustible por cada unidad de aceleración
            if self.cantidad_combustible < 0:
                self.cantidad_combustible = 0

    def frenar(self, cantidad):
        if self.velocidad_actual - cantidad < 0:
            self.velocidad_actual = 0
        else:
            self.velocidad_actual -= cantidad

    def cambiar_aceite(self):
        print("Cambiando el aceite del coche...")
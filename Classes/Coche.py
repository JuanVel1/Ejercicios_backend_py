from Classes.Vehiculo import Vehiculo


def turbo(func):
    def wrapper(self, *args, **kwargs):
        self.velocidad_maxima *= 1.5
        func(self, *args, **kwargs)
        self.velocidad_maxima /= 1.5
    return wrapper



class Coche(Vehiculo):
    def __init__(self):
        super().__init__(velocidad_maxima=180, capacidad_tanque=50)
        self.num_pasajeros = 4

    @turbo
    def acelerar(self, cantidad):
        super().acelerar(cantidad)




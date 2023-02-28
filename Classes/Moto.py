from Classes.Coche import Coche
from Classes.Vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(self):
        super().__init__(velocidad_maxima=250, capacidad_tanque=20)

    def wheelie(self):
        print("Haciendo un wheelie con la moto!")

from Classes.Vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self):
        super().__init__(velocidad_maxima=120, capacidad_tanque=100)
        self.capacidad_carga = 5000

    def cargar(self, cantidad):
        if self.capacidad_carga - cantidad < 0:
            print("No se puede cargar esa cantidad, excede la capacidad del camión")
        else:
            print(f"Cargando {cantidad} kg en el camión...")
            self.capacidad_carga -= cantidad
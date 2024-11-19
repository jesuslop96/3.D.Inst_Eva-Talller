class Vehiculo:
    def __init__(self, marca, modelo, año, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def conducir(self):
        return f"El kilometraje del vehiculo a aumentado a {self.kilometraje}"

    def mostrar_detalles(self):
        return f"El vehiculo es de marca {self.marca} modelo {self.modelo} y tiene un kilometraje de {self.kilometraje}"

    def vehiculo_antiguo(self):
        from datetime import datetime
        año_actual = datetime.now().year
        if año_actual - self.año > 20:
            return f"El vehiculo {self.marca} es del año {self.año} asi que es Antiguo {True}"
        return False


Manejar = Vehiculo("BMW", "XM", 2023, 1000)
print(Manejar.conducir())

Informacion = Vehiculo("Toyota", "Corolla", 2015, 0)
print(Informacion.mostrar_detalles())

Antiguedad = Vehiculo("Hyundai", "Accen", 2001, 17000)
print(Antiguedad.vehiculo_antiguo())
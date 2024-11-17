class Habitaciones:
    def __init__(self, numero, tipo, precio, disponible):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = disponible

    def reservar(self):
        return f"La habitacion {self.numero} que es {self.tipo} paso a ser {self.disponible}"

    def liberar(self):
        return f"La habitacion {self.numero} la que es tipo {self.tipo} ya fue {self.disponible}"

    def mostrar_informacion(self):
        return f"La habitacion {self.numero} es una tipo {self.tipo}, su precio es de {self.precio} y se encuentra {self.disponible}"

Booking = Habitaciones("701", "Romantica", 60000, "Reservada")
print(Booking.reservar())

Checkout = Habitaciones("201", "Camadoble", 40000, "Disponible")
print(Checkout.liberar())

Informacion = Habitaciones("804", "VIP", 350000, "Disponible")
print(Informacion.mostrar_informacion())
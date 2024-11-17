class Gestion_productos:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self):
        return f"Se modifica el precio de {self.nombre}, el nuevo precio es {self.precio}"

    def ajustar_inventario(self):
        return f"Se reajusta la cantidad es de {self.cantidad} en el inventario del producto {self.nombre}"

    def mostrar_informacion(self):
        return f"El producto {self.nombre} tiene el precio de {self.precio} y tiene la cantidad en inventario es de {self.cantidad}"


Modificar = Gestion_productos("Mouse", 20000, "58")
print(Modificar.actualizar_precio())

Actualizar = Gestion_productos("Teclado", 30000, 100)
print(Actualizar.ajustar_inventario())

Enseñar = Gestion_productos("Monitor", 60000, 50)
print(Enseñar.mostrar_informacion())
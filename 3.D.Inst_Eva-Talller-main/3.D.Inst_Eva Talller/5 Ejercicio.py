class Libro:
    def __init__(self, titulo, autor, genero, precio):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio

    def aplicar_descuento(self, porcentaje=15):

        descuento = (self.precio * porcentaje) / 100
        self.precio -= descuento
        return f"Al libro '{self.titulo}' se le aplica un descuento de {porcentaje}%, el nuevo precio es de ${self.precio:.2f}"

    def mostrar_informacion(self):

        return f"El libro '{self.titulo}' de género '{self.genero}' es del autor '{self.autor}' y tiene un valor de ${self.precio:.2f}"

    def es_mas_caro_que(self, otro_libro):

        if self.precio > otro_libro.precio:
            return f"El libro '{self.titulo}' es más caro con un precio de ${self.precio:.2f}."
        elif self.precio < otro_libro.precio:
            return f"El libro '{otro_libro.titulo}' es más caro con un precio de ${otro_libro.precio:.2f}."
        else:
            return "Ambos libros tienen el mismo precio."

# Crear instancias de libros
Total_pagar = Libro("Las ventajas de ser un invisible", "Stephen Chbosky", "Juvenil", 150000)
Informacion = Libro("Cien años de soledad", "Gabriel Garcia Marquez", "Novela", 200000)
Comparacion1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez", "Novela", 250000)
Comparacion2 = Libro("Las ventajas de ser un invisible", "Stephen Chbosky", "Juvenil", 150000)

# Aplicar descuento
print(Total_pagar.aplicar_descuento())
print(Informacion.mostrar_informacion())

# Comparar precios entre libros
print(Informacion.es_mas_caro_que(Comparacion2))
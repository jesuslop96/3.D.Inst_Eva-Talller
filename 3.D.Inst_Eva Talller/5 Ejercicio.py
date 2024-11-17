class Libro:
    def __init__(self, titulo, autor, genero, precio):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio

    def aplicar_descuento(self):
        return f"Al libro {self.titulo} se le aplica el descuento de 15% el valor es de {self.precio}"

    def mostrar_informacion(self):
        return f"El libro {self.titulo} de genero {self.genero} es del autor {self.autor} tiene un valor {self.precio}"

    def es_mas_caro_que(self):
        return f"El libro {self.titulo} tiene precio de {self.precio} asi que es mas caro que {self.titulo} y su valor es {self.precio}"

Total_pagar = Libro("Las ventajas de ser un invisible", "Stephen Chbosky", "Juvenil", 150000)

Informacion = Libro("Cien años de soledad", "Gabriel Garcia Marquez", "Novela", 200000)

Comparacion = Libro("Cien años de soledad", "Gabriel Garcia Marquez", "Novela", 200000)
print
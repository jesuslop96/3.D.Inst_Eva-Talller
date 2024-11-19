class Animal:
    def __init__(self, nombre, especie, edad, habitat):
        self.nombre = nombre
        self.especie = especie
        self.edad = int(edad)
        self.habitat = habitat

    def cumplir_años(self):
        self.edad += 1
        print(f"El animal {self.nombre} cumplio un año mas ahora tiene {self.edad}")

    def cambiar_habitat(self, nuevo_habitat):
        self.habitat = nuevo_habitat
        print(f"El animal {self.nombre} se cambio al habitar {self.habitat}")

    def mostrar_detalles(self):
        print(f"El animal {self.nombre} es de la especie {self.especie} su edad es  {self.edad} y su habitat es {self.habitat}")

Animal1 = Animal("Leon", "Mamifero", "5", "Sabana")
print(Animal1.cumplir_años())

Animal2 = Animal("Ballena", "Mamifero", "35", "Oceano")
print(Animal2.cambiar_habitat("Antartida"))

Animal3 = Animal("Lobo", "Mamifero", "8", "Bosque")
print(Animal3.mostrar_detalles())
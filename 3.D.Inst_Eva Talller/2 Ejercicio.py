class Estudiante:
    def __init__(self, nombre, edad, grado, materias):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.materias = materias

    def inscribir_materia(self):
        return f"Se agrega a la materia {self.materias} al alumno {self.nombre}"

    def mostrar_materias(self):
        return f"Estas son las materias {self.materias} de la alumna {self.nombre} que esta en el grado {self.grado}"

    def actualizar_grado(self):
        return f"El alumno {self.nombre} paso todas las materias y pasa al grado {self.grado}"

    def datos_alumno(self):
        return f"El alumno {self.nombre} su edad es {self.edad} es del grado {self.grado} y sus materias son {self.materias}"

Registrar = Estudiante("Jose", "15", 9, "Ingles, Matematica, Castellano, Fisica")
print(Registrar.inscribir_materia())

Enseñar = Estudiante("Laura", "13", 7, "Educacion Fisica, Ingles, Matematica")
print(Enseñar.mostrar_materias())

Modificar = Estudiante("Manuel", "16", 11, "Quimica, Fisica, Matematica, Ingles")
print(Modificar.actualizar_grado())

Informacion = Estudiante("Daniel", "17", 11, "Quimica, Fisica, Matematica, Ingles, Educacion Fisica")
print(Informacion.datos_alumno())
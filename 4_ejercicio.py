# Ejercicio 1: crear una clase estudiandote que tenga atributos de nombre, edad, grado. Luego, crear métodos para mostrar los datos del estudiante y para estudiar.

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nGrado: {self.grado}")

    def estudiar(self):
        print(f"{self.nombre} está estudiando")

nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
grado = input("Ingrese el grado del estudiante: ")

estudiante = Estudiante(nombre, edad, grado)

estudiante.mostrar_datos()
estudiante.estudiar()
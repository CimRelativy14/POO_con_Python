# Herencia en Python: Clase derivada de la clase base que hereda todos los atributos y métodos de la clase base.

class Persona:
    def __init__(self, nombre, edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nNacionalidad: {self.nacionalidad}")

# Clase derivada de la clase Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, salario):
        super().__init__(nombre, edad, nacionalidad) # Llamamos al constructor de la clase base
        self.salario = salario

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Salario: {self.salario}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, nota):
        super().__init__(nombre, edad, nacionalidad)
        self.nota = nota

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Nota: {self.nota}")

oscar = Empleado("Oscar", 25, "Peruano", 10000)

oscar.mostrar_datos() # Nombre: Oscar\nEdad: 25\nSalario: 10000

# con super() se puede llamar a los métodos de la clase base en la clase derivada. En el ejemplo, se llama al método mostrar_datos() de la clase Persona en la clase Empleado y Estudiante.Con self se llama a los métodos de la clase actual en la clase actual. En el ejemplo, se llama al método mostrar_datos() de la clase Empleado en la clase Empleado.
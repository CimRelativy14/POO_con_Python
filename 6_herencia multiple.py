# Herencia multiple en Python: Clase derivada de dos o más clases base. La clase derivada hereda todos los atributos y métodos de las clases base.

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}")

    def saludar(self):
        print(f"Hola, soy {self.nombre}")

    def hablar(self):
        print(f"{self.nombre} está hablando")

class Artista:
    def __init__(self, genero, instrumento):
        self.genero = genero
        self.instrumento = instrumento

    def mostrar_datos(self):
        print(f"Genero: {self.genero}\nInstrumento: {self.instrumento}")

    def cantar(self):
        print(f"{self.nombre} está cantando")

    def tocar(self):
        print(f"{self.nombre} está tocando {self.instrumento}")

# Clase derivada de las clases Persona y Artista
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, genero, instrumento, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, genero, instrumento)
        self.salario = salario
        self.empresa = empresa

    def mostrar_datos(self):
        Persona.mostrar_datos(self)
        Artista.mostrar_datos(self)
        print(f"Salario: {self.salario}\nEmpresa: {self.empresa}")

    def trabajar(self):
        print(f"{self.nombre} está trabajando")

    def crear(self):
        print(f"{self.nombre} está creando")

oscar = EmpleadoArtista("Oscar", 25, "Peruano", "Rock", "Guitarra", 10000, "Google")

oscar.tocar() # Oscar está tocando Guitarra

# isinstance(): Función que devuelve True si un objeto es una instancia de una clase o de una clase derivada de la clase especificada.
# issubclass(): Función que devuelve True si una clase es una subclase de otra clase.
herencia = issubclass(EmpleadoArtista, Persona)
print(herencia) # True

instancia = isinstance(oscar, EmpleadoArtista)
print(instancia) # True
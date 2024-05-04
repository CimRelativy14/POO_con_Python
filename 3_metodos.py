# Métodos de la clase: Son funciones que pertenecen a una clase. Se definen dentro de la clase y se utilizan para realizar operaciones con los atributos de la clase.

class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    # Métodos de la clase
    def mostrar_camara(self):
        print(f"La cámara de {self.modelo} es de {self.camara}")

    def llamar(self):
        print(f"Llamando desde {self.modelo}")

    def cortar(self):
        print(f"Cortando llamada desde {self.modelo}")

Celular1 = Celular("Samsung", "Galaxy S10", "12 MP")
Celular2 = Celular("Apple", "iPhone 11", "24 MP")

Celular1.mostrar_camara() # La cámara de Galaxy S10 es de 12 MP
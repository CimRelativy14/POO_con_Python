# atributos de un objeto(instancia de una clase)

# 'def __init__()' es un método especial en Python que se utiliza para inicializar objetos de una clase. Se conoce como el constructor de la clase. El doble guion bajo al principio y al final del nombre (__init__) indica que es un método especial de Python.

# Cuando creas una instancia de una clase en Python, se llama automáticamente al método __init__ para inicializar el objeto. Puedes definir este método en tu clase y pasarle los argumentos que deseas inicializar al crear un objeto de esa clase.

class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

Celular1 = Celular("Samsung", "Galaxy S10", "12 MP")
Celular2 = Celular("Apple", "iPhone 11", "12 MP")

print(Celular1.marca) # Samsung
# MRO: metodo de resolución de orden de clases. Es el orden en el que se buscan los métodos y atributos en las clases base de una clase derivada.

# MRO en Python

class A:
    def hablar(self):
        print("Hablando desde A")

class B(A):
    def hablar(self):
        print("Hablando desde B")
    
    def saludar(self):
        print("Saludando desde B")

class C(A):
    def hablar(self):
        print("Hablando desde C")

    def saludar(self):
        print("Saludando desde C")

class D(B,C):
    def hablar(self):
        print("Hablando desde D")

d = D()
d.hablar() # Hablando desde D
d.saludar() # Saludando desde B

print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

C.saludar(d) # Saludando desde C
# explicacion de C.saludar(d): se llama al método saludar() de la clase C y se pasa el objeto d como argumento. En la clase C, se llama al método saludar() de la clase C y se imprime "Saludando desde C".
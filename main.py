class Poligono:

    def __init__(self,b,h):
        self.base=b
        self.altura=h

    def imprimir_datos(self):
        print("La base es: ",self.base)
        print("La altura es:",self.altura)

class Rectangulo(Poligono):

    def area(self):
        return self.base*self.altura

class Triangulo(Poligono):

    def area(self):
        return (self.base*self.altura)/2

rectangulo =Rectangulo(20,10)
rectangulo.imprimir_datos()
print("Area= ",rectangulo.area())

triangulo=Triangulo(20,10)
triangulo.imprimir_datos()
print("Area= ",triangulo.area())

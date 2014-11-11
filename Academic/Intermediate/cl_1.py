__author__ = 'nickbortolotti'
#creacion y modelado de clases

class Figura:
    #atributos
    descripcion = "ninguna descripcion"
    autor ="no autor"

    #metodo inicial - constructor
    def __init__(self,x,y):
        self.x = x
        self.y = y

    #metodos
    def area(self):
        return self.x * self.y

    def perimetro(self):
        return 2 * self.x + 2 * self.y

    def nombreAutor(self, texto):
        self.descripcion = texto

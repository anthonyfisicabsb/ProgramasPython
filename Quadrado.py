class Retangulo:
    lado_a= None
    lado_b= None

    def __init__(self,lado_a,lado_b):
        self.lado_a=lado_a
        self.lado_b=lado_b
        print('Criando uma nova instância de Retângulo')

    def calcula_area(self):
        return self.lado_a*self.lado_b

    def calcula_perimetro(self):
        return 2*(self.lado_a+self.lado_b)

class Quadrado(Retangulo):
    def __init__(self,lado):
        self.lado_a=lado
        self.lado_b=lado

r3=Quadrado(10)

print(r3.lado_a,r3.lado_b)
print(r3.calcula_area(),r3.calcula_perimetro())


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


r1=Retangulo(2,5)
r2=Retangulo(3,4)

print(r1.calcula_perimetro())
print(r2.calcula_area())

print(r1.lado_a)
print(r1.lado_b)


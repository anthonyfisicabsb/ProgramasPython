class Restaurant():
        def __init__(self,name,cuisine):
            self.restaurant_name=name
            self.cuisine_type=cuisine

        def describe_restaurant(self):
            print('Restaurant name: %s' % self.restaurant_name)
            print('Cuisine type: %s' % self.cuisine_type)


class IceCreamStand(Restaurant):

    def __init__(self,name):
        super().__init__(name,'Ice Creams')
        self.flavours = ['Creme de Leite','Morango','Vanilla','Chocolate','Chiclete','Banana','Maçã']
        
    def write_flavours(self):
        print('Lista de Sabores:')
        for valor in range(0,len(self.flavours)-1):
            print('  %d : %s' % (valor,self.flavours[valor]))

loja = IceCreamStand('Sorvetes do Zé')

loja.write_flavours()

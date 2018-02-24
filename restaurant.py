class Restaurant():
    def __init__(self,name,cuisine):
        self.restaurant_name=name
        self.cuisine_type=cuisine

    def describe_restaurant(self):
        print('Restaurant name: %s' % self.restaurant_name)
        print('Cuisine type: %s' % self.cuisine_type)

restaurant = Restaurant('El Chapo','Mexican Food')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()

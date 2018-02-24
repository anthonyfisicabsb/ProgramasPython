class User():
    def __init__(self,first_name,last_name,rg):
        self.first_name=first_name
        self.last_name=last_name
        self.rg= rg

    def describe_user(self):
        print('First name: %s' % self.first_name)
        print('Last name: %s' % self.last_name)
        print('RG: %s' % self.rg)

    def greet_user(self):
        print('I\'m %s %s and with %d ID' %(self.first_name,self.last_name,self.rg))

user1 = User('Carlos','Machado',4568)
user2 = User('Mullin','Jonue',7895)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

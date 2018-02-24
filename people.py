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


class Admin(User):
    def __init__(self,first_name,last_name,rg):
        super().__init__(first_name,last_name,rg);
        self.privileges = Privileges()

class Privileges():
    def __init__(self):
       self. privileges = ['can add a post','can delete a post','can ban a user','can create new rooms']
    
    def show_privileges(self):
        print('Lista de privilégios:')
        for privilege in self.privileges:
            print(' %s' % privilege)
        print(' ')


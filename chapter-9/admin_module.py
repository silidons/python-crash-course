from user_module import User

class Admin(User):
    
    def __init__(self, first_name, last_name, city, age):
        super().__init__(first_name, last_name, city, age)
        self.privileges = Privileges()
        
class Privileges:
    
    def __init__(self, privileges=['can delete post', 'can add user', 'is an admin']):
        self.privileges = privileges
        
    def show_privileges(self):
        print("Privileges: ")
        for privilege in self.privileges:
            print(f'\t{privilege.title()}')
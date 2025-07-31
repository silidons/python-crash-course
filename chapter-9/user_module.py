class User:

    def __init__(self, first_name, last_name, city, age):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"Hello {self.first_name.title()}, the following is a summary of your account: ")
        print(f"\t{self.first_name.title()} is your first name, {self.last_name.title()} is your last name, ")
        print(f"\t{self.age} is your age, and you live in {self.city.title()}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}, thank you for logging in!\n")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0

# 9-1 Restaurant
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restauraunt(self):
        print(f"This is {self.restaurant_name.title()}, welcome, we serve {self.cuisine_type.title()} food!")

    def open_restaurant(self):
        print(f"Welcome to {self.restaurant_name.title()}, we're open!")

restaurant = Restaurant('tacos and beer', 'mexican')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restauraunt()
restaurant.open_restaurant()

# 9-2 Three Restaurants
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restauraunt(self):
        print(f"This is {self.restaurant_name.title()}, welcome, we serve {self.cuisine_type.title()} food!")

    def open_restaurant(self):
        print(f"Welcome to {self.restaurant_name.title()}, we're open!")

rest1 = Restaurant('billy', 'mexican')
rest2 = Restaurant('bobby', 'american')
rest3 = Restaurant('in n out', 'burgers n shiet')

rest1.describe_restauraunt()
rest2.describe_restauraunt()
rest3.describe_restauraunt()

# 9-3 Users
class User:

    def __init__(self, first_name, last_name, city, age):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.age = age

    def describe_user(self):
        print(f"Hello {self.first_name.title()}, the following is a summary of your account: ")
        print(f"\t{self.first_name.title()} is your first name, {self.last_name.title()} is your last name, ")
        print(f"\t{self.age} is your age, and you live in {self.city.title()}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}, thank you for logging in!\n")

page = User('page', 'broughton', 'beaumont', 33)
josh = User('josh', 'kemper', 'beaumont', 32)

page.describe_user()
josh.describe_user()

page.greet_user()
josh.greet_user()
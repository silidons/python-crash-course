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

# 9-4 Number Served
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restauraunt(self):
        print(f"This is {self.restaurant_name.title()}, welcome, we serve {self.cuisine_type.title()} food!")

    def open_restaurant(self):
        print(f"Welcome to {self.restaurant_name.title()}, we're open!")
        
    def set_number_served(self, num_served: int):
        self.number_served = num_served
        
    def increment_number_served(self, num_served: int):
        self.number_served += num_served
        
    def __str__(self):
        return f"Hello, this is {self.restaurant_name.title()}, we have served {self.number_served} people today!"

restaurant = Restaurant('tacos and beer', 'mexican')
print(restaurant.number_served)
restaurant.set_number_served(33)
print(restaurant.number_served)
restaurant.increment_number_served(37)
print(restaurant.number_served)
print(restaurant)

# 9-5 Login Attempt
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
        
page = User('page', 'broughton', 'beaumont', 33)

page.increment_login_attempts()
page.increment_login_attempts()
page.increment_login_attempts()
print(page.login_attempts)
page.reset_login_attempts()
print(page.login_attempts)

# 9-6 Ice Cream Stand

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'banana']
        
    def show_flavors(self):
        print(f'Welcome to {self.restaurant_name.title()}, we have the following flavors:')
        for flavor in self.flavors:
            print(f"\t{flavor.title()}")
            
# yummy = IceCreamStand('Billy', 'Ice Cream')
# print(yummy)
# yummy.show_flavors()

# 9-7 Admin
class Admin(User):
    
    def __init__(self, first_name, last_name, city, age):
        super().__init__(first_name, last_name, city, age)
        self.privileges = Privileges()
            
# 9-8 Privileges
class Privileges:
    
    def __init__(self, privileges=['can delete post', 'can add user', 'is an admin']):
        self.privileges = privileges
        
    def show_privileges(self):
        print("Privileges: ")
        for privilege in self.privileges:
            print(f'\t{privilege.title()}')
            
            
# admin1 = Admin('Page', 'Broughton', 'Beaumont', 33)
# admin1.privileges.show_privileges()

# 9-9 Battery Upgrade
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")
        
    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print(f'Congrats, your battery size is now {self.battery_size}KWh!')
        else:
            print(f'That\'s not an upgrade!')


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
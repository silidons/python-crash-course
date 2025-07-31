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

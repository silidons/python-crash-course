# 8-1 Message
def display_message():
    print("Hello, I'm learning about functions!")
    
display_message()

# 8-2 Favorite Books
def favorite_book(title: str):
    print(f"One of my favorite books is {title.title()}!")
    
favorite_book('alice in wonderland')

# 8-3 T-Shirt
def make_shirt(size: int, message: str):
    print(f'The shirt is size {size} and it says {message}!')
    
make_shirt(15, 'hello bobby')
make_shirt(message='bobby is gay', size=3)

# 8-4 Large Shirts
def make_shirt(size='large', message='I love Python'):
    print(f'The shirt is size {size} and it says {message}!')
    
make_shirt()
make_shirt(size='medium')
make_shirt(size='schmedium', message='bobby is ghay')

# 8-5 Cities
def describe_city(city, country='USA'):
    print(f'{city.title()} is in {country.title()}')

describe_city('boston')
describe_city('madrid', 'spain')
describe_city(country='not usa', city='idk')
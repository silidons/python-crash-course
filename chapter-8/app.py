# # 8-1 Message
# def display_message():
#     print("Hello, I'm learning about functions!")
    
# display_message()

# # 8-2 Favorite Books
# def favorite_book(title: str):
#     print(f"One of my favorite books is {title.title()}!")
    
# favorite_book('alice in wonderland')

# # 8-3 T-Shirt
# def make_shirt(size: int, message: str):
#     print(f'The shirt is size {size} and it says {message}!')
    
# make_shirt(15, 'hello bobby')
# make_shirt(message='bobby is gay', size=3)

# # 8-4 Large Shirts
# def make_shirt(size='large', message='I love Python'):
#     print(f'The shirt is size {size} and it says {message}!')
    
# make_shirt()
# make_shirt(size='medium')
# make_shirt(size='schmedium', message='bobby is ghay')

# # 8-5 Cities
# def describe_city(city, country='USA'):
#     print(f'{city.title()} is in {country.title()}')

# describe_city('boston')
# describe_city('madrid', 'spain')
# describe_city(country='not usa', city='idk')

# # 8-6 City Names
# def city_country(city, country):
#     sent = f'{city.title()}, {country.title()}'
#     return sent

# print(city_country('beaumont', 'california'))
# print(city_country('santiago', 'chile'))
# print(city_country('xiamen', 'china'))

# # 8-7 Album
# def make_album(artist_name, album_title, songs=None):
#     album = {'artist': artist_name.title(), 'album': album_title.title()}
#     if songs:
#         album['songs'] = songs
#         return album
#     return album

# print(make_album('devin townsend', 'ocean machine'))
# print(make_album('devin townsend', 'ziltoid the omniscient'))
# print(make_album('sevendust', 'seasons'))
# print(make_album('lil peep', 'gothboiclique', songs=12))

# # 8-8 User Albums
# def make_album(artist_name, album_title, songs=None):
#     album = {'artist': artist_name.title(), 'album': album_title.title()}
#     if songs:
#         album['songs'] = songs
#         return album
#     return album

# while True:
#     print("\nPlease enter 'q' at any time to quit...")
#     art_name = input("Please input an artists name: ")
#     if art_name == 'q':
#         break
#     alb_name = input("Please input the album title: ")
#     if alb_name == 'q':
#         break
    
    
#     info = make_album(art_name, alb_name)
    
#     print(f'\nDictionary Created! \n\t{info}')
    
# # 8-9 Messages
# def show_messages(texts: list):
#     for text in texts:
#         print(text)
        
# text_messages = ['lol', 'idk', 'yes bro', 'how are you']

# show_messages(text_messages)

# # 8-10 Sending Messages
# def send_messages(texts: list, sent_texts: list):
#     while texts:
#         sent = texts.pop(0)
#         print(f'Now sending {sent}...')
#         sent_texts.append(sent)

# text_messages = ['test1', 'billy', 'lil peep', 'idk bro']
# sent_messages = []

# print(text_messages)
# print(sent_messages)

# send_messages(text_messages, sent_messages)

# print(text_messages)
# print(sent_messages)

# # 8-11 Archived Messages
# def send_messages(texts: list, sent_texts: list):
#     while texts:
#         sent = texts.pop(0)
#         print(f'Now sending {sent}...')
#         sent_texts.append(sent)

# text_messages = ['test1', 'billy', 'lil peep', 'idk bro']
# sent_messages = []

# print(text_messages)
# print(sent_messages)

# send_messages(text_messages[:], sent_messages)

# print(text_messages)
# print(sent_messages)

# # 8-12 Sandwiches
# def build_sandwich(*args):
#     print("You want a sandwich with: ")
#     for arg in args:
#         print(f'-- {arg} --')
        
# build_sandwich('mayo', 'lettuce', 'cheese')
# build_sandwich('provolone', 'ham', 'turkey')
# build_sandwich('mustard', 'cheese', 'bacon')

# # 8-13 User Profile
# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('page', 'broughton', age=33, job='deputy sheriff')

# print(user_profile)

# 8-14 Cars
def make_car(make, model, **car_info):
    car_info['make'] = make
    car_info['model'] = model
    return car_info

my_car = make_car('Ram', '1500 4x4', color='red', milage=28_000)

print(my_car)
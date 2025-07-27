# 6-1 Person
page = {
    'first_name': 'page',
    'last_name': 'broughton',
    'age': 33,
    'city': 'beaumont',
}

for key in page:
    print(page[key])
print()

# 6-2 Favorite Numbers
fav_nums = {
    'sarah': 7,
    'bobby': 11,
    'jimmy': 32,
    'cleveland': 47,
    'billy': 28,
}

for person in fav_nums:
    print(f'{person.title()}\'s favorite number is {fav_nums[person]}!')
print()

# 6-3 Glossary
glossary = {
    'print()':'This function prints output to the terminal.',
    '.title()': 'This function capitalizes the first letter of a string.',
    'for x': 'This for loop, will iterate an item (x) over an iterable object',
    'break': 'This call to break will instantly stop the current loop.',
}

for key in glossary:
    print(f'{key}: {glossary[key]}')
print()

# 6-4 Glossary 2
glossary = {
    'print()':'This function prints output to the terminal.',
    '.title()': 'This function capitalizes the first letter of a string.',
    'for x': 'This for loop, will iterate an item (x) over an iterable object',
    'break': 'This call to break will instantly stop the current loop.',
    'item1': 'this is item 1',
    'item2': 16,
    'item3': 'billy',
    'item4': 'i\'m running out of ideas',
    'item5': 'okay last one'
}

for key, value in glossary.items():
    print(f'{key}: {value}')
print()

# 6-5 Rivers
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for key, value in rivers.items():
    print(f'\nThe {key.title()} river runs through {value.title()}.')
    
# 6-6 Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

poll_takers = ['billy', 'bobby', 'edward', 'jen', 'sally']

for i in poll_takers:
    if i in favorite_languages.keys():
        print(f'{i.title()}, you have already taken the poll!')
    else:
        print(f'Hello {i.title()}, would you please take this poll?')
        
# 6-7 People
page = {
    'first_name': 'page',
    'last_name': 'broughton',
    'age': 33,
    'city': 'beaumont',
    }

josh = {
    'first_name': 'joshua',
    'last_name': 'kemper',
    'age': 32,
    'city': 'beaumont',
}

bianka = {
    'first_name': 'bianka',
    'last_name': 'pastrano',
    'age': 30,
    'city': 'rialto',
}

people = [page, josh, bianka]

for i in people:
    print(f'{i['first_name'].title()} {i['last_name'].title()} is '
          f'{i['age']} years and and lives in {i['city'].title()}.')
    
# 6-8 Pets
pet1 = {
    'name': 'jax',
    'type': 'dog',
    'color': 'black',
    'breed': 'Lab'
}

pet2 = {
    'name': 'billy',
    'type': 'cat',
    'color': 'purple',
    'breed': 'Mixed'
}

pet3 = {
    'name': 'tommy',
    'type': 'cat',
    'color': 'tan',
    'breed': 'Siamese'
}

pet4 = {
    'name': 'ruby',
    'type': 'dog',
    'color': 'white',
    'breed': 'Poodle Mix'
}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    name = pet['name'].title()
    type_an = pet['type']
    color = pet['color']
    breed = pet['breed']
    
    print(f'{name} is a {breed} {type_an} who is the color {color}!\n')
    
# 6-9 Favorite Places
favorite_places = {
    'billy': ['cuba', 'mexico', 'spain'],
    'bobby': ['california', 'new york', 'pennsylvania'],
    'kenny': ['colorado', 'wyoming', 'idaho'],
}

for person, places in favorite_places.items():
    print(f'{person.title()}\'s favorite places are:')
    for location in places:
        print(f'\t{location.title()}')
        
# 6-10 Favorite Numbers
fav_nums = {
    'sarah': [7, 13, 47],
    'bobby': [2, 123, 32],
    'jimmy': [75, 54, 34],
    'cleveland': [74, 13, 64],
    'billy': [5, 35, 64],
}

for person, numbers in fav_nums.items():
    print(f'{person.title()}\'s favorite numbers are:')
    for num in numbers:
        print(f'\t{num}')
        
# 6-11 Cities
cities = {
    'sacramento': {
        'state': 'california',
        'pop': 'a lot',
        'gay': 'very much',
    },
    'chicago': {
        'state': 'illinois',
        'pop': 'less',
        'gay': 'depends',
    },
    'kansas city': {
        'state': 'missouri',
        'pop': 'even less',
        'gay': 'not really',
    }
}

for city, info in cities.items():
    print(f'\nThe city of {city.title()} has the following statistics:')
    print(f'It\'s located in {info['state']}, has {info['pop']} of population '
            f'and has this much gay: {info['gay']}')
    
# 6-12 Extensions

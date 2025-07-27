# 5-3 Alien Colors #1
alien_color = 'green'

if alien_color == 'green':
    print(f'The color is {alien_color}!')
    
if alien_color == 'red':
    print(f'The color is {alien_color}!')
    
# 5-4 Alien Colors #2
alien = 'yellow'

if alien == 'green':
    print(f'You just earned 5 points for shooting the {alien} alien!')
elif alien != 'green':
    print(f'You just earned 10 points for shooting the {alien} alien!')
    
alien = 'green'

if alien == 'green':
    print(f'You just earned 5 points for shooting the {alien} alien!')
elif alien != 'green':
    print(f'You just earned 10 points for shooting the {alien} alien!')
    
# 5-5 Alien Colors #3
alien = 'red'

if alien == 'green':
    print(f'You just earned 5 points for shooting the {alien} alien!')
elif alien == 'yellow':
    print(f'You just earned 10 points for shooting the {alien} alien!')
elif alien == 'red':
    print(f'You just earned 15 points for shooting the {alien} alien!')
    
# 5-6 Stages of Life
age = 33

if age < 2:
    print(f'You\'re a baby!')
elif age < 4:
    print('You\'re a toddler!')
elif age < 13:
    print('You\'re a kid!')
elif age < 20:
    print('You\'re a teenager!')
elif age < 65:
    print('You\'re an adult.')
elif age >= 65:
    print('You\'re an elder.')
    
# 5-7 Favorite Fruit
favorite_fruits = ['banana', 'pineapple', 'watermelon']

fruit_list = ['banana', 'apricot', 'pear', 'watermelon', 'dates']

for i in fruit_list:
    if i in favorite_fruits:
        print(f'You really like {i}s!')
        
# 5-8 Hello Admin
usernames = ['page', 'pageman', 'silidons', 'admin', 'not admin']

for i in usernames:
    if i == 'admin':
        print(f'Hello {i.title()}, would you like to see the status reports?')
    else:
        print(f'Hello {i}, thank you for logging in again.')
        
# 5-9 No Users!

usernames = []

if len(usernames) == 0:
    print('We need to find some users!')

for i in usernames:
    if i == 'admin':
        print(f'Hello {i.title()}, would you like to see the status reports?')
    else:
        print(f'Hello {i}, thank you for logging in again.')
        
# 5-10 Checking Usernames
current_users = ['billy', 'bobby', 'ricky', 'gene', 'hogan']
new_users = ['rick jr', 'helga', 'arnold', 'BiLLy', 'bObby']

current_users = [user.lower() for user in current_users]

for i in new_users:
    if i.lower() in current_users:
        print(f'{i} is already taken - please enter a new username!')
    else:
        print(f'Welcome {i}!')
        
# 5-11 Ordinal Numbers
numbers = [num for num in range(1, 10)]

for num in numbers:
    if num is numbers[0]:
        print(f'{num}st')
    elif num is numbers[1]:
        print(f'{num}nd')
    elif num is numbers[2]:
        print(f'{num}rd')
    else:
        print(f'{num}th')
# 4-10 Slices
random_list = ['my balls', 7, 11, 'yes please', 'billy loves beans']

for i in random_list[:3]:
    print(f'The first three items in the list are: {i}')
    
for i in random_list[2:4]:
    print(f'The middle of the list contains: {i}')
    
for i in random_list[-3:]:
    print(f'The last three iems of the list are: {i}')
    
# 4-11 My Pizza, Your Pizza
pizza = ['pepporoni', 'jalapeno', 'anchovies']

friend_pizza = pizza[:]

pizza.append('extra cheese')
friend_pizza.append('extra sauce')

print('My favorite pizzas are: ')
for i in pizza:
    print(f'{i}')
    
print('My friends favorite pizzas are: ')
for i in friend_pizza:
    print(f'{i}')
    
# 4-13 Buffet
buffet = ('bacon', 'eggs', 'pancakes', 'waffles', 'sausage')
for i in buffet:
    print(i)

buffet = ('bacon', 'not eggs', 'not pancakes', 'waffles', 'sausage')
for i in buffet:
    print(i)
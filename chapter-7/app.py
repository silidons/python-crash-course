# # 7-1 Rental Car
# car = input("What type of rental car would you like?: ")
# print(f'I will try and find you a {car.title()} for your travels.')

# # 7-2 Restaurant Seating
# seating = input("How many seats do you need for your group?: ")
# seating = int(seating)

# if seating > 8:
#     print(f'Please wait, we have to find a table for {seating}.')
# else:
#     print(f'Please come this way, we have a table for {seating} available.')
    
# # 7-3 Multiples of Ten
# num = input("Please provide a number: ")
# num = int(num)

# if num % 10 == 0:
#     print(f'Hey! {num} is a multiple of 10!')
# else:
#     print(f'Sorry, {num} is not a multiple of 10!')
    
# # 7-4 Pizza Toppings
# prompt = ("What pizza toppings would you like?"
#           "Please enter 'quit' to quit the program")

# while toppings:
#     toppings = input(prompt)
#     if toppings == 'quit':
#         break
#     else:
#         print(f'We will add {toppings} to you``r pizza!')
        
# 7-5 Movie Tickets
# prompt = "\nHow old are you? We need to know your age to charge you correctly."
# prompt += "\n\tType 'quit' to quit: "

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)
#     if age < 3:
#         print(f'Your ticket is free, you are {age} years old.')
#     elif age <= 12:
#         print(f'Your ticket is $10, you are {age} years old.')
#     elif age > 12:
#         print(f'Your ticket is $15, you are {age} years old.')

# 7-6 Three Exits
# prompt = "Please provide a number: "

# active = True
# while active:
#     num = input(prompt)
#     if num == 'quit':
#         active = False
#         break
#     try:
#         num = int(num)
#         if num % 10 == 0:
#             print(f'Hey! {num} is a multiple of 10!')
#         else:
#             print(f'Sorry, {num} is not a multiple of 10!')
#     except ValueError:
#         print("Please enter a valid number or 'quit'.")

# 7-8 Deli
# sandwich_orders = [
#     'pastrami', 'meatball', 'turkey', 'blt'
# ]
# finished_sandwiches = []

# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print(f'I made you a {sandwich} sandwhich!')
#     finished_sandwiches.append(sandwich)

# print(f'\nEach sandwich that was made: ')
# for sandwich in finished_sandwiches:
#     print(f'\t{sandwich}!')

# 7-9 No Pastrami
# sandwich_orders = [
#     'pastrami', 'meatball', 'turkey', 'blt', 'pastrami', 'pastrami'
# ]

# finished_sandwiches = []

# print("Uh oh, we ran out of pastrami!!\n")

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print(f'I made you a {sandwich} sandwhich!')
#     finished_sandwiches.append(sandwich)

# print(f'\nEach sandwich that was made: ')
# for sandwich in finished_sandwiches:
#     print(f'\t{sandwich}!')

# 7-10 Dream Vacation
responses = {}

polling_active = True
while polling_active:
    name = input('What is your name?: ')
    response = input('Where would you like to go on vacation?: ')
    
    responses[name] = response
    
    repeat = input('(Y)es or (N)o - continue polling others?: ')
    if repeat == 'no':
        polling_active = False
        
print('---Polling Complete---\n')
for key, value in responses.items():
    print(f'{key.title()} would like to go to: {value}')
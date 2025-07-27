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
prompt = "Please provide a number: "

active = True
while active:
    num = input(prompt)
    if num == 'quit':
        active = False
        break
    try:
        num = int(num)
        if num % 10 == 0:
            print(f'Hey! {num} is a multiple of 10!')
        else:
            print(f'Sorry, {num} is not a multiple of 10!')
    except ValueError:
        print("Please enter a valid number or 'quit'.")
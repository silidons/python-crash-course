from random import randint, choice
import string

# 9-13 Dice
class Die:
    
    def __init__(self, sides=6):
        self.sides = sides
        self.current_side = None
        
    def roll_die(self):
        self.current_side = randint(1, self.sides)
        print(f'The current side is now: {self.current_side}!')
        
my_dice = Die()
my_dice.roll_die()

my_dice = Die(10)
my_dice.roll_die()

my_dice = Die(20)
my_dice.roll_die()

# 9-14 Lottery

numbers = [num for num in range(1, 11)]
letters = [letter for letter in string.ascii_lowercase[:5]]
combined = []

for num in numbers:
    combined.append(num)
for letter in letters:
    combined.append(letter)

winning_ticket = f'{choice(combined)}{choice(combined)}{choice(combined)}{choice(combined)}'

print(f'If your ticket matches {winning_ticket}, you win!')

my_ticket = f'{choice(combined)}{choice(combined)}{choice(combined)}{choice(combined)}'

counter = 1
while my_ticket:
    if my_ticket != winning_ticket:
        my_ticket = f'{choice(combined)}{choice(combined)}{choice(combined)}{choice(combined)}'
        counter += 1
        continue
    else:
        print(f'Congrats, you win! Your ticket: {my_ticket}, winning ticket: {winning_ticket}')
        print(f'Counter: {counter}')
        break
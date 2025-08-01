print("Provide two numbers, and I will add them!")
print("At any time, enter 'q' to quit!")

while True:
    first_number = input('First Number: ')
    if first_number.lower() == 'q':
        break
    second_number = input('Second Number: ')
    if second_number.lower() == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print(f"Error! You didn't enter two numbers!")
    else:
        print(f'{first_number} plus {second_number} equals {answer}!')
    

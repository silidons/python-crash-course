from pathlib import Path

path = Path('chapter-10/guest.txt')


contents = ''
while True:
    print("This program asks for your name.  Enter (Q) if done with the guestbook.")
    answer = input("What is your name?: ")
    if answer == 'q'.lower():
        break
    else:
        contents += f'{answer.title()}\n'

path.write_text(contents)
from pathlib import Path

path = Path('chapter-10/pi_million_digits.txt')
contents = path.read_text()

pi_string = ''

for line in contents.splitlines():
    pi_string += line.lstrip()
    
birthday = input("Enter your birthday, the the form MMDDYY: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi :(")
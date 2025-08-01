from pathlib import Path

path = Path('chapter-10/learning_python.txt')

contents = path.read_text()

#print(contents)

my_string = ''
for line in contents.splitlines():
    my_string += (line + ' ')
    
#print(my_string)

# 10-2 Learning C

print(my_string.lower().replace('python', 'c'.upper()))

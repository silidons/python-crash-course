from pathlib import Path

def count_words(path):
    """Count the approximate amount of words in a text document"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        #print(f'Sorry, the file {path} does not exist.')
        pass
    else:
        # Count the approximate number of words in the file #
        words = contents.split()
        num_words = len(words)
        print(f'The file {path} has about {num_words} words!')
        
path = Path('chapter-10/alice.txt')
count_words(path)

filenames = ['chapter-10/alice.txt', 'chapter-10/siddartha.txt', 'chapter-10/moby_dick.txt',
             'chapter-10/little_women.txt']

for file in filenames:
    path = Path(file)
    count_words(path)
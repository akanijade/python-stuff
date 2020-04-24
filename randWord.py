
import re
from random_word import RandomWords
r = RandomWords()

def run(word):
    regex = re.compile('-')
    if (regex.search(word) == None):
        run(word)
    else:
        print(False)
        word = r.get_random_word
if __name__ == '__main__':
    word = "higher-ups"
    run(word)
    print(word)

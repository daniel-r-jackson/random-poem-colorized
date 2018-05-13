from clint.textui import colored
import random_poem

poem = random_poem.get_poem()

print(colored.red('Here is your poem:\n' + colored.cyan(poem)))

input("Press ENTER to exit.")

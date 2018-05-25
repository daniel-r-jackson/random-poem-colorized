from clint.textui import colored
import random_poem


def getpoem():
    poem = random_poem.get_poem()
    print(colored.red('Here is your poem:\n' + colored.cyan(poem)))
    writefile(poem)
    return poem


def writefile(content):
    filename = 'poem.txt'
    thefile = open(filename, 'w+')
    thefile.write(content)
    thefile.close()
    return filename


getpoem()

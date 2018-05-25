import unittest
import unittest.mock
from clint.textui import colored
from coloredpoem import *


class TestColoredPoem(unittest.TestCase):

    def test_getpoem(self):
        with unittest.mock.patch('random_poem.get_poem', return_value="the poem"):
            poem = getpoem()
            self.assertEqual(poem, "the poem")

    def test_writefile(self):
        content = "junk"
        filename = writefile(content)
        file = open(filename, 'r')
        self.assertEqual(file.read(), content)
        file.close()

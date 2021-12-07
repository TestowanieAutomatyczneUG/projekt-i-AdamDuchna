import unittest

from src.Annife import Annife

class AnnifeEncodeTest(unittest.TestCase):
    def setUp(self):
        assist = Annife()
        self.temp = assist.encode()
    

class AnnifeDecodeTest(unittest.TestCase):
    def setUp(self):
        assist = Annife()
        self.temp = assist.decode()
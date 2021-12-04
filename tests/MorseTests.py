import unittest
from Morse import *
class MorseEncodeTest(unittest.TestCase):
    def setUp(self):
        self.temp = Morse.encode()
    def test_Morse_encode_single_letter(self):
        self.assertEqual(".-",temp("A"))

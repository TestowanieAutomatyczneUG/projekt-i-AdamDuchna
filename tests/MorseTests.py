import unittest
from src.Morse import encode

class MorseEncodeTest(unittest.TestCase):
    def setUp(self):
        self.temp = encode
    def test_Morse_encode_single_letter(self):
        self.assertEqual('.-',self.temp('A'))

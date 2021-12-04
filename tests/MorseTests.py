import unittest
from src.Morse import encode

class MorseEncodeTest(unittest.TestCase):
    def setUp(self):
        self.temp = encode
    def test_Morse_encode_single_letter(self):
        self.assertEqual('.-',self.temp('A'))
    def test_Morse_encode_single_number(self):
        self.assertEqual('.----', self.temp('1'))
    def test_Morse_encode_single_punctuation_mark(self):
        self.assertEqual('.-.-.-', self.temp('.'))
    def test_Morse_encode_intiger(self):
        self.assertRaises(TypeError, self.temp,3)

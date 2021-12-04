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
    def test_Morse_encode_list(self):
        self.assertRaises(TypeError, self.temp, [1,4])
    def test_Morse_encode_double(self):
        self.assertRaises(TypeError, self.temp, 2.65)
    def test_Morse_encode_object(self):
        self.assertRaises(TypeError, self.temp, {})
    def test_Morse_encode_lowercase_word(self):
        self.assertEqual('.-.. .. ...', self.temp('lis'))
    def test_Morse_encode_empty_string(self):
        self.assertEqual('', self.temp(''))

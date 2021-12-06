import unittest

from src.Ceasar import Ceasar


class CeasarEncodeTest(unittest.TestCase):
    def setUp(self):
        assistant = Ceasar()
        self.temp = assistant.encode

    def test_Ceasar_encode_single_uppercase_letter(self):
        self.assertEqual('D', self.temp('A'))

    def test_Ceasar_encode_single_lowercase_letter(self):
        self.assertEqual('f', self.temp('c'))

    def test_Ceasar_encode_non_letter(self):
        self.assertRaises(ValueError, self.temp, '1')

    def test_Ceasar_encode_intiger(self):
        self.assertRaises(TypeError, self.temp, 3)

    def test_Ceasar_encode_list(self):
        self.assertRaises(TypeError, self.temp, [1, 4])

    def test_Ceasar_encode_double(self):
        self.assertRaises(TypeError, self.temp, 2.65)

    def test_Ceasar__object(self):
        self.assertRaises(TypeError, self.temp, {})

    def test_Ceasar_encode_tuple(self):
        self.assertRaises(TypeError, self.temp, ())

    def test_Ceasar_encode_boolean(self):
        self.assertRaises(TypeError, self.temp, True)

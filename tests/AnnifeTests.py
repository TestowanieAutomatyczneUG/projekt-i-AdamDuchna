import unittest

from src.Affine import Affine


class AffineEncodeTest(unittest.TestCase):
    def setUp(self):
        assist = Affine()
        self.temp = assist.encode

    def test_Affine_encode_single_letter(self):
        self.assertEqual('F', self.temp('A',3,5))

    def test_Ceasar_encode_single_lowercase_letter(self):
        self.assertEqual('m', self.temp('c',5,2))

    def test_Ceasar_encode_non_letter(self):
        self.assertRaises(ValueError, self.temp, '1')


class AffineDecodeTest(unittest.TestCase):
    def setUp(self):
        assist = Affine()
        self.temp = assist.decode()

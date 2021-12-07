import unittest

from src.Affine import Affine


class AffineEncodeTest(unittest.TestCase):
    def setUp(self):
        assist = Affine()
        self.temp = assist.encode

    def test_Affine_encode_single_letter(self):
        self.assertEqual('F', self.temp('A',3,5))

    def test_Affine_encode_single_lowercase_letter(self):
        self.assertEqual('m', self.temp('c',5,2))

    def test_Affine_encode_non_letter(self):
        self.assertRaises(ValueError, self.temp, '1',2,3)
        
    def test_Affine_encode_non_letter(self):
        self.assertRaises(ValueError, self.temp, '1',2,3)

    def test_Affine_encode_intiger(self):
        self.assertRaises(TypeError, self.temp, 3,2,3)

    def test_Affine_encode_list(self):
        self.assertRaises(TypeError, self.temp, [1, 4],2,3)

    def test_Affine_encode_double(self):
        self.assertRaises(TypeError, self.temp, 2.65,2,3)

    def test_Affine__object(self):
        self.assertRaises(TypeError, self.temp, {},2,3)

    def test_Affine_encode_tuple(self):
        self.assertRaises(TypeError, self.temp, (),2,3)

    def test_Affine_encode_boolean(self):
        self.assertRaises(TypeError, self.temp, True,2,3)

    def test_Affine_encode_word(self):
        self.assertEqual("xcqg", self.temp("pies",3,4))


class AffineDecodeTest(unittest.TestCase):
    def setUp(self):
        assist = Affine()
        self.temp = assist.decode()

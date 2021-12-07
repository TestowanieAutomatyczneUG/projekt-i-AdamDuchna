import unittest

from src.Affine import Affine


class AffineEncodeTest(unittest.TestCase):
    def setUp(self):
        assist = Affine()
        self.temp = assist.encode()

    def test_Affine_encode_single_letter(self):
        self.assertEqual('.-', self.temp('A'))


class AffineDecodeTest(unittest.TestCase):
    def setUp(self):
        assist = Affine()
        self.temp = assist.decode()

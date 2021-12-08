import unittest

from src.Affine import Affine


class AffineEncodeTest(unittest.TestCase):
    def setUp(self):
        assist = Affine()
        self.temp = assist.encode

    def test_Affine_encode_single_letter(self):
        self.assertEqual('F', self.temp('A', 3, 5))

    def test_Affine_encode_single_lowercase_letter(self):
        self.assertEqual('m', self.temp('c', 5, 2))

    def test_Affine_encode_non_letter(self):
        self.assertRaises(ValueError, self.temp, '1', 2, 3)

    def test_Affine_encode_intiger(self):
        self.assertRaises(TypeError, self.temp, 3, 2, 3)

    def test_Affine_encode_list(self):
        self.assertRaises(TypeError, self.temp, [1, 4], 2, 3)

    def test_Affine_encode_double(self):
        self.assertRaises(TypeError, self.temp, 2.65, 2, 3)

    def test_Affine__object(self):
        self.assertRaises(TypeError, self.temp, {}, 2, 3)

    def test_Affine_encode_tuple(self):
        self.assertRaises(TypeError, self.temp, (), 2, 3)

    def test_Affine_encode_boolean(self):
        self.assertRaises(TypeError, self.temp, True, 2, 3)

    def test_Affine_encode_word(self):
        self.assertEqual("xcqg", self.temp("pies", 3, 4))

    def test_Affine_encode_string_with_non_letters(self):
        self.assertRaises(ValueError, self.temp, "88krzyk!!!", 3, 5)

    def test_Affine_encode_empty_string(self):
        self.assertEqual("", self.temp("", 3, 3))

    def test_Affine_encode_uppercase(self):
        self.assertEqual("BEEB", self.temp("ABBA", 3, 1))

    def test_Affine_encode_letter_out_of_range(self):
        self.assertEqual("xghe", self.temp("zeta", 7, 4))

    def test_Affine_encode_mixed_cases_and_out_of_range(self):
        self.assertEqual("NakiPP OkePPHH", self.temp("ZmioTT WiaTTRR", 17, 4))

    def test_Affine_encode_whole_alphabet(self):
        self.assertEqual("exq atm jjpibugzsljcv oh fyrkd", self.temp("abc ijk ddrstuwxyzdef gh lmnop", 19, 4))

    def test_Affine_encode_whole_alphabet_uppercase(self):
        self.assertEqual("GDA IFC XXHEBYSPMJXUR OL ZWTQN", self.temp("ABC IJK DDRSTUWXYZDEF GH LMNOP", 23, 6))

    def test_Affine_encode_special_signs_and_letters(self):
        self.assertRaises(ValueError, self.temp, "abc i "F" ?SD (###  jk ddrstuwxy !!! ! ! zdef gh lmnop", 3, 7)

    def test_Affine_encode_a_out_of_range(self):
        self.assertRaises(ValueError, self.temp, "test", 120, 7)

    def test_Affine_encode_a_non_prime(self):
        self.assertRaises(ValueError, self.temp, "test", 4, 2)


class AffineDecodeTest(unittest.TestCase):
    def setUp(self):
        assist = Affine()
        self.temp = assist.decode

if __name__ == "__main__":
    unittest.main()
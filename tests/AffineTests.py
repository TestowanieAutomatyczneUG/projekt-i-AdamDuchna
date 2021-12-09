import unittest

from nose.tools import assert_equal
from parameterized import parameterized_class

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

    def tearDown(self):
        self.temp = None


@parameterized_class(('text', 'a', 'b', 'expected'), [
    ('', 5, 3, ''),
    ('tryton', 29, 25, 'eytepm'),
    ('ToSTER', 7, 14, 'RiKRQD'),
    ('TOSTOWNICA', 11, 4, 'FCUFCMROAE'),
    ('abcdefghijklmnopqrstuvwxyz', 19, 5, 'fyrkdwpibungzslexqjcvohatm'),
    ('ZXCVBNMJIKOLPYGHTUDFSATEQWR', 59, 65, 'GSBEUATYRFHMOZDKQXIWJNQPVLC'),

])
class AffineEncodeParameterizedClassTesting(unittest.TestCase):
    def setUp(self):
        assist = Affine()
        self.temp = assist.encode

    def test_Affine_encode_asserts_equal(self):
        assert_equal(self.temp(self.text, self.a, self.b), self.expected)


class AffineDecodeTest(unittest.TestCase):
    def setUp(self):
        assist = Affine()
        self.temp = assist.decode

    def test_Affine_decode_single_letter(self):
        self.assertEqual('A', self.temp('F', 3, 5))

    def test_Affine_decode_single_lowercase_letter(self):
        self.assertEqual('c', self.temp('m', 5, 2))

    def test_Affine_decode_non_letter(self):
        self.assertRaises(ValueError, self.temp, '1', 2, 3)

    def test_Affine_decode_intiger(self):
        self.assertRaises(TypeError, self.temp, 3, 2, 3)

    def test_Affine_decode_list(self):
        self.assertRaises(TypeError, self.temp, [1, 4], 2, 3)

    def test_Affine_decode_double(self):
        self.assertRaises(TypeError, self.temp, 2.65, 2, 3)

    def test_Affine_decode_object(self):
        self.assertRaises(TypeError, self.temp, {}, 2, 3)

    def test_Affine_decode_tuple(self):
        self.assertRaises(TypeError, self.temp, (), 2, 3)

    def test_Affine_decode_boolean(self):
        self.assertRaises(TypeError, self.temp, True, 2, 3)

    def test_Affine_decode_word(self):
        self.assertEqual("pies", self.temp("xcqg", 3, 4))

    def test_Affine_decode_string_with_non_letters(self):
        self.assertRaises(ValueError, self.temp, "88ff!!!", 3, 5)

    def test_Affine_decode_empty_string(self):
        self.assertEqual("", self.temp("", 3, 3))

    def test_Affine_decode_uppercase(self):
        self.assertEqual("ABBA", self.temp("BEEB", 3, 1))

    def test_Affine_decode_letter_out_of_range(self):
        self.assertEqual("zeta", self.temp("xghe", 7, 4))

    def test_Affine_decode_mixed_cases_and_out_of_range(self):
        self.assertEqual("ZmioTT WiaTTRR", self.temp("NakiPP OkePPHH", 17, 4))

    def test_Affine_decode_whole_alphabet(self):
        self.assertEqual("abc ijk ddrstuwxyzdef gh lmnop", self.temp("exq atm jjpibugzsljcv oh fyrkd", 19, 4))

    def test_Affine_decode_whole_alphabet_uppercase(self):
        self.assertEqual("ABC IJK DDRSTUWXYZDEF GH LMNOP", self.temp("GDA IFC XXHEBYSPMJXUR OL ZWTQN", 23, 6))

    def test_Affine_decode_special_signs_and_letters(self):
        self.assertRaises(ValueError, self.temp, "abc i "F" ?SD (###  jk ddrstuwxy !!! ! ! zdef gh lmnop", 3, 7)

    def test_Affine_decode_a_out_of_range(self):
        self.assertRaises(ValueError, self.temp, "test", 120, 7)

    def test_Affine_decode_a_non_prime(self):
        self.assertRaises(ValueError, self.temp, "test", 4, 2)

    def tearDown(self):
        self.temp = None


if __name__ == "__main__":
    unittest.main()

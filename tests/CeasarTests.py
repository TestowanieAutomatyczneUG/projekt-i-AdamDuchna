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

    def test_Ceasar_encode_word(self):
        self.assertEqual("nrw", self.temp("kot"))

    def test_Ceasar_encode_string_with_non_letters(self):
        self.assertRaises(ValueError, self.temp, "88krzyk!!!")

    def test_Ceasar_encode_empty_string(self):
        self.assertEqual("", self.temp(""))

    def test_Ceasar_encode_uppercase(self):
        self.assertEqual("YHQGHWWD", self.temp("VENDETTA"))

    def test_Ceasar_encode_letter_out_of_range(self):
        self.assertEqual("chwd", self.temp("zeta"))

    def test_Ceasar_encode_mixed_cases_and_out_of_range(self):
        self.assertEqual("CuBz VCCbENl", self.temp("ZrYw SZZyBKi"))


class CeasarDecodeTest(unittest.TestCase):
    def setUp(self):
        assistant = Ceasar()
        self.temp = assistant.decode

    def test_Ceasar_decode_single_uppercase_letter(self):
        self.assertEqual('A', self.temp('D'))

    def test_Ceasar_decode_single_lowercase_letter(self):
        self.assertEqual('c', self.temp('f'))

    def test_Ceasar_decode_non_letter(self):
        self.assertRaises(ValueError, self.temp, '1')

    def test_Ceasar_decode_intiger(self):
        self.assertRaises(TypeError, self.temp, 3)

    def test_Ceasar_decode_list(self):
        self.assertRaises(TypeError, self.temp, [1, 4])

    def test_Ceasar_decode_double(self):
        self.assertRaises(TypeError, self.temp, 2.65)

    def test_Ceasar__object(self):
        self.assertRaises(TypeError, self.temp, {})

    def test_Ceasar_decode_tuple(self):
        self.assertRaises(TypeError, self.temp, ())

    def test_Ceasar_decode_boolean(self):
        self.assertRaises(TypeError, self.temp, True)
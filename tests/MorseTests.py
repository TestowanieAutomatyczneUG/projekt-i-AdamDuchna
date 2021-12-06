import unittest

from hamcrest import *

from src.Morse import Morse


class MorseEncodeTest(unittest.TestCase):
    def setUp(self):
        assistant = Morse()
        self.temp = assistant.encode

    def test_Morse_encode_single_letter(self):
        self.assertEqual('.-', self.temp('A'))

    def test_Morse_encode_single_number(self):
        self.assertEqual('.----', self.temp('1'))

    def test_Morse_encode_single_punctuation_mark(self):
        self.assertEqual('.-.-.-', self.temp('.'))

    def test_Morse_encode_intiger(self):
        self.assertRaises(TypeError, self.temp, 3)

    def test_Morse_encode_list(self):
        self.assertRaises(TypeError, self.temp, [1, 4])

    def test_Morse_encode_double(self):
        self.assertRaises(TypeError, self.temp, 2.65)

    def test_Morse_encode_object(self):
        self.assertRaises(TypeError, self.temp, {})

    def test_Morse_encode_tuple(self):
        self.assertRaises(TypeError, self.temp, ())

    def test_Morse_encode_boolean(self):
        self.assertRaises(TypeError, self.temp, True)

    def test_Morse_encode_lowercase_word(self):
        self.assertEqual('.-.. .. ...', self.temp('lis'))

    def test_Morse_encode_empty_string(self):
        self.assertEqual('', self.temp(''))

    def test_Morse_encode_letters_numbers(self):
        self.assertEqual('.-.. .. --.. .- -.-  ....- ..... .....  -.-. ---  ..---', self.temp('lizak 455 co 2'))

    def test_Morse_encode_letters_punctuation_mark(self):
        self.assertEqual('.--. .. . --..--  ... .-..-. . -.- -.-.-- .-..-.', self.temp('pie, s"ek!"'))

    def test_Morse_encode_numbers_punctuation_mark(self):
        self.assertEqual('.---- ..... -.... --... -.-.-- .-.-.- .-.-.- .-.-.-', self.temp('1567!...'))

    def test_Morse_encode_all_characters(self):
        self.assertEqual('.- -... -----  -.-. -.. . ..-. .---- ..--- ...-- --..--  --. -.--. .... -.--.- .. .--- .-..-.'
                         ' -.- ..... .-..-. .-.-.- -.... .-.. -- --- -..-. -..-. -....- -. ..--.. .--. -.-.-- ---... ..'
                         '..- ---.. --.- .-. ... --... ----. - ..- ...-  .-- -..- -.-- --..',
                         self.temp('ab0 cdef123, g(h)ij"k5".6lmo//-n?p!:48qrs79tuv wxyz'))


class MorseEncodeHamcrestTest(unittest.TestCase):
    def setUp(self):
        assistant = Morse()
        self.temp = assistant.encode

    def test_Morse_encode_return_str(self):
        assert_that(self.temp('gxggg23'), instance_of(str))

    def test_Morse_encode_correct_length(self):
        assert_that(self.temp('dgxggrs 24'), has_length(41))

    def test_Morse_encode_start_of_string(self):
        assert_that(self.temp('leonkot !.4'), starts_with('.-.. . ---'))

    def test_Morse_encode_regex_only_dot_dash_space(self):
        assert_that(self.temp('pies "Max" 33!!..'), matches_regexp('[ .-]*'))


class MorseDecodeTest(unittest.TestCase):
    def setUp(self):
        assistant = Morse()
        self.temp = assistant.decode

    def test_Morse_decode_single_letter(self):
        self.assertEqual('D', self.temp('-..'))

    def test_Morse_decode_single_number(self):
        self.assertEqual('4', self.temp('....-'))

    def test_Morse_decode_single_punctuation_mark(self):
        self.assertEqual('!', self.temp('-.-.--'))

    def test_Morse_decode_intiger(self):
        self.assertRaises(TypeError, self.temp, 3)

    def test_Morse_decode_list(self):
        self.assertRaises(TypeError, self.temp, [1, 4])

    def test_Morse_decode_double(self):
        self.assertRaises(TypeError, self.temp, 2.65)

    def test_Morse_decode_object(self):
        self.assertRaises(TypeError, self.temp, {})

    def test_Morse_decode_tuple(self):
        self.assertRaises(TypeError, self.temp, ())

    def test_Morse_decode_boolean(self):
        self.assertRaises(TypeError, self.temp, True)

    def test_Morse_decode_not_in_morse(self):
        self.assertRaises(ValueError, self.temp, "hiob 222033321")

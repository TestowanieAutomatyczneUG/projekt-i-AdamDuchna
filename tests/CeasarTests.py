import unittest
import pytest
from src.Ceasar import Ceasar

class CeasarEncodeTest(unittest.TestCase):
    def setUp(self):
        assistant = Ceasar()
        self.temp = assistant.encode
    def test_Ceasar_encode_single_uppercase_letter(self):
        self.assertEqual('D', self.temp('A'))
    def test_Ceasar_encode_single_uowercase_letter(self):
        self.assertEqual('f', self.temp('c'))


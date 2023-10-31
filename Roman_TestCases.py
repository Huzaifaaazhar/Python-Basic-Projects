import unittest

from converter import Converter

class TestConverter(unittest.TestCase):
    def test_conversion_for_roman_numeral_I(self):
        result = Converter().convert(1)
        self.assertEqual(result, "I", "1 should be converted to 'I'")

    def test_conversion_for_roman_numeral_IV(self):
        result = Converter().convert(4)
        self.assertEqual(result, "IV", "4 should be converted to 'IV'")

    def test_conversion_for_roman_numeral_V(self):
        result = Converter().convert(5)
        self.assertEqual(result, "V", "5 should be converted to 'V'")

    def test_conversion_for_roman_numeral_VI(self):
        result = Converter().convert(6)
        self.assertEqual(result, "VI", "6 should be converted to 'VI'")

    def test_conversion_for_roman_numeral_IX(self):
        result = Converter().convert(9)
        self.assertEqual(result, "IX", "9 should be converted to 'IX'")

    def test_conversion_for_roman_numeral_X(self):
        result = Converter().convert(10)
        self.assertEqual(result, "X", "10 should be converted to 'X'")

if __name__ == '__main__':
    unittest.main()

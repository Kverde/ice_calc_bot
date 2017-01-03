import unittest

from ks_math import MathParser

class TestParser(unittest.TestCase):

    def calc(self, text):
        return  MathParser(text).parse()

    def test_empty(self):
        self.assertEqual(0, self.calc(''))

    def test_main(self):
        self.assertEqual(6, self.calc('2 + 2 * 2'))
        self.assertEqual(23, self.calc('23'))
        self.assertEqual(20.35, self.calc('12.12 + 0.23 + 3. + 5'))
        self.assertEqual(2.0, self.calc('4 / 2'))
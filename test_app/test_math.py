import unittest
import math

from source.ks_math import MathParser

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

    def test_bracket(self):
        self.assertEqual(8, self.calc('2 * (2 + 2)'))
        self.assertEqual(33 * 5, self.calc(' (33 * (5))'))
        self.assertEqual(10, self.calc('3 + (2 * 2) + ((3))'))

    def test_pow(self):
        self.assertEqual(1024, self.calc('2 ^ 10'))
        self.assertEqual(5 ** 5, self.calc('5 ^ + (2 + 3)'))
        self.assertEqual(0.25, self.calc('2 ^ - 2'))

    def test_factorial(self):
        self.assertEqual(1 * 2 * 3 * 4 * 5, self.calc('5!'))
        self.assertEqual(math.factorial(10), self.calc('(5 + 5)!'))

    def test_consts(self):
        self.assertEqual(math.pi, self.calc('pi'))
        self.assertEqual(math.e, self.calc('e'))
        self.assertEqual(math.pi * 2, self.calc('+ pi * 2'))


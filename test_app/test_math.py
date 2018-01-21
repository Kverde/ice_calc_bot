import unittest
import math

from source.ks_math import MathParser

class TestParser(unittest.TestCase):

    def calc(self, text, base = 10):
        return  MathParser(text).solve(base)

    def test_empty(self):
        self.assertEqual(0, self.calc(''))

    def test_main(self):
        self.assertEqual(6, self.calc('2 + 2 * 2'))
        self.assertEqual(23, self.calc('23'))
        self.assertEqual(20.35, self.calc('12.12 + 0.23 + 3. + 5'))

        self.assertEqual('2', str(self.calc('4 / 2')))

        self.assertEqual(2, self.calc('5 // 2'))
        self.assertEqual(2, self.calc('5 div 2'))
        self.assertEqual(1, self.calc('5 mod 2'))


        self.assertEqual(10, self.calc('5 * 2'))
        self.assertEqual(6, self.calc('2 × 3'))

        self.assertEqual(5, self.calc('10 / 2'))
        self.assertEqual(5, self.calc('10 ÷ 2'))
        self.assertEqual(5, self.calc('10 : 2'))



    def test_proc(self):
        self.assertEqual(105, self.calc('100 +% 5'))
        self.assertEqual(75, self.calc('100 -% 25'))
        self.assertEqual(35, self.calc('100 *% 35'))



    def test_bracket(self):
        self.assertEqual(8, self.calc('2 * (2 + 2)'))
        self.assertEqual(33 * 5, self.calc(' (33 * (5))'))
        self.assertEqual(10, self.calc('3 + (2 * 2) + ((3))'))

    def test_pow(self):
        self.assertEqual(1024, self.calc('2 ^ 10'))
        self.assertEqual(5 ** 5, self.calc('5 ^ + (2 + 3)'))
        self.assertEqual(0.25, self.calc('2 ^ - 2'))

        self.assertEqual(0.25, self.calc('2 ** - 2'))
        self.assertEqual(5 ** 5, self.calc('5 ** + (2 + 3)'))

    def test_factorial(self):
        self.assertEqual(1 * 2 * 3 * 4 * 5, self.calc('5!'))
        self.assertEqual(math.factorial(10), self.calc('(5 + 5)!'))

    def test_consts(self):
        self.assertEqual(math.pi, self.calc('pi'))
        self.assertEqual(math.e, self.calc('e'))
        self.assertEqual(math.pi * 2, self.calc('+ pi * 2'))

    def test_error(self):
        self.assertEqual('Error: неизвестный иднтификатор "ss"', self.calc('ss 22 z'))
        self.assertEqual('Error: неизвестный иднтификатор "z"', self.calc('22 z'))

        self.assertEqual('Error: Неизвесный символ ord(#) = 35', self.calc('55.55 #'))


    def test_func(self):
        self.assertEqual(math.sin(90), self.calc('sinr(90)'))
        self.assertEqual(math.cos(90), self.calc('cosr(90)'))
        self.assertEqual(math.sqrt(64) + 33 + math.pi, self.calc('sqrt(64) + 33 + pi'))
        self.assertEqual(math.tan(90), self.calc('tanr(90)'))
        self.assertEqual(math.fabs(90), self.calc('abs(90)'))

        self.assertEqual(math.sin(math.radians(90)), self.calc('sin(90)'))
        self.assertEqual(math.cos(math.radians(90)), self.calc('cos(90)'))
        self.assertEqual(math.sqrt(64) + 33 + math.pi, self.calc('sqrt(64) + 33 + pi'))
        self.assertEqual(math.tan(math.radians(90)), self.calc('tan(90)'))
        self.assertEqual(math.fabs(90), self.calc('abs(90)'))


    def test_base(self):
        self.assertEqual('0b11', self.calc('3', 2))
        self.assertEqual('0o3', self.calc('3', 8))
        self.assertEqual('0xA', self.calc('10', 16))

    def test_log(self):
        self.assertEqual(2, self.calc('log(100)'))
        self.assertEqual(3, self.calc('log(1000)'))
        self.assertEqual(1, self.calc('log(10)'))
        self.assertEqual(0, self.calc('log(1)'))

        self.assertEqual(2, self.calc('log10(100)'))
        self.assertEqual(3, self.calc('log10(1000)'))
        self.assertEqual(1, self.calc('log10(10)'))
        self.assertEqual(0, self.calc('log10(1)'))

        self.assertEqual(1, self.calc('log2(2)'))
        self.assertEqual(5, self.calc('log2(32)'))
        self.assertEqual(0, self.calc('log2(1)'))

        self.assertEqual(math.log(35), self.calc('ln(35)'))
        self.assertEqual(math.log(120), self.calc('ln(120)'))



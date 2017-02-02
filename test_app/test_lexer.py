import unittest

from source.ks_lexer import Lexer

class TestLexer(unittest.TestCase):
    def getList(self, text):
        return list(Lexer(text))

    def test_number(self):
        self.assertEqual([13], self.getList('13'))
        self.assertEqual([1], self.getList('1'))
        self.assertEqual([0], self.getList(' 0 '))
        self.assertEqual([14.0], self.getList('14.'))
        self.assertEqual([15.0], self.getList('15,'))


        self.assertEqual([8], self.getList('010'))
        self.assertEqual([10], self.getList('012'))

        self.assertEqual([5], self.getList('0x5'))
        self.assertEqual([16], self.getList('0X10'))



        self.assertEqual([55.55, 87857], self.getList('55.55 87857'))
        self.assertEqual([1234567.985645], self.getList('1234567,985645'))

    def test_empty(self):
        self.assertEqual([], self.getList(''))
        self.assertEqual([], self.getList('  '))
        self.assertEqual([], self.getList(' \t '))

    def test_math(self):
        self.assertEqual([12, '+', 34, '-'], self.getList('12 + 34 -'))
        self.assertEqual([1.2, '/', '/', '*', 3], self.getList('1.2 / / * 3'))
        self.assertEqual([1, '(', '(', ')'], self.getList('1 ( ( )'))

    def test_ident(self):
        self.assertEqual(['asd'], self.getList('asd'))
        self.assertEqual(['кцо', 'фы'], self.getList('кцо фы'))
        self.assertEqual([1.2, '+', 'pi', '-', 'z35'], self.getList('1.2 + pi - z35'))




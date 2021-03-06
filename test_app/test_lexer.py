import unittest

from source.ks_lexer import Lexer, LexerError

class TestLexer(unittest.TestCase):
    def getList(self, text):
        return list(Lexer(text))

    def testError(self):
        self.assertRaises(LexerError, self.getList, '55.55 #')

    def test_number(self):
        self.assertEqual([13], self.getList('13'))
        self.assertEqual([1], self.getList('1'))
        self.assertEqual([0], self.getList(' 0 '))
        self.assertEqual([14.0], self.getList('14.'))
        self.assertEqual([15.0], self.getList('15,'))


        self.assertEqual([8], self.getList('0o10'))
        self.assertEqual([10], self.getList('0O12'))

        self.assertEqual([5], self.getList('0x5'))
        self.assertEqual([16], self.getList('0X10'))

        self.assertEqual([1], self.getList('0b1'))
        self.assertEqual([5], self.getList('0B101'))

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

        self.assertEqual(['dsa', 'pi', 'div'], self.getList('DSa pi DIV'))


    def test_operators(self):
        self.assertEqual([2, '**', 3], self.getList('2**3'))
        self.assertEqual([2, '//', '/', 3], self.getList('2///3'))
        self.assertEqual([2, 'div', 3], self.getList('2 div 3'))
        self.assertEqual([2, 'mod', 3], self.getList('2 mod 3'))

        self.assertEqual([2, '-%', 3], self.getList('2 -% 3'))
        self.assertEqual([2, '+%', 3], self.getList('2 +% 3'))
        self.assertEqual([2, '*%', 3], self.getList('2 *% 3'))







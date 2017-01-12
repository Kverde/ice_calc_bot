import unittest

from source.ks_lexer import Lexer

class TestLexer(unittest.TestCase):
    def getList(self, text):
        return list(Lexer(text))

    def test_number(self):
        self.assertEqual([12], self.getList('12'))
        self.assertEqual([1], self.getList('1'))
        self.assertEqual([0], self.getList(' 0 '))
        self.assertEqual([12.0], self.getList('12.'))

        self.assertEqual([55.55, 87857], self.getList('55.55 87857'))

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




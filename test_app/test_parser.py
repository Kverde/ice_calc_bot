import unittest

from source.ks_parser import Parser

class TestParser(unittest.TestCase):
    TEST_TEXT = 'abc'

    def test_create(self):
        parser = Parser(TestParser.TEST_TEXT)

        self.assertEqual(TestParser.TEST_TEXT, parser.text)
        self.assertEqual(0, parser.index)


    def test_curent(self):
        parser = Parser(TestParser.TEST_TEXT)

        self.assertEqual(TestParser.TEST_TEXT[0], parser.current())
        parser.index = 2
        self.assertEqual(TestParser.TEST_TEXT[2], parser.current())
        parser.index = 3
        self.assertEqual('', parser.current())

    def test_next(self):
        parser = Parser(TestParser.TEST_TEXT)

        self.assertEqual(0, parser.index)
        parser.next()
        self.assertEqual(1, parser.index)
        parser.next()
        self.assertEqual(2, parser.index)
        parser.next()
        self.assertEqual(3, parser.index)
        parser.next()
        self.assertEqual(3, parser.index)

    def test_eof(self):
        parser = Parser(TestParser.TEST_TEXT)

        self.assertFalse(parser.eof())
        parser.index = 2
        self.assertFalse(parser.eof())
        parser.index = 3
        self.assertTrue(parser.eof())


    def test_skipSpace(self):
        parser = Parser(' 2 \t d')

        parser.skipSpaces()
        self.assertEqual(1, parser.index)
        parser.next()
        parser.skipSpaces()
        self.assertEqual(5, parser.index)

        parser.skipSpaces()
        self.assertEqual(5, parser.index)

        parser.next()
        parser.skipSpaces()
        self.assertEqual(6, parser.index)

    def test_copy(self):
        parser = Parser(TestParser.TEST_TEXT)

        parser.index = 2

        self.assertEqual(TestParser.TEST_TEXT[0:2], parser.copy(0))
        self.assertEqual(TestParser.TEST_TEXT[1:2], parser.copy(1))


    def test_skipWhile(self):
        parser = Parser('123')
        parser.skipWhile(lambda ch : ch.isnumeric())
        self.assertEqual(3, parser.index)

        parser = Parser('.,t 4')
        parser.skipWhile(lambda ch : not ch.isnumeric())
        self.assertEqual(4, parser.index)

        parser = Parser('dsf')
        parser.skipWhile(lambda ch : ch.isnumeric())
        self.assertEqual(0, parser.index)
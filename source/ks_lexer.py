
from source.ks_parser import Parser

class Lexer():
    NUMBERS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    TERM_OPERATOR = {'+', '-'}
    FACTOR_OPERATOR = {'*', '/'}
    BRACKED = {'(', ')'}
    OTHER_OPERATOR = {'^', '!'}
    DECIMAL_SEPARATOR = {'.', ','}
    HEX_FLAG = {'x', 'X'}
    OCT_FLAG = {'o', 'O'}
    BIN_FLAG = {'b', 'B'}
    HEX_DIGIT = ['a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']


    def __init__(self, text):
        self.parser = Parser(text)

    def __iter__(self):
        while not self.parser.eof():
            self.parser.skipSpaces()

            if self.parser.eof():
                break

            ch = self.parser.current()
            if ch in Lexer.TERM_OPERATOR \
                    or ch in Lexer.FACTOR_OPERATOR \
                    or ch in Lexer.BRACKED \
                    or ch in Lexer.OTHER_OPERATOR:
                res = ch
                self.parser.next()
            elif ch in Lexer.NUMBERS:
                res = self.parse_number()
            elif ch.isalpha():
                res = self.parse_ident()
            else:
                return 'Неизвесный символ ord(' + ch + ') = ' + str(ord(ch))

            yield res

    def parse_hex(self):
        start_index = self.parser.index

        self.parser.skipWhile(lambda ch: ch in Lexer.NUMBERS or ch in Lexer.HEX_DIGIT)

        str = self.parser.copy(start_index)
        res = int(str, 16)

        return res


    def parse_oct(self):
        start_index = self.parser.index

        self.parser.skipWhile(lambda ch: ch in Lexer.NUMBERS)

        str = self.parser.copy(start_index)
        res = int(str, 8)

        return res

    def parse_bin(self):
        start_index = self.parser.index

        self.parser.skipWhile(lambda ch: ch in Lexer.NUMBERS)

        str = self.parser.copy(start_index)
        res = int(str, 2)

        return res

    def parse_number(self):
        start_index = self.parser.index

        if self.parser.current() == '0':
            self.parser.next()

            if self.parser.current() in Lexer.HEX_FLAG:
                self.parser.next()
                return self.parse_hex()
            elif self.parser.current() in Lexer.OCT_FLAG:
                self.parser.next()
                return self.parse_oct()
            elif self.parser.current() in Lexer.BIN_FLAG:
                self.parser.next()
                return self.parse_bin()

        self.parser.skipWhile(lambda ch : ch in Lexer.NUMBERS)

        if self.parser.current() in Lexer.DECIMAL_SEPARATOR:
            self.parser.next()

            self.parser.skipWhile(lambda ch: ch in Lexer.NUMBERS)

            res = self.parser.copy(start_index).replace(',', '.')
            res = float(res)
        else:
            str = self.parser.copy(start_index)
            res = int(str)

        return res

    def parse_ident(self):
        start_index = self.parser.index
        self.parser.next()

        self.parser.skipWhile(lambda ch : ch.isalnum())

        return self.parser.copy(start_index)


if __name__ == '__main__':
    print(list(Lexer('342.44 + 2424 - 3')))




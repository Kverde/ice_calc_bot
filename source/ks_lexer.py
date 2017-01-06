
from source.ks_parser import Parser

class Lexer():
    NUMBERS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    TERM_OPERATOR = {'+', '-'}
    FACTOR_OPERATOR = {'*', '/'}
    BRACKED = {'(', ')'}
    OTHER_OPERATOR = {'^'}

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
            else:
                return 'Неизвесный символ ord(' + ch + ') = ' + str(ord(ch))

            yield res

    def parse_number(self):
        start_index = self.parser.index

        self.parser.skipWhile(lambda ch : ch in Lexer.NUMBERS)

        if self.parser.current() == '.':
            self.parser.next()

            self.parser.skipWhile(lambda ch: ch in Lexer.NUMBERS)

            res = float(self.parser.copy(start_index))
        else:
            res = int(self.parser.copy(start_index))

        return res


if __name__ == '__main__':
    print(list(Lexer('342.44 + 2424 - 3')))




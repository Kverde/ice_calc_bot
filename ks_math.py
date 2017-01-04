import operator

from ks_lexer import Lexer
from ks_memiter import MemIter

class SyntaxEror(Exception):
    pass

class MathParser():
    OPERATOR1 = {
        '+': operator.add,
        '-': operator.sub
    }

    OPERATOR2 = {
        '*': operator.mul,
        '/': operator.truediv
    }

    UNARY_OPERATOR = {
        '+': operator.pos,
        '-': operator.neg
    }

    def __init__(self, text):
        self.index = 0
        self.lexer = MemIter(Lexer(text))

    def mathExpr(self):
        res = self.term()

        while self.lexer.cur in MathParser.OPERATOR1:
            operator = MathParser.OPERATOR1[self.lexer.cur]
            self.lexer.next()

            arg = self.term()

            res = operator(res, arg)
        return res

    def term(self):
        res = self.factor()

        while self.lexer.cur in MathParser.OPERATOR2:
            operator = MathParser.OPERATOR2[self.lexer.cur]
            self.lexer.next()

            arg = self.factor()

            res = operator(res, arg)
        return res

    def factor(self):
        if self.lexer.cur in MathParser.UNARY_OPERATOR:
            operator = MathParser.UNARY_OPERATOR[self.lexer.cur]
            self.lexer.next()
            return operator(self.factor())

        return self.base()

    def base(self):
        res = self.lexer.cur

        if res == '(':
            self.lexer.next()
            res = self.mathExpr()

            if self.lexer.cur == ')':
                self.lexer.next()
                return res
            raise SyntaxEror("Ошибка: ожидаеся закрывающая скобка")

        if type(res) == int or type(res) == float:
            self.lexer.next()
            return res

        raise SyntaxEror('Ошибка: неизвестный иднтификатор "{}"'.format(res))

    def parse(self):
        if self.lexer.cur is None:
            return 0
        else:
            try:
                return self.mathExpr()
            except Exception as e:
                return str(e)

if __name__ == '__main__':
    p = MathParser('2 + 2 * + 2 dfd')
    print(p.parse())

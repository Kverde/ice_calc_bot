import operator
import math

from source.ks_memiter import MemIter

from source.ks_lexer import Lexer

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

    MATH_CONST = {
        'pi': math.pi,
        'e': math.e
    }

    MATH_FUNCTION = {
        'sin': math.sin,
        'cos': math.cos,
        'sqrt': math.sqrt,
        'tan': math.tan,
        'abs': math.fabs
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
            res = operator(self.factor())
        else:
            res = self.base()

        if self.lexer.cur == '!':
            self.lexer.next()
            res = math.factorial(res)

        while self.lexer.cur == '^':
            self.lexer.next()
            res = res ** self.factor()

        return res

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

        if type(res) == str:
            if res in self.MATH_CONST:
                self.lexer.next()
                res = self.MATH_CONST[res]
                return res
            elif res in self.MATH_FUNCTION:
                self.lexer.next()

                if not self.lexer.cur == '(':
                    raise SyntaxEror('Ошибка: ожидается символ "(", обнаружен "{}"'.format(self.lexer.cur))
                self.lexer.next()

                arg = self.mathExpr()

                if not self.lexer.cur == ')':
                    raise SyntaxEror('Ошибка: ожидается символ "(", обнаружен "{}"'.format(self.lexer.cur))
                self.lexer.next()

                func = self.MATH_FUNCTION[res]
                return func(arg)
            else:
                raise SyntaxEror('Ошибка: неизвестный иднтификатор "{}"'.format(res))

        raise SyntaxEror('Ошибка: неизвестная лексема "{}"'.format(res))

    def parse(self):
        if self.lexer.cur is None:
            return 0
        else:
            try:
                res = self.mathExpr()

                if not self.lexer.cur == None:
                    raise SyntaxEror('Ошибка: неизвестный иднтификатор "{}"'.format(self.lexer.cur))

                return res

            except Exception as e:
                return str(e)

if __name__ == '__main__':
    p = MathParser('2 + 2 * + 2 dfd')
    print(p.parse())

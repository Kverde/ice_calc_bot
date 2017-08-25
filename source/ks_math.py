import operator
import math

from source.ks_memiter import MemIter

from source.ks_lexer import Lexer

class SyntaxEror(Exception):
    pass

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def asin(x):
    return math.degrees(math.asin(x))

def acos(x):
    return math.degrees(math.acos(x))

def atan(x):
    return math.degrees(math.atan(x))


def mul_proc(a, b):
    return a * (b / 100)

def add_proc(a, b):
    return a + a * (b / 100)

def sub_proc(a, b):
    return a - a * (b / 100)

def ln(x):
    return math.log(x)


class MathParser():
    ERROR_PREFIX = 'Error: '

    OPERATOR1 = {
        '+': operator.add,
        '-': operator.sub,
        '+%': add_proc,
        '-%': sub_proc
    }

    OPERATOR2 = {
        '*': operator.mul,
        '/': operator.truediv,
        '//': operator.floordiv,
        'div': operator.floordiv,
        'mod': operator.mod,
        '*%': mul_proc
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
        'sin': sin,
        'cos': cos,
        'tan': tan,
        'asin': asin,
        'acos': acos,
        'atan': atan,

        'sinr': math.sin,
        'cosr': math.cos,
        'tanr': math.tan,
        'asinr': math.asin,
        'acosr': math.acos,
        'atanr': math.atan,


        'sqrt': math.sqrt,

        'abs': math.fabs,
        'radians': math.radians,
        'degrees': math.degrees,
        'log': math.log10,
        'log2': math.log2,
        'log10': math.log10,
        'ln': ln

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

        while self.lexer.cur in ('^', '**'):
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
            raise SyntaxEror("ожидаеся закрывающая скобка")

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
                    raise SyntaxEror('ожидается символ "(", обнаружен "{}"'.format(self.lexer.cur))
                self.lexer.next()

                arg = self.mathExpr()

                if not self.lexer.cur == ')':
                    raise SyntaxEror('ожидается символ "(", обнаружен "{}"'.format(self.lexer.cur))
                self.lexer.next()

                func = self.MATH_FUNCTION[res]
                return func(arg)
            else:
                raise SyntaxEror('неизвестный иднтификатор "{}"'.format(res))

        raise SyntaxEror('неизвестная лексема "{}"'.format(res))

    def parse(self, base):
        if self.lexer.cur is None:
            return 0
        else:
            try:
                res = self.mathExpr()

                if not self.lexer.cur == None:
                    raise SyntaxEror('неизвестный иднтификатор "{}"'.format(self.lexer.cur))

                if base == 10:
                    return res
                elif base == 2:
                    return bin(res)
                elif base == 8:
                    return oct(res)
                elif base == 16:
                    res = hex(res)
                    return res[0:2] + res[2:].upper()
                else:
                    raise SyntaxEror('Система счисления с основанием {} не поддерживается'.format(base))

            except Exception as e:
                return str(MathParser.ERROR_PREFIX + str(e))

    def solve(self, base):
        res = self.parse(base)

        if type(res) == float:
            frac = math.modf(res)
            if frac[0] == 0:
                res = int(res)

        return res

if __name__ == '__main__':
    p = MathParser('2 + 2 * + 2 dfd')
    print(p.parse())

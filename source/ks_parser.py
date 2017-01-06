
class Parser():
    def __init__(self, text):
        self.text = text
        self.index = 0

    def current(self):
        if self.eof():
            return ''
        else:
            return self.text[self.index]

    # def read(self):
    #     if self.eof():
    #         return chr(0)
    #     else:
    #         self.text[self.index]
    #         self.index += 1

    def skipSpaces(self):
        while self.current().isspace():
            self.next()

    def copy(self, startIndex):
        return self.text[startIndex:self.index]

    def next(self):
        if not self.eof():
            self.index += 1

    def skipWhile(self, func):
        while func(self.current()):
            self.next()

    def eof(self):
        return len(self.text) <= self.index
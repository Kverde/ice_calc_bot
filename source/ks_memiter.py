
class MemIter():
    def __init__(self, obj):
        self.iter = obj.__iter__()
        self.next()

    def next(self):
        try:
            self.cur = next(self.iter)
        except StopIteration as e:
            self.cur = None

    def current(self):
        return self.cur



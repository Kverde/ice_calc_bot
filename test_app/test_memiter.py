import unittest

from source.ks_memiter import MemIter

class TestMemIter(unittest.TestCase):
    def test_current(self):
        obj = [1, 2, 3]

        memIter = MemIter(obj)
        self.assertEqual(1, memIter.cur)

        memIter.next()
        self.assertEqual(2, memIter.cur)

        memIter.next()
        self.assertEqual(3, memIter.cur)

        memIter.next()
        self.assertEqual(None, memIter.cur)

        memIter.next()
        self.assertEqual(None, memIter.cur)
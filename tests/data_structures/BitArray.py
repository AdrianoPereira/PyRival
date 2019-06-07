import unittest
from snippets.data_structures.BitArray import bitarray

class TestBitarray(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.array = bitarray(2)

    def test_setitem_getitem(self):
        self.array[0] = 1

        self.assertTrue(self.array[0])
        self.assertFalse(self.array[1])

if __name__ == '__main__':
    unittest.main()

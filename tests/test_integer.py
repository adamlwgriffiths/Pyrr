try:
    import unittest2 as unittest
except ImportError:
    import unittest
import numpy as np
from pyrr import integer

class test_integer(unittest.TestCase):
    def test_count_bits(self):
        i = 0b010101
        self.assertEqual(integer.count_bits(i), 3)

if __name__ == '__main__':
    unittest.main()

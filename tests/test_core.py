import unittest

from smart_square.core import square

class TestCore(unittest.TestCase):
    """ unittest for core module"""

    def test_float(self):
        """ Test with a float"""
        self.assertAlmostEqual(square(2.), 4.)



if __name__ == '__main__':
    unittest.main()

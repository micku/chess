import unittest
import sys
import os

sys.path.append(os.path.abspath('.'))

from chess import main


class TestMain(unittest.TestCase):

    def test_error(self):
        with self.assertRaises(TypeError):
            main.calculate()


if __name__ == '__main__':
    unittest.main()

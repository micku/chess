import unittest
import sys
import os

sys.path.append(os.path.abspath('.'))

from chess import main
from test_utils import *
from test_board import *


class TestMain(unittest.TestCase):

    def test_error(self):
        # TODO: Add console app tests
        pass


if __name__ == '__main__':
    unittest.main()

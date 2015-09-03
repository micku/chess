import unittest
import sys
import os

from chess.piece import King, Queen, Rook, Bishop, Knight


class TestPiece(unittest.TestCase):

    def test_king_movement(self):
        with self.assertRaises(TypeError):
            MAIN.CALculate()


if __name__ == '__main__':
    unittest.main()

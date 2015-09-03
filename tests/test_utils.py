import unittest
import sys
import os

from chess import utils
from chess import piece


class TestUtils(unittest.TestCase):

    def test_create_piece_list(self):
        kings = 0
        queens = 1
        rooks = 3
        bishops = 2
        knights = 0
        pieces = utils.create_pieces_list(
                kings, queens, rooks, bishops, knights)

        self.assertEqual(len(pieces), sum([kings, queens, rooks, bishops]))

        types = [
                piece.Queen,
                piece.Rook,
                piece.Rook,
                piece.Rook,
                piece.Bishop,
                piece.Bishop
                ]

        for i in range(len(pieces)):
            self.assertIsInstance(pieces[i], types[i])

if __name__ == '__main__':
    unittest.main()

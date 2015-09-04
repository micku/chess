import unittest
import sys
import os

sys.path.append(os.path.abspath('.'))

from chess import main, utils
from chess.board import Board
from test_utils import *
from test_board import *
from test_piece import *


class TestMain(unittest.TestCase):

    def test_calculate_combinations(self):
        board = Board(3, 3)
        pieces = utils.create_pieces_list(
                kings=2,
                queens=0,
                rooks=1,
                bishops=0,
                knights=0)
        valid_boards = []
        valid_boards = main.calculate_combinations(valid_boards, board, pieces)
        self.assertEqual(len(valid_boards), 4)

        board = Board(4, 4)
        pieces = utils.create_pieces_list(
                kings=0,
                queens=0,
                rooks=2,
                bishops=0,
                knights=4)
        valid_boards = []
        valid_boards = main.calculate_combinations(valid_boards, board, pieces)
        self.assertEqual(len(valid_boards), 8)


if __name__ == '__main__':
    unittest.main()

import unittest
import sys
import os

from chess import board


class TestBoard(unittest.TestCase):

    def test_board_size(self):
        width = 4
        height = 5

        chessboard = board.Board(width, height)

        self.assertEqual(width, len(chessboard.chessboard))
        self.assertEqual(height, len(chessboard.chessboard[0]))


    def test_iter(self):
        width = 4
        height = 5

        chessboard = board.Board(width, height)
        squares_count = 0
        for square in chessboard:
            squares_count+=1
            self.assertIsInstance(square, board.BoardSquare)

        self.assertEqual(squares_count, width*height)

if __name__ == '__main__':
    unittest.main()

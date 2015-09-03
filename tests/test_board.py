import unittest
import sys
import os

from chess import board
from chess import piece


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


class TestBoardSquare(unittest.TestCase):

    def test_string(self):
        empty_square = board.BoardSquare((1,1))
        self.assertEqual(' ', str(empty_square))

        king_square = board.BoardSquare((1,1))
        king_square.set_piece(piece.King())
        self.assertEqual('K', str(king_square))

        threat_square = board.BoardSquare((1,1))
        threat_square.set_threat()
        self.assertEqual(' ', str(threat_square))

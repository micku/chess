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

    
    def test_equality(self):
        board1 = board.Board(4, 4)
        board2 = board.Board(4, 3)
        self.assertNotEqual(board1, board2)

        board2 = board.Board(4, 4)
        self.assertEqual(board1, board2)

        board1.get_square((0, 0)).set_threat()
        self.assertNotEqual(board1, board2)

        board2.get_square((0, 0)).set_threat()
        self.assertEqual(board1, board2)


    def test_contains(self):
        chessboard = board.Board(4, 4)
        square = board.BoardSquare((1, 2))
        square.set_threat()
        self.assertFalse(square in chessboard)

        chessboard.get_square((1, 2)).set_threat()
        self.assertTrue(square in chessboard)


    def test_add_squares(self):
        chessboard = board.Board(4, 4)

        tests = [
                [(0,0), 1, (1, 0)],
                [(0,0), 4, (0, 1)],
                [(3,0), 1, (0, 1)],
                [(0,0), 5, (1, 1)],
                [(0,0), 1, (1, 0)],
                [(0,0), 1, (1, 0)],
                ]

        for test in tests:
            square = chessboard.add_to_position(test[0], test[1])
            self.assertEqual(test[2], square)



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

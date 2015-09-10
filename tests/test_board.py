import unittest
import sys
import os

from chess import board
from chess import piece


class TestBoard(unittest.TestCase):

    def test_iter(self):
        width = 4
        height = 5

        chessboard = board.Board(width, height)
        squares_count = 0
        for square in chessboard:
            squares_count+=1
            self.assertIsInstance(square, board.BoardSquare)

        self.assertEqual(squares_count, width*height)


    def test_add_squares(self):
        chessboard = board.Board(4, 4)

        tests = [
                [(0,0), 1, (1, 0)],
                [(0,0), 4, (0, 1)],
                [(3,0), 1, (0, 1)],
                [(0,0), 5, (1, 1)],
                [(0,0), 1, (1, 0)],
                [(0,0), 1, (1, 0)],
                [(2,3), 1, (3, 3)],
                ]

        for test in tests:
            square = chessboard.add_to_position(test[0], test[1])
            self.assertEqual(test[2], square)


    def test_iter_free_squares(self):
        chessboard = board.Board(4, 4)
        square = board.BoardSquare((2, 2))
        square.set_piece(piece.Rook())
        chessboard.set_square(square)

        tests = [
                [(0,0), 15],
                [(3,0), 12],
                [(0,1), 11],
                [(1,3), 3],
                [(2,3), 2],
                [(3,3), 1],
                ]

        for test in tests:
            i = 0
            for square in chessboard.iter_free_squares(test[0]):
                i += 1
            self.assertEqual(test[1], i)


    def test_chessboard_state(self):
        chessboard = board.Board(4, 4)
        square = board.BoardSquare((2, 2))
        square.set_piece(piece.Rook())
        chessboard.set_square(square)

        state = chessboard.get_chessboard_state()
        self.assertIsInstance(state[1], dict)
        self.assertIsNotNone(state[1].get('2,2'))
        self.assertIsNone(state[1].get('3,3'))
        self.assertIsInstance(state[1].get('2,2'), board.BoardSquare)

        chessboard2 = board.Board.from_chessboard_state(state)
        self.assertEqual(chessboard2.size, (4, 4))
        self.assertIsInstance(chessboard2.get_square((2, 2)).piece, piece.Rook)
        self.assertIsNone(chessboard2.get_square((0, 0)))
        self.assertEqual(str(chessboard2.get_square((2, 2))), 'R')


class TestBoardSquare(unittest.TestCase):

    def test_string(self):
        default_position = (0, 0)
        empty_square = board.BoardSquare(default_position)
        self.assertEqual(' ', str(empty_square))

        king_square = board.BoardSquare(default_position)
        king_square.set_piece(piece.King())
        self.assertEqual('K', str(king_square))

        threat_square = board.BoardSquare(default_position)
        threat_square.set_threat()
        self.assertEqual(' ', str(threat_square))

import unittest
import sys
import os

from chess.piece import King, Queen, Rook, Bishop, Knight


class TestPiece(unittest.TestCase):

    def test_king_threats(self):
        king = King()
        board_size = (3, 3)
        
        # test top left corner
        count = 0
        for m in king.iter_threats(board_size, (0, 0)):
            count +=1
        self.assertEqual(count, 3)
        
        # test bottom right corner
        count = 0
        for m in king.iter_threats(board_size, (2, 2)):
            count +=1
        self.assertEqual(count, 3)
        
        # test center
        count = 0
        for m in king.iter_threats(board_size, (1, 1)):
            count +=1
        self.assertEqual(count, 8)
        
        # test left center
        count = 0
        for m in king.iter_threats(board_size, (0, 1)):
            count +=1
        self.assertEqual(count, 5)
        
        # test bottom center
        count = 0
        for m in king.iter_threats(board_size, (1, 2)):
            count +=1
        self.assertEqual(count, 5)


    def test_knight_threats(self):
        knight = Knight()
        board_size = (5, 5)

        combinations = (
                ((0, 0), 2),
                ((1, 1), 4),
                ((2, 2), 8),
                ((3, 3), 4),
                ((4, 4), 2),
                ((0, 2), 4),
                ((0, 1), 3),
                ((2, 1), 6),
                )

        for combination in combinations:
            position = combination[0]
            result = combination[1]
            count = 0
            for m in knight.iter_threats(board_size, position):
                count += 1
            self.assertEqual(count, result)


    def test_queen_threats(self):
        queen = Queen()
        board_size = (5, 5)

        combinations = (
                ((0, 0), 12),
                ((1, 1), 14),
                ((2, 2), 16),
                ((3, 3), 14),
                ((4, 4), 12),
                ((0, 2), 12),
                ((0, 1), 12),
                ((2, 1), 14),
                )

        for combination in combinations:
            position = combination[0]
            result = combination[1]
            count = 0
            for m in queen.iter_threats(board_size, position):
                count += 1
            self.assertEqual(count, result)


    def test_rook_threats(self):
        rook = Rook()
        board_size = (5, 5)

        combinations = (
                ((0, 0), 8),
                ((1, 1), 8),
                ((2, 2), 8),
                ((3, 3), 8),
                ((4, 4), 8),
                ((0, 2), 8),
                ((0, 1), 8),
                ((2, 1), 8),
                )

        for combination in combinations:
            position = combination[0]
            result = combination[1]
            count = 0
            for m in rook.iter_threats(board_size, position):
                count += 1
            self.assertEqual(count, result)



    def test_bishop_threats(self):
        bishop = Bishop()
        board_size = (5, 5)

        combinations = (
                ((0, 0), 4),
                ((1, 1), 6),
                ((2, 2), 8),
                ((3, 3), 6),
                ((4, 4), 4),
                ((0, 2), 4),
                ((0, 1), 4),
                ((2, 1), 6),
                )

        for combination in combinations:
            position = combination[0]
            result = combination[1]
            count = 0
            for m in bishop.iter_threats(board_size, position):
                count += 1
            self.assertEqual(count, result)



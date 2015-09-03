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


"""Module that contains all the pieces logic"""


import itertools


class Piece(object):
    """Interface for the pieces"""
    def iter_threats(self, board_size, position):
        """Iterator for all the possible positions in the board
        that can be reached by the piece

        :param board_size: Size of the chessboard
        :type board_size: (x, y)
        :param position: Position of the piece on the chessboard
        :type position: (x, y)
        """
        pass


class DirectionMovementPiece(Piece):
    """Class that defines pieces that move in directions until
    the end of the board."""

    def iter_direction_threats(self, movements, board_size, position):
        """Iterates and extends a single movement until the end of
        the board.

        :param movements: Movements to iterate
        :type movements: list<tuple>
        :param board_size: Size of the chessboard
        :type board_size: (x, y)
        :param position: Position of the piece on the chessboard
        :type position: (x, y)
        """
        for movement in movements:
            new_x = sum([movement[0], position[0]])
            new_y = sum([movement[1], position[1]])
            if new_x >= 0 and new_x < board_size[0] and \
                    new_y >= 0 and new_y < board_size[1]:
                for square in self.iter_direction_threats([movement], board_size, (new_x, new_y)):
                    yield square
                yield (new_x, new_y)


    def iter_threats(self, board_size, position):
        """Iterator for all the possible positions in the board
        that can be reached by the piece

        :param board_size: Size of the chessboard
        :type board_size: (x, y)
        :param position: Position of the piece on the chessboard
        :type position: (x, y)
        """
        return self.iter_direction_threats(self.movements, board_size, position)


class FixedMovementPiece(Piece):
    """Class that defines pieces that move by a finite number
    of combinations"""

    def iter_threats(self, board_size, position):
        """Iterator for all the possible positions in the board
        that can be reached by the piece

        :param board_size: Size of the chessboard
        :type board_size: (x, y)
        :param position: Position of the piece on the chessboard
        :type position: (x, y)
        """
        for movement in self.movements:
            new_x = sum([movement[0], position[0]])
            new_y = sum([movement[1], position[1]])
            if new_x >= 0 and new_x < board_size[0] and \
                    new_y >= 0 and new_y < board_size[1]:
                yield (new_x, new_y)


class King(FixedMovementPiece):
    """King piece class"""

    movements = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    """Possible movement of a King"""


    def __str__(self):
        return 'K'


class Queen(DirectionMovementPiece):
    """Queen piece class"""

    movements = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    """Movement directions for a Queen"""


    def __str__(self):
        return 'Q'


class Rook(DirectionMovementPiece):
    """Rook piece class"""

    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    """Movement directions for a Rook"""


    def __str__(self):
        return 'R'


class Bishop(DirectionMovementPiece):
    """Bishop piece class"""

    movements = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    """Movement directions for a Bishop"""


    def __str__(self):
        return 'B'


class Knight(FixedMovementPiece):
    """Knight piece class"""

    movements = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)] 
    """Possible movement of a Knight"""


    def __str__(self):
        return 'N'

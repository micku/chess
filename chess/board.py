"""Module that contains all board classes"""

import os
import copy


class Board(object):
    """Class that defines the chessboard."""

    def __init__(self, width, height):
        """Creates an empty board of the given size.

        :param width: Width of the board
        :param height: Height of the board
        """
        self.width = width
        self.height = height
        self.size = (width, height)
        self.chessboard = {}


    def get_chessboard_state(self):
        """Returns the actual state and info of the board."""
        return (self.size, copy.copy(self.chessboard))


    @staticmethod
    def from_chessboard_state(state):
        """Creates a new instance of Board given a state.

        :param state: tuple created by get_chessboard_state
        :type state: tuple
        """
        size = state[0]
        chessboard = state[1]
        new_board = Board(size[0], size[1])
        new_board.chessboard = chessboard
        return new_board


    def __iter__(self):
        """Iterates all the squares in the board."""
        return self.iter_squares()


    def add_to_position(self, position, squares):
        """Returns the position plus a number of squares.

        :param position: Tuple containing the position from
        which start the loop
        :param squares: Number of squares to add
        """
        i = 0
        for square in self.iter_squares(position):
            if i == squares:
                return square.position
            i += 1
        return None


    def iter_squares(self, starting_position=None):
        """Iterates all the squares in the board.

        :param starting_position: Tuple containing the position from
        which start the loop
        """
        if starting_position is None:
            starting_position = (0, 0)
        for row in xrange(starting_position[1], self.height):
            for col in xrange(starting_position[0] \
                if row == starting_position[1] \
                else 0, self.width \
                ):
                yield self.chessboard.get('{},{}'.format(col, row)) \
                    or BoardSquare((col, row))


    def iter_free_squares(self, starting_position=None):
        """Iterates all the free squares in the board.

        :param starting_position: Tuple containing the position from
        which the loop starts
        """
        for square in self.iter_squares(starting_position):
            if square.is_empty():
                yield square


    def set_square(self, square):
        """Sets a single square given its position.

        :param position: Tuple containing row and column
        """
        self.chessboard['{},{}'.format(square.position[0], square.position[1])] = square


    def get_square(self, position):
        """Gets a single square given its position.

        :param position: Tuple containing row and column
        """
        #return self.chessboard[position[1]][position[0]]
        return self.chessboard.get('{},{}'.format(position[0], position[1])) \
                or BoardSquare((position[0], position[1]))


    def _table_horiz_separator(self):
        """Helper method that returns an horizontal separator."""
        return '{}-{}'.format(
            '-' * 4 * self.width,
            os.linesep
        )


    def _table_empty_line(self):
        """Helper method that returns an empty line
        with vertical separators."""
        return '{}|{}'.format(
            '|   ' * self.width,
            os.linesep
        )


    def __str__(self):
        """Returns the graphical representation of the chessboard."""
        ret = ''
        for row in self.chessboard:
            ret += self._table_horiz_separator() + \
                    self._table_empty_line()

            for col in row:
                ret += '| {} '.format(str(col))
            ret += '|{}'.format(os.linesep)

            ret += self._table_empty_line()

        ret += self._table_horiz_separator()
        return ret


class BoardSquare(object):
    """Class that contains a single square info."""
    is_threat = False
    piece = None

    def __init__(self, position):
        """Creates a new instance of BoardSquare
        assigning its position
        """
        self.row = position[1]
        self.col = position[0]
        self.position = position


    def set_piece(self, piece):
        """Sets the piece of this square.

        :param piece: Piece to assigne to this square
        :type piece: chess.piece.Piece
        """
        self.piece = piece


    def set_threat(self):
        """Sets the square as threated"""
        self.is_threat = True


    def is_empty(self):
        """Returns whether the square is empty and
        not under threat"""
        return not self.is_occupied()


    def is_empty_or_threat(self):
        """Returns whether the square is empty or
        under threat"""
        return self.is_threat or self.piece is None


    def is_occupied(self):
        """Returns whether the square is occupied or threat"""
        return self.is_threat or (self.piece is not None)


    def __str__(self):
        """Returns the representation of the square"""
        return ' ' \
                if (self.is_threat or not self.is_occupied()) \
                else str(self.piece)

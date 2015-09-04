import os


class Board:
    """Class that defines the chessboard."""

    def __init__(self, width, height):
        """Creates an empty board of the given size.

        :param width: Width of the board
        :param height: Height of the board
        """
        self.width = width
        self.height = height
        self.size = (width, height)
        self.chessboard = []
        for x in range(self.width):
            columns = []
            for y in range(self.height):
                columns.append(BoardSquare((x, y)))
            self.chessboard.append(columns)
        #self.chessboard = [['']*width]*height


    def __iter__(self):
        """Iterates all the squares in the board."""
        for row in self.chessboard:
            for col in row:
                yield col


    def get_square(self, position):
        return self.chessboard[position[0]][position[1]]


    def __eq__(self, other):
        if self.width != other.width or \
            self.height != other.height:
            return False
        for other_square in other:
            if other_square not in self:
                return False
        return True


    def __contains__(self, key):
        for square in self:
            if square.position[0] == key.position[0] and \
                square.position[1] == key.position[1] and \
                square.is_threat == key.is_threat and \
                str(square) == str(key):
                return True
        return False


    def __str__(self):
        ret = ''
        for row in self.chessboard:
            ret += '-'*4*self.width
            ret += '-'
            ret += os.linesep

            ret += '|   '*self.width
            ret += '|{}'.format(os.linesep)
            for col in row:
                ret += '| {} '.format(str(col))
            ret += '|{}'.format(os.linesep)

            ret += '|   '*self.width
            ret += '|{}'.format(os.linesep)

        ret += '-'*4*self.width
        ret += '-'
        return ret


class BoardSquare:
    """Class that contains a single square info."""
    is_threat = False
    piece = None

    def __init__(self, position):
        """Creates a new instance of BoardSquare
        assigning its position
        """
        self.x = position[0]
        self.y = position[1]
        self.position = position


    def set_piece(self, piece):
        """Sets the piece of this square.

        :param piece: Piece to assigne to this square
        :type piece: chess.piece.Piece
        """
        # TODO: Raise exception if is_threat
        self.piece = piece


    def set_threat(self):
        """Sets the square as threated"""
        # TODO: Raise exception if occupied
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
        return ' ' if (self.is_threat or not self.is_occupied()) else str(self.piece)

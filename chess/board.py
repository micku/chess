class Board:
    """Class that defines the chessboard."""

    def __init__(self, width, height):
        """Creates an empty board of the given size.

        :param width: Width of the board
        :param height: Height of the board
        """
        self.width = width
        self.height = height
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


    def is_occupied(self):
        """Returns whether the square is occupied or threat"""
        return self.is_threat or (self.piece is not None)

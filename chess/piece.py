import itertools


class Piece():
    """Interface for the pieces"""
    def iter_threats(self, board_size, position):
        """Iterates the possible threats in a given board size
        places in a given position"""
        pass


class FixedMovementPiece(Piece):
    def iter_fixed_threats(self, movements, board_size, position):
        for movement in movements:
            new_x = sum([movement[0], position[0]])
            new_y = sum([movement[1], position[1]])
            if new_x >= 0 and new_x < board_size[0] and \
                    new_y >= 0 and new_y < board_size[1]:
                yield (new_x, new_y)


class King(FixedMovementPiece):
    def iter_threats(self, board_size, position):
        movements = [(x,y)
                for (x,y)
                in itertools.product(range(-1,2), repeat=2)
                if not(x==0 and y==x)]
        return self.iter_fixed_threats(movements, board_size, position)


    def __str__(self):
        return 'K'


class Queen(Piece):
    def iter_threats(self, board_size, position):
        pass


    def __str__(self):
        return 'Q'


class Rook(Piece):
    def iter_threats(self, board_size, position):
        pass


    def __str__(self):
        return 'R'


class Bishop(Piece):
    def iter_threats(self, board_size, position):
        pass


    def __str__(self):
        return 'B'


class Knight(FixedMovementPiece):
    def iter_threats(self, board_size, position):
        movements = [(x, y)
                for (x, y)
                in itertools.permutations([-1, 1, -2, 2], 2)
                if x != y * -1]
        return self.iter_fixed_threats(movements, board_size, position)


    def __str__(self):
        return 'N'

"""Module containing helper classes."""

from piece import Queen, Rook, Bishop, King, Knight


def create_pieces_list(kings, queens, rooks, bishops, knights):
    """Creates the list of pieces to loop.

    :param kings: Number of kings pieces
    :type kings: int
    :param queens: Number of queens pieces
    :type queens: int
    :param rooks: Number of rooks pieces
    :type rooks: int
    :param bishops: Number of bishops pieces
    :type bishops: int
    :param knights: Number of knights pieces
    :type knights: int
    """
    pieces = []

    for _ in xrange(queens):
        pieces.append(Queen())

    for _ in xrange(rooks):
        pieces.append(Rook())

    for _ in xrange(bishops):
        pieces.append(Bishop())

    for _ in xrange(kings):
        pieces.append(King())

    for _ in xrange(knights):
        pieces.append(Knight())

    return pieces

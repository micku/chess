from piece import *


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

    for queen in range(queens):
        pieces.append(Queen())

    for rook in range(rooks):
        pieces.append(Rook())

    for bishop in range(bishops):
        pieces.append(Bishop())

    for king in range(kings):
        pieces.append(King())

    for knight in range(knights):
        pieces.append(Knight())

    return pieces

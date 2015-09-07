from piece import *


def create_pieces_list(kings, queens, rooks, bishops, knights):
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

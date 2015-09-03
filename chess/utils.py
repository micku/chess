from chess import piece


def create_pieces_list(kings, queens, rooks, bishops, knights):
    pieces = []

    for king in range(kings):
        pieces.append(piece.King())

    for queen in range(queens):
        pieces.append(piece.Queen())

    for rook in range(rooks):
        pieces.append(piece.Rook())

    for bishop in range(bishops):
        pieces.append(piece.Bishop())

    for knight in range(knights):
        pieces.append(piece.Knight())

    return pieces

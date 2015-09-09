#!/usr/bin/env python
"""Module containing main iter logic and CLI"""

import click
import time

from board import Board, BoardSquare
from utils import create_pieces_list


@click.command()
@click.option(
    '--width', prompt='Width of the board', type=int,
    help='Width of the board'
)
@click.option(
    '--height', prompt='Height of the board', type=int,
    help='Height of the board'
)
@click.option(
    '--kings', default=0, prompt='Kings', type=int,
    help='Number of kings to place on the board'
)
@click.option(
    '--queens', default=0, prompt='Queens', type=int,
    help='Number of queens to place on the board'
)
@click.option(
    '--rooks', default=0, prompt='Rooks', type=int,
    help='Number of rooks to place on the board'
)
@click.option(
    '--bishops', default=0, prompt='Bishops', type=int,
    help='Number of bishops to place on the board'
)
@click.option(
    '--knights', default=0, prompt='Knights', type=int,
    help='Number of knights to place on the board'
)
@click.option(
    '--graphic', default=False, prompt='Print chessboards', type=bool,
    help='Print the chessboard configurations'
)
def main(width=None, height=None, kings=None, queens=None, rooks=None, bishops=None, knights=None, graphic=None):
    """Calculate the number of different combinations of the board
    given size and number of pieces."""
    click.echo('Board size: {}x{}'.format(width, height))

    start_time = time.time()

    board = Board(width, height)
    pieces = create_pieces_list(
        kings=kings,
        queens=queens,
        rooks=rooks,
        bishops=bishops,
        knights=knights
    )
    total_boards = 0
    for _ in calculate_combinations(board, pieces):
        total_boards += 1


    execution_time = time.time() - start_time

    """
    if graphic:
        for valid_board in valid_boards:
            click.echo(valid_board)
    """
    click.echo('Found {} possible chessboards'.format(total_boards))
    click.echo('Execution time: {}'.format(execution_time))


def calculate_combinations(board, pieces, previous_position=None):
    """Calculates the combinations with given parameters.

    :param board: Current board to work on
    :type board: Board
    :param pieces: List of pieces left to place
    :type pieces: list<Piece>
    :param previous_position: First possible position for this piece
    :type previous_position: tuple
    """
    for square in board.iter_free_squares(previous_position):
        if not square.is_occupied():
            is_valid = True
            threats = []
            piece = pieces[0]
            for threat in piece.iter_threats(board.size, square.position):
                threat_square = board.get_square(threat)
                if threat_square.is_empty_or_threat():
                    threats.append(threat_square.position)
                else:
                    is_valid = False
                    break
            if is_valid:
                state = board.get_chessboard_state()
                position = square.position
                for chessboard in put_piece(
                    board.clone(),
                    position,
                    pieces,
                    threats
                    ):
                    yield board


def put_piece(board, square_position, pieces, threats):
    """Tries to put a piece on the given square position.

    :param board: Current board to work on
    :type board: Board
    :param square_position: Position to place the piece
    :type square_position: tuple
    :param pieces: List of pieces left to place
    :type pieces: list<Piece>
    :param threats: Threats to be added to the cloned board
    :type threats: list<tuple>
    """
    square = board.get_square(square_position)
    piece = pieces[0]
    for threat in threats:
        board_threat = BoardSquare(threat)
        board_threat.set_threat()
        board.set_square(board_threat)

    square.set_piece(piece)
    board.set_square(square)

    if len(pieces[1:]) <= 0:
        yield board
    else:
        next_square = board.add_to_position(square_position, 1)
        starting_position = next_square \
                if str(pieces[1]) == str(piece) \
                else (0, 0)
        if starting_position is not None:
            for chessboard in calculate_combinations(
                board, pieces[1:],
                starting_position
                ):
                yield chessboard


if __name__ == '__main__':
    main()

#!/usr/bin/env python
import click
import copy
import time

from board import Board
from piece import King, Queen, Rook, Bishop, Knight
from utils import create_pieces_list


@click.command()
@click.option('--width', prompt='Width of the board', type=int,
        help='Width of the board')
@click.option('--height', prompt='Height of the board', type=int,
        help='Height of the board')
@click.option('--kings', default=0, prompt='Kings', type=int,
        help='Number of kings to place on the board')
@click.option('--queens', default=0, prompt='Queens', type=int,
        help='Number of queens to place on the board')
@click.option('--rooks', default=0, prompt='Rooks', type=int,
        help='Number of rooks to place on the board')
@click.option('--bishops', default=0, prompt='Bishops', type=int,
        help='Number of bishops to place on the board')
@click.option('--knights', default=0, prompt='Knights', type=int,
        help='Number of knights to place on the board')
def main(width, height, kings, queens, rooks, bishops, knights):
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
            knights=knights)
    valid_boards = []
    valid_boards = calculate_combinations(valid_boards, board, pieces)

    execution_time = time.time() - start_time

    for valid_board in valid_boards:
        click.echo(valid_board)
    click.echo('Found {} possible chessboards'.format(len(valid_boards)))
    click.echo('Execution time: {}'.format(execution_time))


def calculate_combinations(valid_boards, board, pieces):
    for square in board:
        valid_boards = put_piece(valid_boards, copy.deepcopy(board), square.position, pieces[:])
    return valid_boards


def put_piece(valid_boards, board, square_position, pieces):
    square = board.get_square(square_position)
    if square.is_occupied():
        return valid_boards
    piece = pieces[0]
    square.set_piece(piece)
    for threat in piece.iter_threats(board.size, square.position):
        threat_square = board.get_square(threat)
        if threat_square.is_empty_or_threat():
            threat_square.set_threat()
        else:
            return valid_boards
    if len(pieces[1:])<=0:
        # TODO: Find a better way to manage double pieces
        if board not in valid_boards:
            valid_boards.append(board)
    else:
        valid_boards = calculate_combinations(valid_boards, copy.deepcopy(board), pieces[1:])
    return valid_boards


if __name__ == '__main__':
    main()

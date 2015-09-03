#!/usr/bin/env python
import click

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

    board = Board(width, height)
    pieces = create_pieces_list(
            kings=kings,
            queens=queens,
            rooks=rooks,
            bishops=bishops,
            knights=knights)
    #board.add_piece(King(), x, y)


if __name__ == '__main__':
    main()

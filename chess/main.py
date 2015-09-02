#!/usr/bin/env python
import click


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
    given size and number of pieces"""
    click.echo('Board size: {}x{}'.format(width, height))

    calculate((width, height), None)


def calculate(size, pieces):
    pass


if __name__ == '__main__':
    main()

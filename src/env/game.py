from __future__ import print_function
import numpy as np

from src.const import (
    WIDTH,
    HEIGHT,
    WIN,
)


class Board(object):
    """
    board for the game
    """

    def __init__(self, **kwargs):
        self.width = int(kwargs.get('width', WIDTH))
        self.height = int(kwargs.get('height', HEIGHT))
        # board states stored as a dict,
        # key: move as location on the board,
        # value: player as pieces type
        self.states = {}
        # need how many pieces in a row to win
        self.n_in_row = int(kwargs.get('n_in_row', WIN))
        self.players = [1, 2]  # player1 and player2

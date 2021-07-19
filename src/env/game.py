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

    def init_board(self, start_player=0):
        if self.width < self.n_in_row or self.height < self.n_in_row:
            raise Exception(f'board width and height can not be less than {self.n_in_row}')
        self.current_player = self.players[start_player]
        # keep available moves in a list
        self.availables = list(range(self.width * self.height))
        self.states = {}
        self.last_move = -1

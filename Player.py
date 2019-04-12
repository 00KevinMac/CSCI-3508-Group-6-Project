"""
Kevin Macfarlane
CSCI 3508
11 Apr 2019
Player Class - takes in a board object and returns a random valid move
"""
import sys
import random
import Board
# import numpy as np


def random_move(board, playerNum):
    moves = []

    # sys.stderr.write("Board: " + np.matrix(board) + '\n')  # unsure if this will work

    moves = board.get_OkayDokayColumns()
    sys.stderr.write("Valid moves: " + moves + '\n')  # displays the valid moves

    column = random.choice(moves)
    sys.stderr.write("Random move: " + str(column) + '\n')  # displays the random column choice

    return column

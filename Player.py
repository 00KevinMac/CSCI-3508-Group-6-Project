import sys
import random
import Board


def random_move(board, playerNum):
    moves = []

    sys.stderr.write("Board: " + board + '\n')  # unsure if this will work

    moves = board.get_OkayDokayColumns()
    sys.stderr.write("Valid moves: " + moves + '\n')  # displays the valid moves

    column = random.choice(moves)
    sys.stderr.write("Random move: " + str(column) + '\n')  # displays the random column choice

    return column

import random
import Board as brd


def random_move(board):
    moves = []
    moves = board.get_OkayDokayColumns()
    return random.choice(moves)

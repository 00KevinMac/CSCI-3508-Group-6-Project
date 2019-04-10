import random
import Board


def random_move(board):
    moves = []
    moves = board.get_OkayDokayColumns()
    return random.choice(moves)

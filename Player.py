import random
import Board


def random_move(board, playerNum):
    moves = []
    moves = board.get_OkayDokayColumns()
    return random.choice(moves)

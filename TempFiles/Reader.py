import sys
import json


def read_json():
    for line in sys.stdin:
        board = []
        grid = json.loads(line)
        board = grid['grid']
        return board

import json
import sys
import Board

#def init_stream_read():
    #readin = input()
    #parse = json.load(readin)
    # call constructor for board object
    # board = Board(parse["player"], parse["width"], parse["height"])
    # return board object
    # return board

def stream_read(width, height):
    readin = input()
    parse = json.loads(readin)
    board_array = parse['grid']
    board = Board(board_array)
    return board
import json
import sys

#def init_stream_read():
    #readin = input()
    #parse = json.load(readin)
    # call constructor for board object
    # board = Board(parse["player"], parse["width"], parse["height"])
    # return board object
    # return board

def stream_read(width, height):
    readin = input()
    board = Board(height, width)
    parse = json.loads(readin)
    board.board_Array = parse['grid']

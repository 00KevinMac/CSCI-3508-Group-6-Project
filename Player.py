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

    # sys.stderr.write("Board: " + board + '\n')  # unsure if this will work

    moves = board.get_OkayDokeyColumns()
    sys.stderr.write("Valid moves: " + str(moves) + '\n')  # displays the valid moves

    column = random.choice(moves)
    # sys.stderr.write("Random move: " + str(column) + '\n')  # displays the random column choice

    return column


def same_column_move(board, playerNum):
    moves = []
    moves = board.get_OkayDokeyColumns()

    column = moves[0]

    return column

def brute_force_move(board, playerNum):

    friendly_runs = {}

    hostile_runs = []

    useable_cols = board.get_OkayDokeyColumns()

    #get vert runs
    for i in range(board.get_length(), 0, -1):
        for j in range(0, board.get_width()):
            if board.get_Content(i, j) == playerNum:
                friendly_runs["run"+str(j)] = 1
                temp = i 
                while temp + 1 < board.get_length():
                    if board.get_Content(temp+1, j) == playerNum:
                        friendly_runs["run"+str(j)] += 1
                    else:
                        break
                    temp += 1
            elif board.get_Content(i, j) != playerNum and board.get_Content(i, j) != 0:
                hostile_runs["run"+str(j)] = 1
                temp = i 
                while temp + 1 < board.get_length():
                    if board.get_Content(i, j) != playerNum and board.get_Content(i, j) != 0:
                        hostile_runs["run"+str(j)] += 1
                    else:
                        break
                    temp += 1

    #get horiz runs        
    for i in range(0, board.get_width()):
        for j in range(board.get_length(), 0, -1):
            if board.get_Content(i, j) == playerNum:
                friendly_runs["run"+str(j)] = 1
                temp = i 
                while temp + 1 < board.get_length():
                    if board.get_Content(temp+1, j) == playerNum:
                        friendly_runs["run"+str(j)] += 1
                    else:
                        break
                    temp += 1
            elif board.get_Content(i, j) != playerNum and board.get_Content(i, j) != 0:
                hostile_runs["run"+str(j)] = 1
                temp = i 
                while temp + 1 < board.get_length():
                    if board.get_Content(i, j) != playerNum and board.get_Content(i, j) != 0:
                        hostile_runs["run"+str(j)] += 1
                    else:
                        break
                    temp += 1
    
                        
    





























    

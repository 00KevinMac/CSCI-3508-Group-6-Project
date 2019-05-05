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


def smartMove(board, playerNum):
    # tempBoard = setupValidMoves(board, playerNum)
    enemyNum = 0
    selectedMove = 0
    isPlayer = True

    if playerNum == 1:
        enemyNum = 2
    elif playerNum == 2:
        enemyNum = 1

    for depth in range(1):
        for column in range(board.width):
            addWeight(board, column, isPlayer, playerNum, enemyNum)

        selectedMove = selectWeight(board, isPlayer)
        isPlayer = not isPlayer

    return selectedMove
    # return int(selectHighestWeight(board))


# makes all our locations on the board cells to 'X', all enemy locations to 'Y'
def setupValidMoves(board, playerNum):
    tempBoard = board

    for row in range(tempBoard.length):
        for column in range(tempBoard.width):
            if tempBoard.get_Content(row, column) == playerNum:  # set our positions to X
                tempBoard.set_Content(row, column, 'X')
            elif tempBoard.get_Content(row, column) != playerNum and tempBoard.get_Content(row, column) == 1 or tempBoard.get_Content(row, column) == 2:  # enemy to Y
                tempBoard.set_Content(row, column, 'Y')

    return tempBoard


# checks the valid moves and returns the best score of the moves
def addWeight(board, column, isPlayer, playerNum, enemyNum):
    weight = 0
    selectedRow = board.length-1

    # *******************VERTICAL CHECKS******************
    # checks if there is a valid move on top of another piece (DOUBLE = 10 points)
    for row in range(board.length - 1):
        if board.get_Content(row, column) == 0 and board.get_Content(row+1, column) == playerNum:  # above player
            if isPlayer:
                weight = weight + 10
                selectedRow = row

        if board.get_Content(row, column) == 0 and board.get_Content(row + 1, column) == enemyNum:  # above enemy
            if not isPlayer:
                weight -= 10
                selectedRow = row

    # checks if there is a valid move on top of two other pieces (TRIPLE = 20 points)
    for row in range(board.length - 2):
        if board.get_Content(row, column) == 0 and board.get_Content(row + 1, column) == playerNum and board.get_Content(row + 2, column) == playerNum:  # above two players
            if isPlayer:
                weight += 50
                selectedRow = row

        if board.get_Content(row, column) == 0 and board.get_Content(row + 1, column) == enemyNum and board.get_Content(row + 2, column) == enemyNum:  # above two enemies
            if not isPlayer:
                weight -= 50
                selectedRow = row

    # checks if there is a valid move on top of three other pieces (FOUR = 1000 points)
    for row in range(board.length - 3):
        if board.get_Content(row, column) == 0 and board.get_Content(row + 1, column) == playerNum and board.get_Content(row + 2, column) == playerNum and board.get_Content(row + 3, column) == playerNum:  # above two players
            if isPlayer:
                weight += 1000
                selectedRow = row

        if board.get_Content(row, column) == 0 and board.get_Content(row + 1, column) == enemyNum and board.get_Content(row + 2, column) == enemyNum and board.get_Content(row + 3, column) == enemyNum:  # above two enemies
            if not isPlayer:
                weight -= 1000
                selectedRow = row
    # *******************VERTICAL CHECKS******************

    # *******************HORIZONTAL CHECKS*******************
    for row in reversed(range(board.length)):  # start from the bottom
        if board.get_Content(row, column) == 0:  # check if the spot is empty

            # for checking 3 in a row
            if 1 < column < board.width - 2:  # not the two edge columns
                if (board.get_Content(row, column - 1) == playerNum and board.get_Content(row, column - 2) == playerNum) or (board.get_Content(row, column + 1) == playerNum and board.get_Content(row, column + 2) == playerNum):  # player pieces next to it
                    if row == board.length - 1:  # it is the bottom row
                        if isPlayer:
                            weight += 50
                            selectedRow = row
                            break
                    '''else:  # it is not the bottom row
                        if board.get_Content(row + 1, column - 1) == 1 or board.get_Content(row + 1, column - 1) == 2 or board.get_Content(row + 1, column + 1) == 1 or board.get_Content(row + 1, column + 1) == 2:  # checks that there are pieces below the ones where we would add a new piece
                            if isPlayer:
                                weight += 10
                                selectedRow = row
                                break'''
            elif column == 1 or column == 0:
                if board.get_Content(row, column + 1) == playerNum and board.get_Content(row,
                                                                                         column + 2) == playerNum:  # player pieces next to it
                    if row == board.length - 1:  # it is the bottom row
                        if isPlayer:
                            weight += 50
                            selectedRow = row
                            break
                    # else:  # it is not the bottom row

            elif column == board.width - 1 or column == board.width - 2:
                if board.get_Content(row, column - 1) == playerNum and board.get_Content(row, column - 2) == playerNum:  # player pieces next to it
                    if row == board.length - 1:  # it is the bottom row
                        if isPlayer:
                            weight += 50
                            selectedRow = row
                            break

            # for checking 2 in a row
            if 0 < column < board.width-1:  # not the edge columns
                if board.get_Content(row, column-1) == playerNum or board.get_Content(row, column+1) == playerNum:  # player pieces next to it
                    if row == board.length - 1:  # it is the bottom row
                        if isPlayer:
                            weight += 10
                            selectedRow = row
                            break
                    else:  # it is not the bottom row
                        if ((board.get_Content(row + 1, column-1) == 1 or board.get_Content(row + 1, column-1) == 2) and board.get_Content(row, column-1) == playerNum) or ((board.get_Content(row + 1, column+1) == 1 or board.get_Content(row + 1, column+1) == 2) and board.get_Content(row, column+1) == playerNum):  # checks that there are pieces below the ones where we would add a new piece
                            if isPlayer:
                                weight += 10
                                selectedRow = row
                                break

                if board.get_Content(row, column-1) == enemyNum or board.get_Content(row, column+1) == enemyNum:  # enemy pieces next to it
                    if row == board.length - 1:  # it is the bottom row
                        if not isPlayer:
                            weight -= 10
                            selectedRow = row
                            break
                    else:  # it is not the bottom row
                        if ((board.get_Content(row + 1, column-1) == 1 or board.get_Content(row + 1, column-1) == 2) and board.get_Content(row, column-1) == playerNum) or ((board.get_Content(row + 1, column+1) == 1 or board.get_Content(row + 1, column+1) == 2) and board.get_Content(row, column+1) == playerNum):  # checks that there are pieces below the ones where we would add a new piece
                            if not isPlayer:
                                weight -= 10
                                selectedRow = row
                                break

            elif column == 0:  # left most edge
                if board.get_Content(row, column+1) == playerNum:  # player pieces next to it
                    if row == board.length - 1:  # it is the bottom row
                        if isPlayer:
                            weight += 10
                            selectedRow = row
                            break
                    else:  # it is not the bottom row
                        if board.get_Content(row + 1, column+1) == 1 or board.get_Content(row + 1, column+1) == 2:  # checks that there are pieces below the ones where we would add a new piece
                            if isPlayer:
                                weight += 10
                                selectedRow = row
                                break

                if board.get_Content(row, column+1) == enemyNum:  # enemy pieces next to it
                    if row == board.length - 1:  # it is the bottom row
                        if not isPlayer:
                            weight -= 10
                            selectedRow = row
                            break
                    else:
                        if board.get_Content(row + 1, column+1) == 1 or board.get_Content(row + 1, column+1) == 2:  # checks that there are pieces below the ones where we would add a new piece
                            if not isPlayer:
                                weight -= 10
                                selectedRow = row
                                break

            elif column == board.width-1:  # right most edge
                if board.get_Content(row, column-1) == playerNum:  # player pieces next to it
                    if row == board.length - 1:  # it is the bottom row
                        if isPlayer:
                            weight += 10
                            selectedRow = row
                            break
                    else:  # it is not the bottom row
                        if board.get_Content(row + 1, column-1) == 1 or board.get_Content(row + 1, column-1) == 2:  # checks that there are pieces below the ones where we would add a new piece
                            if isPlayer:
                                weight += 10
                                selectedRow = row
                                break

                if board.get_Content(row, column - 1) == enemyNum:  # enemy pieces next to it
                    if row == board.length - 1:  # it is the bottom row
                        if not isPlayer:
                            weight -= 10
                            selectedRow = row
                            break
                    else:
                        if board.get_Content(row + 1, column - 1) == 1 or board.get_Content(row + 1, column - 1) == 2:  # checks that there are pieces below the ones where we would add a new piece
                            if not isPlayer:
                                weight -= 10
                                selectedRow = row
                                break

            break  # break the loop if we find a 0, but no tokens next to it
    # *******************HORIZONTAL CHECKS*******************

    # *******************DIAGONAL CHECKS*******************
    # *******************DIAGONAL CHECKS*******************

    # ******************MIDDLE CHECK******************
    # checks if the column is in the middle (MIDDLE = 5 points)
    if column == int((board.width - 1) / 2):
        for row in reversed(range(board.length)):
            if board.get_Content(row, column) != 1 and board.get_Content(row, column) != 2:
                if isPlayer:
                    weight += 5
                else:
                    weight -= 5
                selectedRow = row
                break
    # ******************MIDDLE CHECK******************

    actualWeight = weight
    weight = 0
    if board.get_Content(selectedRow, column) != 1 or board.get_Content(selectedRow, column) != 2:
        board.set_Content(selectedRow, column, actualWeight)


# This will add player/enemy choices to the board which will help when determining the weights
def selectWeight(board, isPlayer):
    maxWeight = 0
    minWeight = 1000000
    selectedColumn = -1
    selectedRow = -1

    for row in range(board.length):
        for column in range(board.width):
            if isPlayer:  # if it is the player, we want maxWeight
                if int(board.get_Content(row, column)) >= maxWeight:
                    maxWeight = int(board.get_Content(row, column))
                    selectedColumn = column
                    selectedRow = row
            else:  # if it is not the player, we want minWeight
                if int(board.get_Content(row, column)) <= minWeight:
                    minWeight = int(board.get_Content(row, column))
                    selectedColumn = column
                    selectedRow = row

    if isPlayer:
        board.set_Content(selectedRow, selectedColumn, maxWeight)
    else:
        board.set_Content(selectedRow, selectedColumn, minWeight)

    return selectedColumn


# selects the highest weight for the player
def selectHighestWeight(board):
    maxWeight = 0
    selectedColumn = -1

    for row in range(board.length):
        for column in range(board.width):
            if int(board.get_Content(row, column)) >= maxWeight:
                maxWeight = int(board.get_Content(row, column))
                selectedColumn = column

    return int(selectedColumn)



def valid_move(grid, width):
    moves = []
    for i in range(width):  # goes through each column and adds to moves if the last available slot is free
        if grid[i][0] == 0:
            moves.append(i)
    return moves

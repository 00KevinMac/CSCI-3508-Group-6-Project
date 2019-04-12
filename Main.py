"""
Kevin Macfarlane, Benjamin Stanton
CSCI 3508, Prof. Doug Williams
4/3/19
"""

import sys
import StreamReader as rdr
import Board as brd
import Player as plr
import StreamSender as snd

sys.stderr.write("Connect Four\n")

# assumes driver sends correct arguments
player_num = int(sys.argv[2])  # this gives the player number
width = int(sys.argv[4])  # this gives us the width
height = int(sys.argv[6])  # this gives us the height
turn_num = 0
bad_move = True
max_iters = 3

# do we need these? I think Doug said something about using stderr
sys.stderr.write("Player: " + str(player_num) + '\n')
sys.stderr.write("Width: " + str(width) + '\n')
sys.stderr.write("Height: " + str(height) + '\n')

while True:
    sys.stderr.write("Turn: " + str(turn_num) + '\n')
    sys.stderr.write("Recieving board from driver\n")

    # read in the json to the board
    board = rdr.stream_read(width, height)

    #update log 
    if board.isEmpty():
        if player_num != 1:
            sys.stderr.write("Recieve failed\n")
        elif player_num == 1 and turn_num == 0:
            sys.stderr.write("Recieve succeeded\n")
    else:
        sys.stderr.write("Recieve succeeded\n")        
        
    sys.stderr.write("Determining move\n")

    while bad_move:
        # get random valid move
        move = plr.random_move(board, player_num)

        if move >= width:
            sys.stderr.write("Invalid move determined, retrying...\n")
            max_iters -= 1
        elif board.isFull(move):
            sys.stderr.write("Invalid move determined, retrying...\n")
            max_iters -= 1
        else:
            sys.stderr.write(str(move) + " chosen. This is a valid move.\n")
            bad_move = False
        if max_iters == 0:
            move = plr.random_move(board, player_num)
            sys.stderr.write(str(move) + " chosen. This is a valid move.\n")
            bad_move = False

    sys.stderr.write("Sending move to driver\n")   
    #try to send move 3 times
    for i in range(0,3):
        # send move to driver
        success = snd.send_move(move)

        if success:
            sys.stderr.write("Send succeeded\n")
            break
        else:
            sys.stderr.write("Send failed, retrying...\n")

    if not success:
        sys.stderr.write("Send failed\n")
            



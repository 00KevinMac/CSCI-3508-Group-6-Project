"""
Kevin Macfarlane, Benjamin Stanton
CSCI 3508, Prof. Doug Williams
4/3/19
"""

import sys
import Reader as rdr
import Board as brd
import Player as plr
import Sender as snd

sys.stderr.write("Connect Four\n")

# assumes driver sends correct arguments
player_num = int(sys.argv[2])  # this gives the player number
width = int(sys.argv[4])  # this gives us the width
height = int(sys.argv[6])  # this gives us the height

# do we need these? I think Doug said something about using stderr
sys.stderr.write("Player: " + str(player) + '\n')
sys.stderr.write("Width: " + str(width) + '\n')
sys.stderr.write("Height: " + str(height) + '\n')

board = rdr.read_json(width, height)  # read in the json to the board

# get random valid move
move = plr.random_move(board, player_num)

# send move to driver
snd.send_move(move)

# close ports
sys.stdin.close()
sys.stdout.close()
sys.stderr.close()

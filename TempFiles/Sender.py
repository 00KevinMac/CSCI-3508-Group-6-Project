import sys
import json


def send_move(move):
    msg = json.dumps(move)
    sys.stderr.write(msg + '\n')
    sys.stdout.write(msg + '\n')
    sys.stdout.flush()
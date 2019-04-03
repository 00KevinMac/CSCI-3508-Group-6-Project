# Jahoon Koo
# The stream sender will put the move into stdout,
# then return a bool representing the success or failure of the stream.
import sys

def Stream_Sender(move):
    try:
        sys.stdout.write(move)
        sys.stdout.flush()
        return true
    except:
        e = sys.exc_info()[0]
        print("Error: ", e)
        return false

    
    

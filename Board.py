"""
Khang Le
CSCI 3508
4/8/19
Board Class - A 2D array that we'll be using to simulate the board of the game
"""

class Board:
    def __init__(self, _length, _width):             #initialization of the Board object's length and width
        self.length = _length
        self.width = _width
        self.board_Array = [[0] * self.width for i in range(self.length)]       #creates a 2D array of specified dimensions

    def get_Content(self, row, column):              #Function that returns the value of an element in the 2D array
        return self.board_Array[row][column]
    
    def set_Content(self, row, column, value):       #Function that sets the value of an element in the 2D array
        self.board_Array[row][column] = value

    def isFull(self, column):                        #Function that tests if a column in the 2D array is full; value of 0 represents an empty slot, 1 for player 1, 2 for player 2
        for i in range(self.length):                 #for loop that iterates down the board in a certain column
            if self.board_Array[i][column] == 0:     #if a value of 0 is read in any element then the board is not full; return false
                return False
        return True                                  #if no values of 0's are read, then the board is full; return true

    def get_OkayDokeyColumns(self):                  #Function that returns a list of values that show which columns are not full
        okayDokeyList = []                           #Creates a list/array
        for i in range(self.width):                  #for loop that uses the isFull function to test all columns of the board
            if not self.isFull(i):                   #if the column is not full then append the column number to the list
                okayDokeyList.append(i)              #appends the number of column that is not full onto the list
        return okayDokeyList                         #returns the list
    
    
"""
test = Board(5,8)                               #creates a Board class object named test
print(test.length, test.width)                  #prints the length and width variable stored in object test

for i in range(test.length):                    #prints out contents of the 2D array in test
    for r in range(test.width):
        print(test.get_Content(i,r), end=" ")
    print('\n')
"""

"""
                                                #testing the set and get functions
test.set_Content(2,5,0)                         #sets the element in row 2, column 5 to 0
print(test.get_Content(2, 5))                   #prints out the value of the element in row 2 column 5

for i in range(test.length):                    #prints out contents of 2D array
    for r in range(test.width):
        print(test.get_Content(i,r), end=" ")
    print('\n')
"""

"""
                                                #testing the isFull function
if test.isFull(5):
    print("true")
else:
    print("false")
"""

"""
                                                #testing the get_OkayDokeyColumns function
a = test.get_OkayDokeyColumns()                 
print(a)
"""
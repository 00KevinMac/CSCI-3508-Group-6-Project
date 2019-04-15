# CSCI 3508 Group 6 Project

DESCRIPTION:
-----------------------------------------------
This is a program that plays connect 4 in 
conjunction with a driver program which 
conforms to the API determined in class.
-----------------------------------------------

FILES:
-----------------------------------------------
There will be 5 modules used in this program. 
1) The main function
	Coder: The Invincible Overlord
	Arguments:
		Player # (int)
		Board width (int)
		Board height (int)
	Return value:
		(int)

The Main function will call the stream reader, 
Check the EOF Flag,pass the filled board object 
to the MDE, pass the resulting int to the 
stream writer, then loop and wait for new input.

 2) Stream reader
	Coder: The One Who Refuses to Bring a Laptop
	Arguments:
		Width (int)
		Height (int)
		EOF_flag (bool)
	Return value:
		Board object
	
The stream reader will access stdin, parse 
the Json string into a 2D int array, call 
the Board class constructor, then return 
the board. If stdin has EOF in it, the
function sets the EOF_flag and exits

3) Move Decision Engine (MDE) MVP version
	Coder: Level 7 Wizard
	Arguments: 
Board object
Player (int)
	Return value:
		Move choice (int)
	
The MDE will use some manner of algorithm 
to return a int representing a legal column. 
This column is the chosen move.






4)Stream sender
	Coder: The Vegan Who Likes Meat
	Arguments:
		Move (int)
	Return value
		Success (bool)
The stream sender will put the move into 
stdout, then return a bool representing 
the success or failure of the stream.

5) The Board class
	Coder: Level 4 Cleric
	Data Fields:
		A 2d array representing the board
Constructors: 
A constructor that takes a 2d array of ints, 
which it reads into the data field.
	
Methods:

Getters
	Arguments:
		X index (int)
		Y index (int)

	Return value:
		Contents (int)
These methods will allow for the getting of 
individual indices in the data field.

Setters
	Arguments:
		X index (int)
		Y index (int)
		Value (int)
	Return value:
		None
These methods will allow for the setting of 
individual indices in the data field.
	
Get valid columns
	Arguments:
		None
	Return value:
		Valid_moves (list<int>)
This method will return a list of ints which 
represent all the columns that can be legally moved into.

Isfull
	Arguments:
		Column index (int)
	Return value
		Full? (bool)
This method checks a column index to see if that column is full.
If it is, the method returns TRUE, if the column is not full, 
the method returns FALSE. 

HOW TO USE
-----------------------------------------------
Main must be called with three arguments:
Player number: Either 1 or 2
Width: The number of columns in the board
Height: The number of rows in the board

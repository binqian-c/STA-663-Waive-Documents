# Binqian Chai, binqianc@usc.edu
# ITP 115, Summer 2022
# Section: 31810
# Assignment 8 Extra Credit: Print Pretty Board
"""
Tic Tac Toe Helper: provides two functions to be used for a game of Tic Tac Toe
1) Check for winner: determines the current state of the board
2) Print pretty board: prints out a Tic Tac Toe board in a basic format
"""


# Given a tic, tac, toe board determine if there is a winner
# Function inputs:
#     boardList: an array of 9 strings representing the Tic Tac Toe board
#     moveCounter: an integer representing the number of moves that have been made
# Returns a string:
#     'x' if x won
#     'o' if o won
#     'n' if no one wins
#     's' if there is a stalemate
def checkForWinner(boardList, moveCounter):
    j = 0
    for i in range(0, 9, 3):
        # Check for 3 in a row
        if boardList[i] == boardList[i+1] == boardList[i+2]:
            return boardList[i]

        # Check for 3 in a column
        elif boardList[j] == boardList[j+3] == boardList[j+6]:
            return boardList[j]

        # Check the diagonal from the top left to the bottom right
        elif boardList[0] == boardList[4] == boardList[8]:
            return boardList[0]

        # Check the diagonal from top right to bottom left
        elif boardList[2] == boardList[4] == boardList[6]:
            return boardList[2]
        j += 1

    # If winner was not found and board is completely filled up, return stalemate
    if moveCounter > 8:
        return "s"

    # Otherwise, 3 in a row anywhere on the board
    return "n"


# write a function printPrettyBoard() to print out the Tic Tac Toe board
def printPrettyBoard(boardList):
    """
    function name: printPrettyBoard(boardList)
    :param boardList: a list representing the board
    :return: none
    side effect: print the pretty Tic Tac Toe board
    function description: printPrettyBoard(boardList) is to print the pretty Tic Tac Toe board
    """
    print()  # print an empty line
    counter = 0  # create a variable to represent the index position in boardList
    for i in range(3):  # when i is between 0 and 3, 3 is not included
        for j in range(3):  # when j is between 0 and 3, 3 is not included
            if j < 2:  # when the third number in each row is not reached ("2", "5", "8")
                print(boardList[counter], end=" | ")  # print each number in boardList (except "2", "5", "8") ending with " | "
            else:  # when the third number in each row is reached ("2", "5", "8")
                print(boardList[counter], end="")  # print "2", "5", "8" without starting a new line by default
            counter += 1  # add 1 to counter
        if i < 2:  # only print "---------" after row 1 and row 2
            print("\n---------")  # print "---------" in a new line
    print()  # print an empty line

# Binqian Chai, binqianc@usc.edu
# ITP 115, Summer 2022
# Section: 31810
# Assignment 8 Extra Credit: Print Pretty Board
# This program is about defining and calling functions with a helper file.
# This program simulates the game of Tic Tac Toe with either player x or player o alternatively taking a turn.
# The program will update the 3*3 board after each player's turn.
# The program will finally display the message telling who is the winner or whether stalemate is reached.
# The Tic Tac Toe game will be kept playing until the user wants to quit by entering letter other than "y".

# import ExtraCreditHelper file
import ExtraCreditHelper


# write a function isValidNumber(boardList,position) to check whether the position the user chooses to place their letter on is a valid number
# and whether the index position is available
def isValidNumber(boardList, position):
    """
    function name: isValidNumber(boardList,position)
    :param boardList: a list representing the board
    :param position: an integer representing the index position the user would like their letter to be placed on
    :return: a boolean (True or False)
    side effect: none
    function description: isValidNumber(boardList,position) is to check whether the position the user chooses to place their letter on is a valid number
    and whether the index position is available
    """
    if position in range(9):  # when the position is a valid number (from 0 to 8 inclusive)
        if boardList[position] != "x" and boardList[position] != "o":  # when the position is available
            return True
        else:  # when the position is not available
            return False
    else:  # when the position isn't a valid number
        return False


# write a function updateBoard(boardList, position, playerLetter) to update the board with the user's choice of where to put their letter on
def updateBoard(boardList, position, playerLetter):
    """
    function name: updateBoard(boardList,position,playerLetter)
    :param boardList: a list representing the board
    :param position: an integer representing the index position the user would like their letter to be placed on
    :param playerLetter: a string representing the user's letter ("x" or "o")
    :return: none
    side effect: based on the user's choice of position, change the number into the user's playerLetter
    function description: updateBoard(boardList,position,playerLetter) is to update the board with the user's choice of where to put their letter on
    """
    boardList[position] = playerLetter  # update the board with the user's ("x" or "o") choice of position


# write a function playGame() to simulate the Tic Tac Toe game; each player ("x" or "o") will take a turn; tell who is the winner
def playGame():
    """
    function name: playGame()
    :param: none
    :return: none
    side effect: display the board to the user; get user input for position; print the message when game is over; print who is the winner
    function description: playGame() is to simulate the Tic Tac Toe game with each player taking a turn; it will tell who is the winner when the game is over
    """
    boardList = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]  # create a variable boardList to represent the board
    moveCounter = 1  # create an integer variable moveCounter to count the moves for the game
    winner = "n"  # create a string variable winner to tell the winner; set it to be "n" first so that the while loop will run at least once
    while winner == "n":  # continue the game
        ExtraCreditHelper.printPrettyBoard(boardList)  # display the board to the user
        if moveCounter % 2 == 1:  # when it is player x's turn
            playerLetter = "x"  # update the playerLetter to "x"
            position = int(input("Player x, enter a number: "))  # get player x's choice of position and convert the position into an integer
            while isValidNumber(boardList, position) == False:  # when player x's choice of position is invalid or unavailable
                position = int(input("Player x, enter a number: "))  # get player x's choice of position again and convert the position into an integer
            updateBoard(boardList, position, playerLetter)  # when player x's choice of position is valid or available, update the corresponding position with "x"
        else:  # when it is player o's turn
            playerLetter = "o"  # update the playerLetter to "o"
            position = int(input("Player o, enter a number: "))  # get player o's choice of position and convert the position into an integer
            while isValidNumber(boardList, position) == False:  # when player o's choice of position is invalid or unavailable
                position = int(input("Player o, enter a number: "))  # get player o's choice of position again and convert the position into an integer
            updateBoard(boardList, position, playerLetter)  # when player o's choice of position is valid or available, update the corresponding position with "o"
        winner = ExtraCreditHelper.checkForWinner(boardList, moveCounter)  # check whether there is a winner by calling checkForWinner() and update the result into winner
        moveCounter += 1  # add 1 to the number of moves
    ExtraCreditHelper.printPrettyBoard(boardList)  # display the final board
    print("")  # print an empty line to separate the board and the game result
    print("Game Over!")  # telling the players the game is over
    if winner == "s":  # when stalemate is reached
        print("Stalemate reached.")
    elif winner == "x":  # when player x wins
        print("Player x is the winner!")
    else:  # when player o wins
        print("Player o is the winner!")


# write a function main() to start the game of Tic Tac Toe; keep playing the game until the user wants to quit
def main():
    """
    function name: main()
    parameter: none
    :return: none
    side effect: print the title of the game; print Goodbye when the user wants to quit
    function description: main() is to start the game of Tic Tac Toe.
    The game will be kept playing the game until the user wants to quit.
    """
    print("Let’s play Tic Tac Toe!")  # print the title of the game
    answer = "y"  # set answer to "y" so that the while loop will run at least once
    while answer == "y":  # when the user wants to keep playing the game
        playGame()  # call the playGame() function to play the game
        answer = input("Would you like to play another round (y or n)? ").strip().lower()  # ask the user whether they want to continue playing; get rid of white spaces and convert into lowercase
    print("Goodbye!")  # when the user wants to quit


main()  # call function main()

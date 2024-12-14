# Binqian Chai, binqianc@usc.edu
# ITP 115, Summer 2022
# Section: 31810
# Assignment 7
# Description: This program simulates the rock-paper-scissors game by defining multiple functions and calling the defined functions.
# The player will play the rock-paper-scissors game against the computer.
# The player will keep be asked to enter their choice until they want to exit the game.
# The program will then display how many times the computer wins, how many times the player wins, and how many times they tie.

# import random module
import random

# write a function displayRules() to tell the user the game rules with no parameters and no return values
# displayRules() function only has side effects
def displayRules():
    print("Let's play Rock Paper Scissors.")
    print("The rules of the game are:")
    print("\tRock smashes Scissors")  # print a tab before this line of information
    print("\tScissors cut Paper")  # print a tab before this line of information
    print("\tPaper covers Rock")  # print a tab before this line of information
    print("\tIf both the choices are the same, it's a tie")  # print a tab before this line of information

# write a function getComputerNum() to get computer's choice of rock-paper-scissors
# getComputerNum() has no parameter and returns a random integer between 0 and 2 (inclusive)
def getComputerNum():
    return random.randrange(3)  # use random module to get a random integer; selected from a group of 3 numbers starting at 0

# write a function getPlayerNum() to get user's choice of rock-paper-scissors
# getPlayerNum() has no parameter and returns the integer between 0 and 2 (inclusive) entered by the user
def getPlayerNum():
    print("Enter 0 for Rock, 1 for Paper, or 2 for Scissors")  # display the message (0-2 corresponding to rock-paper-scissors) to the user
    num = int(input("> "))  # get user input and store it in the variable num; the input should be an integer
    while num != 0 and num != 1 and num != 2:  # keep asking user input until he enters a valid input (integer between 0 and 2)
        num = int(input("> "))  # updating user input; the input should be an integer
    return num  # return the integer between 0 and 2 (inclusive) entered by the user

# write a function playRound(computerNum,playerNum) to simulate the game and determine the winner
# playRound(computerNum,playerNum) function has 2 parameters and return -1 for computer wins, 1 for player wins, 0 for a tie
def playRound(computerNum, playerNum):
    if computerNum == 0:  # when computer chooses rock
        if playerNum == 0:  # when player chooses rock
            return 0  # the player and computer tie
        elif playerNum == 1:  # when player chooses paper
            return 1  # player wins
        else:  # when player chooses scissors
            return -1  # computer wins
    elif computerNum == 1:  # when computer chooses paper
        if playerNum == 0:  # when player chooses rock
            return -1  # computer wins
        elif playerNum == 1:  # when player chooses paper
            return 0  # the player and computer tie
        else:  # when player chooses scissors
            return 1  # player wins
    else:  # when computer chooses scissors
        if playerNum == 0:  # when player chooses rock
            return 1  # player wins
        elif playerNum == 1:  # when player chooses paper
            return -1  # computer wins
        else:  # when player chooses scissors
            return 0  # the player and computer tie

# write a function continueGame() to ask the user whether he wants to continue playing rock-paper-scissors
# continueGame() function has no parameter and returns a boolean
def continueGame():
    game = input("Do you want to continue playing (y or n)? ").strip().lower()  # get user input; get rid of white spaces and convert input into lowercase
    if game == "y":  # when the user enters Y or y
        return True  # return True
    else:  # when the user enters N or n
        return False  # return False

# write a function main() with no parameters and return value
def main():
    # create variables to track the number of computer wins, player wins, and ties; the variables start at 0
    computer = 0  # the number of computer wins
    player = 0  # the number of player wins
    tie = 0  # the number of the player and computer tie
    answer = True  # do-while loop: initializing the loop, the while loop will run at least once
    while answer == True:  # when the user enters Y or y
        displayRules()  # call function displayRules() to display the game rules to the user
        computerNum = getComputerNum()  # get computer's choice by calling function getComputerNum() and store it in computerNum
        playerNum = getPlayerNum()  # get player's choice by calling function getPlayNum() and store it in playerNum
        if playRound(computerNum, playerNum) == -1:  # call playRound function; when computer wins the game
            computer += 1  # add 1 to the number of computer wins
            print("Computer wins.")  # print the message telling computer wins
        elif playRound(computerNum, playerNum) == 1:  # call playRound function; when the player wins the game
            player += 1  # add 1 to the number of player wins
            print("You win!")  # print the message telling the player he wins
        else:  # when the player and computer tie
            tie += 1  # add 1 to the number of the player and computer tie
            print("You and the computer tied.")  # print the message telling the player and computer tie
        answer = continueGame()  # updating the value stored in answer by calling continueGame() function
        print("")  # print an empty line
    print("You won", player, "game(s).")  # display the number of player wins
    print("The computer won", computer, "game(s).")  # display the number of computer wins
    print("You tied with the computer", tie, "times(s).")  # display the number of the player and computer tie


main()  # call main() function

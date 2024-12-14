# Binqian Chai, binqianc@usc.edu
# ITP 115, Summer 2022
# Section: 31810
# Assignment 6
# Description: string processing, list, and loop
# The program is to let the user guess words by giving them a jumbled word. The user can ask for hints after his first guess.
# The program ends until the user enters the correct word, and the number of guesses the user takes will be displayed.

# import the random module
import random

# create two lists; list1 and list2 are index corresponded
list1 = ["anthropologie", "violin", "mathematics"]  # list1 is the list of words
list2 = ["brand", "musical instrument", "major"]  # list2 is the list of hints for the words in list1

# get a random index and store the number in the variable index
index = random.randrange(3)

# create the jumbled word using while loop
list1String = list(list1[index])  # turn the random word in list1 into a list and hold it in list1String
jumbled = ""  # create an empty string
while len(list1String) != 0:  # when length of list1String is greater than 0
    letter = random.choice(list1String)  # randomly select an element (letter) in list1String
    jumbled += letter  # add the randomly selected letter to jumbled
    list1String.remove(letter)  # remove the selected letter from the list list1String

# print the jumbled word to the user
print("The jumbled word is", "\"" + jumbled + "\"")
# get user input to guess the word
guess = input("Enter your guess: ")
# create a variable to store the number of guesses the user take
count = 1
# have the user guess the word using while loop
while guess.strip().lower() != list1[index]:  # when the user does not enter the correct word
    count += 1  # add 1 to the number of guesses the user take
    print("That is not correct")  # tell the user he does not enter the correct word
    hint = input("Do you want a hint (y or n)? ")  # ask the user whether he needs hint or not
    if hint.strip().lower() == "y":  # if the user need hint; get rid of whitespaces and change the input to lower case
        print("The hint is", "\"" + list2[index] + "\"")  # give the user the hint
    print("The jumbled word is", "\"" + jumbled + "\"")  # print the jumbled word again
    guess = input("Enter your guess: ")  # get user input to guess the word again

# when the user enter the correct word
print("You got it!")
# tell the user the number of guesses he takes (distinguish between singular and plural)
if count == 1:  # when the user takes only 1 guess
    print("It took you", str(count), "guess.")  # singular "guess"
else:  # when the user takes more than 1 guess
    print("It took you", str(count), "guesses.")  # plural "guess" ("guesses")

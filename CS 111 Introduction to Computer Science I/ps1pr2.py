# 
# ps1pr2.py - Problem Set 1, Problem 2
#
# Indexing and slicing puzzles
#

#
# List puzzles
#

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example puzzle (puzzle 0):
# Creating the list [2, 5, 9] from pi and e
answer0 = [e[0]] + pi[-2:]

# Put your solutions to the remaining list puzzles below.
# Puzzle 1:
# Creating the list [7, 1] from pi and e
answer1 = e[1:]

# Puzzle 2:
# Creating the list [9, 1, 1] from pi and e
answer2 = pi[5::-2]

# Puzzle 3:
# Creating the list [1, 2, 3, 4, 5] from pi and e
answer3 = e[::-2] + pi[::2]




#
# String puzzles
#

b = 'boston'
u = 'university'
t = 'terriers'

# Example puzzle (puzzle 4)
# Creating the string 'bossy'
answer4 = b[:3] + t[-1] + u[-1]

# Put your solutions to the remaining string puzzles below.
# Puzzle 5:
# Creating the string 'stone'
answer5 = b[2:] + t[1]

# Puzzle 6:
# Creating the string 'nonononono'
answer6 = b[-1::-4] * 5

# Puzzle 7:
# Creating the string 'bestever'
answer7 = b[0] + u[4::2] + t[1] + u[3:6]

# Puzzle 8:
# Creating the string 'serenity'
answer8 = t[7::-2] + u[1:3] + u[8:]



# The code below tests the values of your expressions. DO NOT MODIFY IT!
if __name__ == '__main__':    
    for n in range(0, 9):
        answer_var = 'answer' + str(n)
        if answer_var in dir():
            print(answer_var, '=', eval(answer_var))

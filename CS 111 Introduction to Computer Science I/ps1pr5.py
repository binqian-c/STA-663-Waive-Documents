# 
# ps1pr5.py - Problem Set 1, Problem 5
#
# Functions on strings and lists, part I
#

# function 1
def first_and_last(values):
    """ takes a list values and returns a new list containing the first value
        of the original list followed by the last value of the original list
        input values: an arbitrary list
    """
    first = values[0]
    last = values[-1]
    return [first, last] 

# function 2
def even_odd(s):
    """ takes as input a string s and returns a new string in which all of 
        the characters that are in even positions in the original string s 
        are followed by all characters in odd positions
        input s: an aribitrary string
    """
    return s[::2] + s[1::2]
 
# function 3
def move_to_end(s, n):
    """ takes a string value s and an integer n as inputs and returns a new 
        string in which the first n characters of s have been moved to the 
        end of the string
        input s: an arbitrary string
        input n: any integer
    """
    if n >= len(s):
        return s
    else:
        return s[n:] + s[:n]






# test function with a sample test call for function 1
def test():
    """ performs test calls on the functions above """
    print('first_and_last([1, 2, 3, 4]) returns', first_and_last([1, 2, 3, 4]))

    # optional but encouraged: add test calls for your functions below
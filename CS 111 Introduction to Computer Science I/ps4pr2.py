# 
# ps4pr2.py - Problem Set 4, Problem 2
#
# Using your conversion functions
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:

# Put your functions below.

from ps4pr1 import *

# function 1
def add(b1, b2):
    """ takes as inputs b1 and b2, compute the sum of the numbers, and return 
        that sum in the form of a string that represents a binary number
        input b1: an arbitrary string that represent a binary number
        input b2: an arbitrary string that represent a binary number
    """
    n1=bin_to_dec(b1)
    n2=bin_to_dec(b2)
    b_sum=n1+n2
    return dec_to_bin(b_sum)

# function 2
def increment(b):
    """ takes as input b and returns the next larger binary number as an 
        8-character string
        input b: an arbitrary 8-character string representation of a binary number
    """
    if b=='11111111':
        return '00000000'
    else:
        n=bin_to_dec(b) 
        new_n=n+1 
        new_bin=dec_to_bin(new_n)
        if len(new_bin)<8:
            return '0'*(8-len(new_bin))+new_bin
        else:
            return new_bin
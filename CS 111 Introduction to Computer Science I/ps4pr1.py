# 
# ps4pr1.py - Problem Set 4, Problem 1
#
# From binary to decimal and back!
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:

#
# Recursive Functions
#

# Put your functions below.

# function 1
def dec_to_bin(n):
    """ takes n and uses recursion to convert it from decimal to binary – 
        constructing and returning a string version of the binary 
        representation of that number
        input n: any non-negative integer
    """
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        new_n=dec_to_bin(n>>1)
        if n % 2 ==1:
            return new_n+'1'
        else:
            return new_n+'0'

# function 2
def bin_to_dec(b):
    """ takes b and uses recursion to convert the number from binary to 
        decimal, returning the resulting integer
        input b: an arbitrary string that represents a binary number 
    """
    if b == '0':
        return 0
    elif b == '1':
        return 1
    else:
        rest_b=bin_to_dec(b[:-1])
        if b[-1]=='1':
            return 2*rest_b+1
        else:
            return 2*rest_b+0
        
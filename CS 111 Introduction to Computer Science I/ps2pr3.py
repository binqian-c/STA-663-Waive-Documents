# 
# ps2pr3.py - Problem Set 2, Problem 3
#
# More practice writing non-recursive functions
#

#
# Non-recursive Functions
#

# Put your functions below.

# Function 1
def swap_outer(s):
    """takes a input s and returns a new string in which the first and last 
       characters have been swapped
       input s: an arbitrary string
    """
    if len(s)<=2:
        return s
    else:
        return s[-1]+s[1:-1]+s[0]

# Function 2
def adjust(vals, length):
    """ takes as inputs vals and length and returns a new list in 
        which the value of vals has been adjusted as necessary to produce a 
        list with the specified length
        input vals: an arbitrary list
        input length: a non-negative interger
    """
    if len(vals)>=length:
        return vals[:length]
    else:
        return vals[:]+[0]*(length-len(vals))


# test function with a sample test call for function 1
def test():
    """ performs test calls on the functions above """
    s='computer'
    print('swap_outer(s) returns', swap_outer(s))
    # optional but encouraged: add test calls for your functions below
    
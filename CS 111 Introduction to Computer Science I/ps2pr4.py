# 
# ps2pr4.py - Problem Set 2, Problem 4
#
# Fun with recursion, part I
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:

#
# Recursive Functions
#

# Put your functions below.

# Function 1
def process(vals):
    """takes as input vals and uses recursion to compute and returns the sum 
       of the squares of the individual numbers in the list
       input vals: an arbitrary list of numbers
    """
    if vals==[]:
        return 0
    else:
       rest_vals=process(vals[1:])
       return rest_vals+vals[0]**2

# Function 2
def count_spaces(s):
    """ takes a string input s and uses recursion to determine 
        and return the number of spaces in s
        input s: an arbitrary string 
    """
    if s=='':
        return 0
    else:
        rest_space=count_spaces(s[1:]) 
        if s[0]==' ':
            return 1+rest_space
        else:
            return 0+rest_space
        
# Function 3
def copy(s, n):
    """ takes a string s and an integer n and uses recursion to create and 
        return a string in which n copies of s have been concatenated together
        input s: an arbitrary string
        input n: any interger
    """
    if n<=0:
            return ''
    else:
        rest_string=copy(s,n-1)
        return s+rest_string



# test function with a sample test call for function 1
def test():
    """ performs test calls on the functions above """
    print('process([2, 5, 3]) returns', process([2, 5, 3]))

    # optional but encouraged: add test calls for your functions below
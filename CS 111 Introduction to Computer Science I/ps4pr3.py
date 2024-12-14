# 
# ps4pr3.py - Problem Set 4, Problem 3
#
# Recursive operations on binary numbers
#

# Put your functions below.

# Function 1
def bitwise_and(b1, b2):
    """ takes as inputs b1 and b2, uses recursion to compute the bitwise AND 
        of the two numbers and returns the result in the form of a string
        input b1: an arbitrary string that represent a binary number
        input b2: an arbitrary string that represent a binary number
    """
    if b1=='' and b2=='':
        return ''
    elif b1=='':
        return '0'*len(b2)
    elif b2=='':
        return '0'*len(b1)
    else:
        rest_bit=bitwise_and(b1[:-1], b2[:-1])
        if b1[-1]=='1' and b2[-1]=='1':
            return rest_bit+'1'
        else:
            return rest_bit+'0'
        
def add_bitwise(b1, b2):
    """ takes as inputs b1 and b2, uses recursion to perform the bitwise, 
        elementary-school addition algorithm, returns the result in the form 
        of a string
        input b1: an arbitrary string that represent a binary number
        input b2: an arbitrary string that represent a binary number
    """
    if b1=='' and b2=='':
        return ''
    elif b1=='':
        return b2
    elif b2=='':
        return b1
    else:
        sum_rest=add_bitwise(b1[:-1], b2[:-1])
        if b1[-1]=='1' and b2[-1]=='1':
            return add_bitwise(sum_rest,'1')+'0'
        elif b1[-1]=='0' and b2[-1]=='1':
            return sum_rest+'1'
        elif b1[-1]=='1' and b2[-1]=='0':
            return sum_rest+'1'
        else:
            return sum_rest+'0'
    
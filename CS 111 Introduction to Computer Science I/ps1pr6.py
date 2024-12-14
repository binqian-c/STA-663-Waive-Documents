# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions on strings and lists, part II
#

# function 1
def longer_len(s1, s2):
    """ takes two string values s1 and s2 as inputs and returns the string 
        with the longer length
        input s1: an arbitrary string 
        input s2: an arbitrary string
    """
    if len(s1) > len(s2) or len(s1) == len(s2):
        return s1
    else:
        return s2
    
# function 2
def is_pal(s):
    """ takes a string s as input and returns True if s is a palindrome and 
        False otherwise 
        input s: an arbitrary string
    """
    if s[::1] == s[::-1]:
        a= True
        return a
    else:
        b= False
        return b

# function 3
def replace_end(values, new_end_vals):
    """ takes a list values and another list new_end_vals as inputs and 
        returns a new list in which the elements in new_end_vals have 
        replaced the last n elements of the list values, where n is the 
        length of new_end_vals
        input values: an arbitrary list
        input new_end_vals: an arbitrary list
    """
    a=len(new_end_vals)
    b=len(values)
    if a >= b:
         return new_end_vals[:]
    else:
        return values[:(b - a)] + new_end_vals[:]

# function 4
def repeat_elem(values, index, num_times):
    """ takes a list values, an integer index, and a positive integer 
        num_times as inputs, and returns a new list in which the element of 
        values at position index has been repeated num_times times
        input values: an arbitrary list
        input index: any integer
        input num_times: any positive integer
    """
    a=index
    b=num_times
    return values[:a] + [values[a]] * b + values[a+1:]



    
# test function with a sample test call for function 1
def test():
    """ performs test calls on the functions above """
    s1='computer'
    s2='compute'
    print('longer_len(s1,s2) returns', longer_len(s1,s2))
    
    # optional but encouraged: add test calls for your functions below
    
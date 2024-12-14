# 
# ps3pr2.py - Problem Set 3, Problem 2
#
# Algorithm design
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:

#
# List comprehensions and Recursion
#

# Put your functions below.

# Function 1
def consonants_lc(s):
    """takes as input s and returns a list containing the consonants 
       (if any) in s
       input s: an arbitrary string of lowercase letters
    """
    con_lc=[x for x in s if x not in 'aeiou']
    return con_lc

# Function 2
def consonants_rec(s):
    """ takes as input a string s and returns a list containing the consonants 
        (if any) in s
        input s: an arbitrary string of lowercase letters
    """
    if s=='':
        return []
    else:
        con_rest=consonants_rec(s[1:])
        if s[0] in 'aeiou':
            return con_rest
        else:
            return [s[0]]+con_rest

# Function 3
def num_consonants(s):
    """ takes as input s and returns the number of consonants in s
        input s: an arbitrary string
    """
    return len(consonants_lc(s))

# Function 4
def most_consonants(wordlist):
    """ takes as input wordlist and returns the word in the list with the 
        most consonants
        input wordlist: an arbitrary list of lowercase words
    """
    lc=[[num_consonants(s),s] for s in wordlist]
    most_con=max(lc)
    return most_con[1]

# Function 5
def num_multiples(m, values):
    """ takes as inputs m and values and returns the number of integers in 
        values that are multiples of m
        input m: any integer
        input values: an arbitrary list of integers
    """
    mul_lc=[x for x in values if x % m == 0]
    return len(mul_lc)

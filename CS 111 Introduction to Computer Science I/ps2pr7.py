# 
# ps2pr7.py - Problem Set 2, Problem 7
#
# Fun with recursion, part II
#

#
# Recursive Functions
#

# Put your functions below.

# Function 1
def letter_score(letter):
    """takes letter as input and returns the value of that letter 
       as a scrabble tile
       input letter: an arbitrary lowercase letter
    """
    if letter in ['a','e','i','l','n','o','r','s','t','u']:
        return 1
    elif letter in ['d','g']:
        return 2
    elif letter in ['b','c','m','p']:
        return 3
    elif letter in ['f','h','v','w','y']:
        return 4
    elif letter in ['k']:
        return 5
    elif letter in ['j','x']:
        return 8
    elif letter in ['q','z']:
        return 10
    else:
        return 0

# Function 2
def scrabble_score(word):
    """ takes as input word and return the scrabble score of that string
        input word: an arbitrary string containing only lowercase letters
    """
    if word=='':
        return 0
    else:
        rest_word=scrabble_score(word[1:])
        return letter_score(word[0])+rest_word
    
        
# Function 3
def BUtify(s):
    """ takes as input s and return a new string in which all lower-case bs 
        are replaced by upper-case Bs and all lower-case us are replaced by 
        upper-case Us
        input s: an arbitrary string
    """
    if s=='':
            return ''
    else:
        rest_string=BUtify(s[1:])
        if s[0] in 'u':
            return 'U'+rest_string
        elif s[0] in 'b':
            return 'B'+rest_string
        else:
            return s[0]+rest_string
        
# Function 4
def diff(vals1, vals2):
    """ takes as inputs vals1 and vals2 and return a new list in which each 
        element is the the absolute value of the difference of the 
        corresponding elements from the original lists
        input vals1: an arbitrary list of non-negative intergers
        input vals2: an arbitrary list of non-negative intergers
    """
    if vals1==[] and vals2==[]:
        return []
    elif vals1==[]:
        return vals2[len(vals1):]
    elif vals2==[]:
        return vals1[len(vals2):]
    else:
        x=vals1[0]-vals2[0]
        rest_vals=diff(vals1[1:], vals2[1:])
        if x<0:
            return [x*(-1)]+rest_vals
        else:
            return [x]+rest_vals

# 
# ps3pr4.py - Problem Set 3, Problem 4
#
# More algorithm design
#

# Put your functions below.

# Function 1
def rem_last(elem, values):
    """takes as inputs elem and values and return a version of values in 
       which the last occurrence of elem (if any) has been removed
       input elem: any number
       input values: an arbitrary list
    """
    if values==[]:
        return []
    else:
        rem_rest=rem_last(elem, values[1:])
        if values[0]==elem:
            if values[0] in values[1:]:
                return [values[0]]+rem_rest
            else:
                return rem_rest
        else:
            return [values[0]]+rem_rest

# Function 2
def find(elem, seq):
    """ takes as inputs elem and seq and returns the index of the first 
        occurrence of elem in seq; if seq is a string, elem will be a 
        single-character string; if seq is a list, elem can be any value 
        input elem: an arbitrary element
        input seq: an arbitrary sequence
    """
    if len(seq)==0:
        return -1
    elif elem==seq[0]:
        return 0
    else:
        rest_seq=find(elem, seq[1:])
        if rest_seq==-1:
            return -1
        else:
            return 1+rest_seq

# Function 3
# a helper function
def remove(elem,s):
    """ takes elem and s as inputs and returns a new string with the first 
        occurences of elem removed from s
        input s: an arbitrary string
        input elem: an arbitrary element of string
    """
    if s=='':
        return ''
    elif s[0]==elem:
        return s[1:]
    else: 
        rest_s=remove(elem, s[1:])
        return s[0]+rest_s

def jscore(s1, s2):
    """ takes two strings s1 and s2 as inputs and returns the Jotto score of 
        s1 compared with s2
        input s1: an arbitrary string
        input s2: an arbitrary string
    """
    if s1=='' or s2=='':
        return 0
    else:
        js_rest=jscore(s1[1:],remove(s1[0], s2))
        if s1[0] in s2:
            return 1+js_rest
        else:
            return js_rest

        
        
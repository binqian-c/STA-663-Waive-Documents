#
# ps3pr3.py (Problem Set 3, Problem 3)        
#
# Caesar cipher / decipher
#

# A template for a helper function called rot that we recommend you write
# as part of your work on the encipher function.
def rot(c, n):
    """ rotates c forward by n spots in the alphabet 
        input c: an arbitrary single-character string
        input n: any non-negative integer
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    # Put the rest of your code for this function below.   
    if 'a'<= c <= 'z':
        new_ord=ord(c)+n
        if new_ord > ord('z'):
            new_ord= new_ord - 26
    elif 'A' <= c <= 'Z':
        new_ord=ord(c)+n
        if new_ord > ord('Z'):
            new_ord= new_ord - 26
    else:
        new_ord=ord(c)
    return chr(new_ord)

### Put your code for the encipher function below. ###
def encipher(s, n):
    """ takes as inputs s and n and returns a new string in which the letters 
        in s have been “rotated” by n characters forward in the alphabet, 
        wrapping around as needed; only letters change
        input s: an arbitrary string
        input n: any non-negative integer between 0 and 25
    """
    if s=='':
        return ''
    else:
        enci_rest=encipher(s[1:],n)
        return rot(s[0],n)+enci_rest


# A helper function that could be useful when assessing
# the "Englishness" of a phrase.
# You do *NOT* need to modify this function.
def letter_prob(c):
    """ if c is the space character (' ') or an alphabetic character,
        returns c's monogram probability (for English);
        returns 1.0 for any other character.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character   
    assert(type(c) == str and len(c) == 1)

    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0

#### Put your code for the decipher function below. ####
# a helper function 
def sum_prob(a):
    """ takes a as input and returns the sum of the probability of each letter 
        in a
        input a: an arbitrary string
    """
    sum_lc=[letter_prob(x) for x in a]
    return sum(sum_lc)

# Use list comprehention first to list all the possible decipherings and 
# calculate the total probability of each possible deciphering, then compare 
# the total probability and returns the deciphering with the maximum probablity
def decipher(s):
    """ takes as input s that has already been enciphered by having its 
        characters “rotated” by some amount (possibly 0) and returns the 
        original English string
        input s: an arbitrary string
    """
    dec_lc=[encipher(s,n) for n in range(26)]
    dec_prob=[[sum_prob(y), y] for y in dec_lc]
    max_prob=max(dec_prob)
    return max_prob[1]

        
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
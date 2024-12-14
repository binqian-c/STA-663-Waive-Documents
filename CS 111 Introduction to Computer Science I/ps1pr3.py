# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below
# function 1
def cube(x):
    """ returns the cube of its input
        input x: any number (int or float)
    """
    return x**3

# function 2
def convert_to_inches(yards, feet):
    """ returns the corresponding inputs yards and feet in inches 
        input yards: any number (int or float)
        input feet: any number (int or float)
    """
    if yards<0:
        yards=0
    if feet<0:
        feet=0
    return yards*36 + feet*12

# function 3
def area_sq_inches(height_yds, height_ft, width_yds, width_ft):
    """ return the area of the rectangle in square inches 
        input height_yds: any number (int or float)
        input height_ft: any number (int or float)
        input width_yds: any number (int or float)
        input width_ft: any number (int or float)
    """
    height= convert_to_inches(height_yds, height_ft)
    width= convert_to_inches(width_yds, width_ft)
    return height * width

# function 4
def median(a, b, c):
    """ returns the median of the three inputs 
        input a: any number (int or float)
        input b: any number (int or float)
        input c: any number (int or float)
    """
    if a >= b and a >= c:
        if b >= c:
            return b
        else:
            return c
    elif b >= a and b >= c:
        if a >= c:
            return a
        else:
            return c
    elif c >= b and c >= a:
        if a >= b:
            return a
        else: 
            return b




# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))

    # optional but encouraged: add test calls for your functions below

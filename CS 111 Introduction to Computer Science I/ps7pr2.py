#
# ps7pr2.py (Problem Set 7, Problem 2)
#
# 2-D Lists
#
# Computer Science 111
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
# 

def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []
    
    for r in range(height):
        row = [0] * width     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line, and nothing between values.
        input: grid is a 2-D list. We assume that all of the cell
               values are integers between 0 and 9.
    """
    height = len(grid)
    width = len(grid[0])
    
    for r in range(height):
        for c in range(width):
            print(grid[r][c], end='')   # print nothing between values
        print()                         # at end of row, go to next line

# function 0
def diagonal_grid(height, width):
    """ creates and returns a height x width grid in which the cells
        on the diagonal are set to 1, and all other cells are 0.
        inputs: height and width are non-negative integers
    """
    grid = create_grid(height, width)   # initially all 0s

    for r in range(height):
        for c in range(width):
            if r == c:
                grid[r][c] = 1

    return grid

# function 1
def inner_grid(height, width, digit):
    """ creates and returns a 2-D list of height rows and width columns in 
        which the “inner” cells all have a value of digit and the cells on the 
        outer border are all 0
        input height: any non-negative integer
        input width: any non-negative integer
        input digit: any integer between 0 and 9 inclusive
    """
    grid = create_grid(height, width)
    
    for r in range(1, (height-1)):
        for c in range(1, (width-1)):
            grid[r][c] = digit
        
    return grid

# function 2
def copy(grid):
    """ creates and returns a deep copy of grid–a new, separate 2-D list that 
        has the same dimensions and cell values as grid
    """
    new_grid=create_grid(len(grid),len(grid[0]))
    
    for r in range(len(new_grid)):
        for c in range(len(new_grid[0])):
            new_grid[r][c]=grid[r][c]
            
    return new_grid

# function 3
def add_one(grid):
    """ takes an existing 2-D list of digits and adds 1 to the value of each 
        digit. If adding 1 to a given digit gives it a value of 10 (i.e., if 
        the original digit was a 9), then the digit should “wrap around” and 
        become a 0
        input grid: an arbitrary 2-D list
    """
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]==9:
                grid[r][c]=0
            else:
                grid[r][c] +=1

# function 4
def negate_bits(grid):
    """ takes an existing 2-D list of binary digits (0s and 1s) and negates 
        all of the bits – changing the 0s to 1s and the 1s to 0s
        input grid: an arbitrary 2-D list that only contains 0s and 1s
    """
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c]==1:
                grid[r][c]=0
            else:
                grid[r][c]=1

# function 5
def num_nonzero_row(grid, r):
    """ takes grid and r as inputs, and counts and returns the number of 
        nonzero digits in the row whose index is r
        input grid: an existing 2-D list of digits
        input r: any integer
    """
    count=0
    
    for c in range(len(grid[0])):
        if grid[r][c] !=0:
            count +=1
            
    return count
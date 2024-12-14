#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# TT Securities    
#
# Computer Science 111
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Find the average price')
    print('(4) Find the median price')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.
# function for option 3
def avg_price(prices):
    """ takes a list of 1 or more prices and computes and returns the average 
        price
        input: prices is a list of 1 or more numbers
    """
    a = 0
    for i in prices:
        a += i
    return a / len(prices)

# function for option 4
def median_price(prices):
    """ takes a list of 1 or more prices and computes and returns the median 
        of the prices
        input: prices is a list of 1 or more numbers
    """
    copy = prices[:]
    copy.sort()
    if len(copy) % 2 != 0:
        return copy[len(copy) // 2]
    else:
        c = copy[len(copy) // 2 - 1] + copy[len(copy) // 2]
        return c / 2

# function for option 5
def max_day(prices):
    """ takes a list of 1 or more prices and computes and returns the day 
        (i.e., the index) of the maximum price
        input: prices is a list of 1 or more numbers
    """
    m = 0
    for i in range(len(prices)):
        if prices[i] > prices[m]:
            m = i
    return m

# function for option 6
def any_above(prices, threshold):
    """ takes a list of 1 or more prices and an integer threshold, and uses 
        a loop to determine if there are any prices above that threshold
        input: prices is a list of 1 or more numbers
        input threshold: any integer
    """
    for i in prices:
        if i > threshold:
            return True
    return False

# function for option 7
def find_tts(prices):
    """ takes a list of 2 or more prices, and that uses one or more loops to 
        find the best days on which to buy and sell the stock whose prices are 
        given in the list of prices
        input: prices is a list of 2 or more numbers
    """
    l1 = prices[:]
    a = 0
    b = 1
    diff = l1[b] - l1[a]
    for x in range(len(l1)):
        l2 = prices[(x+1):]
        for y in range(len(l2)):
            d = l2[y] - l1[x]
            if d > diff:
                diff = d
                a = x
                b = x + 1 + y
    return [a,b,diff]

def tts():
    """ the main user-interaction loop
    """
    prices = []
    threshold = ''

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            average = avg_price(prices)
            print('The average price is',average)
        
        elif choice == 4:
            median = median_price(prices)
            print('The median price is',median)
        
        elif choice == 5:
            day_max = max_day(prices)
            print('The max price is',prices[day_max],'on day',day_max)
        
        elif choice == 6:
            threshold = int(input('Enter the threshold: '))
            if any_above(prices, threshold) == True:
                print('There is at least one price above',threshold)
            else:
                print('There are no prices above',threshold)
        
        elif choice == 7:
            strategy = find_tts(prices)
            print(' Buy on day',strategy[0],'at price',prices[strategy[0]])
            print('Sell on day',strategy[1],'at price',prices[strategy[1]])
            print('Total profit:',strategy[2])
            
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')

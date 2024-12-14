#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month = init_month
        self.day = init_day
        self.year = init_year

    # The function for the Date class that returns a string
    # representation of a Date object.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this *can* be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self): 
        """ Returns True if the called object is
            in a leap year, and False otherwise.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, and year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

    #### Put your code for problem 2 below. ####
    #### Make sure that it is indented by an appropriate amount. ####
    # Problem 2
    
    # Problem 3
    def advance_one(self):
        """ changes the called object so that it represents one calendar day 
            after the date that it originally represented
        """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year() == True and self.month == 2:
            if self.day == 29:
                self.day = 1
                self.month += 1
            else:
                self.day += 1
        else:
            if self.month == 12 and self.day == 31:
                self.day = 1
                self. month = 1
                self.year += 1
            elif self.day == days_in_month[self.month]:
                self.month += 1
                self.day = 1
            else:
                self.day += 1
            
    # Problem 4
    def advance_n(self, n):
        """ changes the calling object so that it represents n calendar days 
            after the date it originally represented, and print all of the 
            dates from the starting date to the finishing date, inclusive of 
            both endpoints
            input n: any nonnegative integer
        """
        for i in range(n+1):
            if i == 0:
                print(self)
            else:
                self.advance_one() 
                print(self)
        
    # Problem 5
    def __eq__(self, other):
        """ returns True if the called object (self) and the argument (other) 
            represent the same calendar date, and False otherwise
        """
        if self.month == other.month and self.day == other.day and self.year == other.year:
            return True
        else:
            return False
    
    # Problem 6
    def is_before(self, other):
        """ returns True if the called object represents a calendar date that 
            occurs before the calendar date that is represented by other
        """
        if self.year < other.year:
            return True
        elif self.month < other.month and self.year == other.year:
            return True
        elif self.day < other.day and self.month == other.month and self.year == other.year:
            return True
        else:
            return False
    
    # Problem 7
    def is_after(self, other):
        """ returns True if the calling object represents a calendar date 
            that occurs after the calendar date that is represented by other
            and False otherwise
        """
        if self.year > other.year:
            return True
        elif self.month > other.month and self.year == other.year:
            return True
        elif self.day > other.day and self.month == other.month and self.year == other.year:
            return True
        else:
            return False
        
    # Problem 8
    def days_between(self, other):
        """ returns an integer that represents the number of days between self 
            and other
        """
        a = self.copy()
        b = other.copy()
        count = 0
        if self.is_before(other) == True:
            while a.is_before(b) == True:
                a.advance_one()
                count = count - 1
        else:
            while b.is_before(a) == True:
                b.advance_one()
                count = count + 1
        return count

    # Problem 9
    def day_name(self):
        """ returns a string that indicates the name of the day of the week 
            of the Date object that calls it
        """
        day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        a = self.days_between(Date(4, 5, 2021))
        a %= len(day_names)
        return day_names[a]

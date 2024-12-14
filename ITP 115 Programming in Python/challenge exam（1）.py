# CS 102 Placement Exam
# University of Southern California
#
# Given a hotel with 30 floors numbered 1-30 and up to 100 rooms per floor
# so that the lower 2 digits are the room number and upper digits are the
# floor number, take reservations that consist of pairs of inputs that
# represent the number of nights and a room number (each on a separate line)
# and terminated by "0 0", and output
#   a.) the average duration (number of nights) of a reservation,
#   b.) the floor number (1-30) that had the most reservations. If there is
#       a tie for the floor with the most reservations, you may output ANY
#       one of the floors that tied.
# For error checking of input values, you should ignore any input that
# has an illegal room number (i.e. above 3099 or below 100) or an input
# that has a negative number of nights for the reservation. Instead, count
# how many of these errors occur and output those values. So, in addition,
# to the outputting a. and b. described above, also output
#   c.) the number of invalid room numbers entered
#   d.) the number of negative reservation durations
#
# We guarantee inputs from the user will contain at least one valid entry
# so that there will always be a floor with the most reservations and a
# non-zero average duration.
#
# No other error conditions need be checked for and we guarantee the input
# will match our described format (two integers per line and terminated
# by a line with "0 0").
#
# Your program should compute the desired values a. through d. described
# above. Then, We have provided a function, `printResults()` below that you
# MUST call to output those answers in a format that will our automated
# tests will recognized.
#
# An example input and output sequence is shown below.
#
# Sample input:
# -------------
# | 101 2
# | 3099 3
# | 2054 -1
# | 3100 -1
# | 99 2
# | -546 3
# | 3064 2
# | 0 0
# -------------
#
# In the above there are only 3 valid input lines (the first 2 and the last).
# There are 3 lines with invalid room numbers (3100, 99, -546) and
# 2 lines with negative night durations.  Notice that one input line can
# contain both and invalid room number AND a negative night duration.
# 2.3333 is the average number of nights per reservation for the valid inputs.
# And floor 30 is the floor with the most reservations.
#
# The correct output of your program for this input is shown below:
# -------------
# | Average nights per reservation: 2.33333
# | Floor with most reservations: 30
# | Invalid room numbers: 3
# | Number of negative nights: 2
# -------------
#
# If you are unable to produce all 4 answers, you may pass dummy values
# (e.g. 0) to printResults(), but still produce and pass the answers you
# can correctly compute.

# You may not import other modules but must use built-ins

# Helper function to print out your computed results in
# the desired format to match our automated tests.
# ------------------------- DO NOT ALTER THIS CODE ---------------------
def printResults(avgNights,
                 mostUsedFloor,
                 numInvalidRoomNumbers,
                 numNegativeNights):
    print("Average nights per reservation: " + str(avgNights));
    print("Floor with most reservations: " + str(mostUsedFloor));
    print("Invalid room numbers: " + str(numInvalidRoomNumbers));
    print("Number of negative nights: " + str(numNegativeNights));



def main():
    # Add your code here to declare data values, read the input,
    # and compute the desired answers.
    rooms = []
    nights = []
    line = input("Please enter a line of reservation: ").strip()
    while line != "0 0":
        list = line.split(" ")
        rooms.append(list[0])
        nights.append(list[1])
        line = input("Please enter a line of reservation: ").strip()

    numInvalidRoomNumbers = 0
    totalNights = 0
    numInputs = 0
    numNegativeNights = 0
    for room in rooms:
        index = rooms.index(room)
        night = int(nights[index])
        room = int(room)
        if room > 3099 or room < 100:
            numInvalidRoomNumbers += 1
        if night < 0:
            numNegativeNights += 1
        if night > 0 and room in range(101, 3100):
            numInputs += 1
            totalNights += night

    list_floor = []
    floor_night = []
    for rm in rooms:
        floor = rm[:2]
        list_floor.append(floor)
        index2 = rooms.index(rm)
        ni = int(nights[index2])
        floor_night.append(ni)
        if floor in list_floor:
            floor_index = list_floor.index(floor)
            floor_night[floor_index] += ni
    maxNight = max(floor_night)
    index3 = floor_night.index(maxNight)
    maxFloor = list_floor[index3]


    # call printResults before exiting and pass it your answers
    printResults(totalNights / numInputs, maxFloor, numInvalidRoomNumbers, numNegativeNights)


if __name__ == "__main__":
    main()

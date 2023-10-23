
import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if year == 1918:
        return "26.09.1918"
    elif (year < 1918 and year % 4 == 0) or \
            (year > 1918 and ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))):
        return "12.09.{}".format(year)
    else:
        return "13.09.{}".format(year)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
#Logic:
#The function first checks for the special case of the transition year 1918, returning '26.09.1918'. For other years, it uses a ternary conditional operator to check if the year is a leap year based on either the Julian or Gregorian calendar, returning '12.09.YYYY' for leap years and '13.09.YYYY' for non-leap years, where 'YYYY' is the input year."
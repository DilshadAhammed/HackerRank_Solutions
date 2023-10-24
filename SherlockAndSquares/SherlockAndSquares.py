#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    return int(math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
#Explanation:
""""
1. math.sqrt(b): Calculate the square root of the largest number b.
2. math.sqrt(a): Calculate the square root of the smallest number a.
3. math.floor(math.sqrt(b)): Take the floor value of the square root of b to get the largest integer whose square is less than or equal to b.
4. math.ceil(math.sqrt(a)): Take the ceiling value of the square root of a to get the smallest integer whose square is greater than or equal to a.
5. Subtract the ceiling value from the floor value and add 1. This represents the count of perfect squares within the range [a, b].
6. Return the count of perfect squares as the result.
"""


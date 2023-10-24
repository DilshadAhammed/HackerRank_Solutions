#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

def saveThePrisoner(n, m, s):
    # Write your code here
    remaining_sweets = m % n
    
    final_position = (s + remaining_sweets - 1) % n
    return final_position if final_position != 0 else n    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
#Explanation:
"""
1. remaining_sweets = m % n: Calculate the number of sweets left after distributing to complete rounds of all prisoners. This helps determine the position of the prisoner who will receive the last sweet.

2. (s + remaining_sweets - 1) % n: Calculate the final position of the prisoner who receives the last sweet. Subtracting 1 accounts for 1-based indexing (Python uses 0-based indexing) and the modulo operation ensures the position remains within the range [1, n].

3. Handle the edge case where the final position is 0 (the last prisoner). In this case, return the total number of prisoners n.

This logic ensures the correct prisoner receives the last sweet and handles the scenario where the distribution loops back to the first prisoner after reaching the last prisoner.
"""

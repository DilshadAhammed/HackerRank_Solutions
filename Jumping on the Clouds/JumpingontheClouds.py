#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    jumps = 0
    i = 0
    while i < len(c) - 1:
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
    return jumps
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
#Explanation:
"""
1. jumps = 0: Initialize a variable to count the number of jumps needed to reach the end, starting at 0.

2. i = 0: Initialize the current position to the first cloud (index 0).

3. The while loop continues until the current position i is less than the index of the last cloud (i.e., len(c) - 1).

4. Inside the loop:

Check if a double jump (two clouds ahead) is safe and within bounds (i + 2 < len(c)). If it is, perform the double jump by increasing i by 2.
If a double jump is not safe or not within bounds, perform a single jump by increasing i by 1.
5. Increment the jumps count after each jump.

6. Once the loop ends, return the total number of jumps, which represents the minimum number of jumps required to reach the end of the cloud sequence.

This logic minimizes the number of jumps by always taking double jumps when it's safe to do so, resulting in the shortest path to the end.
"""
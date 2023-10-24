#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here
    rotation_index = k % len(a)
    
    rotated_array = a[-rotation_index:] + a[:-rotation_index]
    
    results = [rotated_array[q] for q in queries]
    
    return results
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#Explanation:
"""
1. rotation_index = k % len(a): Calculate the effective rotation index to avoid unnecessary full rotations. Taking the modulo with the length of the array ensures that the rotation index is within the bounds of the array length.

2. rotated_array = a[-rotation_index:] + a[:-rotation_index]: Perform the circular rotation by slicing the array into two parts: elements from the negative rotation index to the end, and elements from the start to the negative rotation index. Concatenate these two parts to form the rotated array.

3. results = [rotated_array[q] for q in queries]: For each query index q, extract the corresponding element from the rotated array and store it in the results list. This answers the queries about the rotated array.
"""

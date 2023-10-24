#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    element_indices = {}
    
    min_distance = float('inf')
    
    for i, num in enumerate(a):
        if num in element_indices:
            
            min_distance = min(min_distance, i - element_indices[num])
        
        
        element_indices[num] = i
    return min_distance if min_distance != float('inf') else -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
#Explanation:
""""
1. Create a dictionary element_indices to store the most recent index of each element encountered in the array a.

2. Initialize the min_distance variable to a large value (float('inf')).

3. Iterate through the array a using enumeration to keep track of the indices.

4. For each element, check if it has been encountered before (num in element_indices). If it has, calculate the distance between the current index and the most recent index where the element was seen (i - element_indices[num]). Update min_distance with the smaller value between the current minimum distance and the calculated distance.

5. Update the most recent index of the current element in the element_indices dictionary.

6. After iterating through the array, if min_distance remains as the initial large value, it means no equal elements were found, so return -1. Otherwise, return the calculated min_distance representing the minimum distance between equal elements.
"""

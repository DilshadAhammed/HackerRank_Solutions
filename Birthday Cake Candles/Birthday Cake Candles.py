#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    max_height = max(candles)
    count = candles.count(max_height)
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
#Explanation:
"""
1.The max function is used to find the maximum height among all the candles in the input list candles.

2.The count method is then used to count how many times the maximum height appears in the list, indicating how many candles have the tallest height.

3.The count is returned as the result.

For example, if the input list candles is [4, 4, 1, 3, 2, 4], the function will identify that the tallest candles have a height of 4 and count how many times 4 appears in the list, which is 3. Therefore, the function will return 3 as the output.
"""

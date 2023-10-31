#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    c=1
    for char in s:
        if char.isupper():
            c+=1
    return c
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
#explanation:
# In summary, the camelcase function calculates the number of words in a camel case string by counting the uppercase letters, assuming each uppercase letter signifies the start of a new word.

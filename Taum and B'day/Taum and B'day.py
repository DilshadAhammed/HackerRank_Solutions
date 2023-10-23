#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#

def taumBday(b, w, bc, wc, z):
    # Write your code here
    return b * min(bc, wc + z) + w * min(wc, bc + z)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
#Explanation:
"""
1. min(bc, wc + z): Calculates the minimum cost of purchasing black gifts. It compares the cost of black gifts (bc) with the cost of converting white gifts to black gifts (wc + z). It chooses the lower cost option.

2. min(wc, bc + z): Calculates the minimum cost of purchasing white gifts. It compares the cost of white gifts (wc) with the cost of converting black gifts to white gifts (bc + z). It chooses the lower cost option.

3. b * min(bc, wc + z) + w * min(wc, bc + z): Calculates the total minimum cost. Multiplies the minimum cost of black gifts by the number of black gifts (b) and the minimum cost of white gifts by the number of white gifts (w), then sums the two costs.

This logic ensures that the function minimizes the total cost by considering both the direct purchase costs and the conversion costs.
"""
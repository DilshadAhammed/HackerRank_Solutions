#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    max_topics = 0
    max_teams = 0
    
    for i in range(len(topic)):
        for j in range(i + 1, len(topic)):
            current_topics = bin(int(topic[i], 2) | int(topic[j], 2)).count('1')
            if current_topics > max_topics:
                max_topics = current_topics
                max_teams = 1
            elif current_topics == max_topics:
                max_teams += 1
    
    return [max_topics, max_teams]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
#Explanation:
"""
1.The function iterates through all possible pairs of people using nested loops.

2.For each pair, it calculates the number of topics they know by performing a bitwise OR operation (int(topic[i], 2) | int(topic[j], 2)) to find the combined topics, then counts the number of set bits (1s) using bin(...).count('1').

3.If the current pair knows more topics than the previous maximum, it updates the max_topics and resets the max_teams count to 1. If the current pair knows the same number of topics as the maximum, it increments the max_teams count.

4.Finally, the function returns a list containing the maximum number of topics and the number of teams knowing that maximum number of topics.

This code finds the maximum number of topics a team can know and how many teams can achieve that maximum number, based on the given list of topics.
"""
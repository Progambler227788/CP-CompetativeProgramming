
import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def solve(n, k):

    # Write your code here
    remainder_count = [0] * k

    for i in range(1, n + 1):
        remainder_count[i % k] += 1

    pairs = 0
    pairs += (remainder_count[0] * (remainder_count[0] - 1)) // 2

    for r in range(1, (k // 2) + 1):
        if r != k - r:
            pairs += remainder_count[r] * remainder_count[k - r]
        else:
            pairs += (remainder_count[r] * (remainder_count[r] - 1)) // 2

    return pairs
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = solve(n, k)

        print(result)
        
        

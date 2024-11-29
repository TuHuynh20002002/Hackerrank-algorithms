#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#


def birthday(s, d, m):
    # Write your code here
    ways = 0
    for idx_main in range(len(s) - m + 1):
        temp_sum = 0
        for idx_sub in range(idx_main, idx_main+m):
            temp_sum += s[idx_sub]
        print(temp_sum)
        if temp_sum == d:
            ways += 1
    return ways


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

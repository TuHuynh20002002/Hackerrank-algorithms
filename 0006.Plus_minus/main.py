#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    count_positive = 0
    count_negative = 0
    count_zero = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count_zero += 1
        if arr[i] > 0:
            count_positive += 1
        if arr[i] < 0:
            count_negative += 1
    return [count_positive/len(arr), count_negative/len(arr), count_zero/len(arr)]


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = plusMinus(arr)
    for i in range(len(result)):
        print(result[i])

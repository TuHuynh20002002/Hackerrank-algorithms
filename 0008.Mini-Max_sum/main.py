#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    sum_min = sum(arr[0:4])
    sum_max = sum(arr[-4:])
    return ([sum_min, sum_max])


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    result = miniMaxSum(arr)
    for i in result:
        print(i, end=" ")

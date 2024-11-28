#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    AM_or_PM = s[-2:]
    if (AM_or_PM == 'PM') and (int(s[0:2]) != 12):
        new_string = str(int(s[0:2])+12) + s[2:-2]
    elif (AM_or_PM == 'AM') and (int(s[0:2]) == 12):
        new_string = "00" + s[2:-2]
    else:
        new_string = s[0:-2]
    return new_string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

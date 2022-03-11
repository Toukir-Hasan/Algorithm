#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    left=[]
    right=[]
    equal=arr[0]
    for x in range(0,len(arr)):
        if (equal>arr[x]):
            left.append(arr[x])

        elif(equal<arr[x] or equal==arr[x] ):
            right.append(arr[x])
    return (left+right)


if __name__ == '__main__':


    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)
    print(result)


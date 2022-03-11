#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    a=1
    b=arr[-1]


    for x in range(0,len(arr)):
        if(a!=len(arr)):
            if b<arr[-1-a]:
                arr.pop(-a)
                arr.insert(-a,arr[-a])
                print(*arr)
            else:
             arr.pop(-x)
             (arr.insert(-x,b))
             print (*arr)
             break
        else:
            arr.pop(-x)
            (arr.insert(-x, b))
            print(*arr)
            break
        a+=1




if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

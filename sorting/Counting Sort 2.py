#!/bin/python3

import math
import os
import random
import re
import sys


def countingSort(arr):
    a=max(arr)
    result=[0]*(a+1)
    c=[]

    for x in range(0,len(arr)):
        b=arr[x]
        result[b]=result[b]+1
    print(result)
    for y in range(0,len(result)):
        if result[y]!=0:
            for z in range(0,result[y]):
                c.append(y)
    return c






if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print (result)

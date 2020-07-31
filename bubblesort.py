# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:25:15 2020

@author: crist
"""


import math
import os
import random
import re
import sys

if __name__ == '__main__':

    x = list(map(int, input().rstrip().split())) #try adding 4 2 3 1 or whatever values you would like to run



def CSwaps(x):
    if (sorted(x) == x):
        swap=0
        print('Array is sorted in', swap, 'swaps.')
        print('First Element:', x[0])
        print('Last Element:', x[-1])  
    else:
        swap=0
        for i in range(len(x)):
            for j in range(len(x)-1):
                if x[j]>x[j+1]:
                    x[j],x[j+1]=x[j+1],x[j]
                    swap+=1
        print('Array is sorted in', swap, 'swaps.')
        print('First Element:', x[0])
        print('Last Element:', x[-1])   
 
CSwaps(x)

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    b = {}
    r = 0
    cont = True
    while cont:
        cont = False
        for i in xrange(n - 1):
            if q[i] > q[i + 1]:
                if not q[i] in b:
                    b[q[i]] = 0
                b[q[i]] += 1
                if b[q[i]] > 2:
                    cont = False
                    r = "Too chaotic"
                    break
                q[i],q[i + 1] = q[i + 1],q[i]
                r += 1
                cont = True
    print r
    
if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
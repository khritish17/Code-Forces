"""
    Link: https://codeforces.com/problemset/problem/1872/C
"""

import sys
import math

input = sys.stdin.readline

def solve(l, r):
    if r < 4:
        return -1, -1
    if l != r:
        if r % 2 == 0:
            return r-2, 2
        else:
            return r-3, 2
    else:
        for i in range(2, int(math.sqrt(l)) + 1):
            if l % i == 0:
                return i, l - i
        return -1, -1 

t = int(input().strip())
for _ in range(t):
    l, r = map(int, input().strip().split(" "))
    a, b = solve(l, r)
    if a == -1:
        print("-1")
    else:
        print(f"{a} {b}")
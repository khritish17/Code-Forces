"""
    Link: https://codeforces.com/problemset/problem/1201/C
"""

import sys

tokens = iter(sys.stdin.read().split())
n, k = int(next(tokens)), int(next(tokens))
a = [int(next(tokens)) for _ in range(n)]

a.sort()

mid = n//2

sorted_half = a[mid:]
m = len(sorted_half)
cost = 0
ans = sorted_half[0]

for i in range(1, m):
    cost = (sorted_half[i] - sorted_half[i - 1])*i
    if k >= cost:
        ans = sorted_half[i]
        k -= cost
    else:
        ans += k//i
        k = 0
        break
if k > 0:
    ans += k//m
sys.stdout.write(f"{ans}\n")





"""
    https://codeforces.com/problemset/problem/1133/C
"""

import sys

tokens = iter(sys.stdin.read().strip().split())
n = int(next(tokens))

a = [int(next(tokens)) for _ in range(n)]

a.sort()
l = 0
ans = 1
for r in range(n):
    ele = a[r]
    while l <= r and abs(a[r] - a[l]) > 5:
        l += 1
    ans = max(ans, r - l + 1)
sys.stdout.write(f"{ans}\n")
    

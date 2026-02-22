"""
    Link: https://codeforces.com/problemset/problem/1183/c
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

q = int(next(tokens))
ans = []
for _ in range(q):
    k, n, a, b =  int(next(tokens)), int(next(tokens)), int(next(tokens)), int(next(tokens))
    if k - n * b <= 0:
        ans.append("-1")
        continue
    else:
        x = (k - 1 - (n*b))//(a - b)
        x = min(x, n)
        ans.append(str(x))

sys.stdout.write("\n".join(ans))

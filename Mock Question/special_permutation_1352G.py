"""
    Link: https://codeforces.com/problemset/problem/1352/G
"""

import sys
from collections import deque

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
ans = []
for _ in range(t):
    n = int(next(tokens))
    if n < 4:
        ans.append("-1")
        continue
    even = []
    odd = []

    for i in range(1, n + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    final_arr = odd[::-1] + even[:2][::-1] + even[2:]
    final_arr = list(map(str, final_arr))
    ans.append(" ".join(final_arr))
sys.stdout.write("\n".join(ans))
"""
    Link: https://codeforces.com/problemset/problem/1669/H
    Level: 1300
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
ans = []
for _ in range(t):
    n, k = int(next(tokens)), int(next(tokens))
    a = [int(next(tokens)) for _ in range(n)]

    bits = [0] * 31
    res = 0
    for i in range(31):
        index = 30 - i
        for ele in a:
            if not (ele & (1 << index)):
                bits[i] += 1
        if index <= 30:
            if bits[i] <= k:
                k -= bits[i]
                bits[i] = 0
        if bits[i] == 0:
            res += 2**index
    ans.append(str(res))

sys.stdout.write("\n".join(ans))
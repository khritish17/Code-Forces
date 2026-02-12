"""
    https://codeforces.com/problemset/problem/1367/C
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
for _ in range(t):
    n, k = int(next(tokens)), int(next(tokens))
    s = next(tokens)
    ones = [i for i, ele in enumerate(s) if ele == "1"]
    ones = [-k-1] + ones + [n + k]
    ans = 0
    for i in range(len(ones) - 1):
        gap = ones[i + 1] - ones[i] - 1
        ans += max(0, (gap -k)//(k + 1) )
    sys.stdout.write(f"{ans}\n")
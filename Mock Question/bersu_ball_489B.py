"""
    https://codeforces.com/problemset/problem/489/B
"""

import sys
tokens = iter(sys.stdin.read().strip().split())

n = int(next(tokens))
boys = [int(next(tokens)) for _ in range(n)]

m = int(next(tokens))
girls = [int(next(tokens)) for _ in range(m)]

boys.sort()
girls.sort()

b, g = 0, 0
pairs  = 0
while b < n and g < m:
    if abs(boys[b] - girls[g]) <= 1:
        pairs += 1
        b += 1
        g += 1
    elif boys[b] < girls[g]:
        b += 1
    else:
        g += 1

sys.stdout.write(f"{pairs}\n")

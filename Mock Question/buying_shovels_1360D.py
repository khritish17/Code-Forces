"""
    Link: https://codeforces.com/problemset/problem/1360/D
"""

import sys
import math


def solve(n, k):
    div = 1
    for d in range(1, int(math.sqrt(n)) + 1):
        if n % d == 0:
            if 1 <= d <= k:
                div = max(div, d) 
            if 1 <= n//d <= k:
                div = max(div, n//d)
    return str(n//div)
            
input = sys.stdin.read().strip().split()

i = 0
t = int(input[i])
i += 1
ans = []
for _ in range(t):
    n, k = map(int, input[i: i+ 2])
    i += 2
    ans.append(solve(n, k))

sys.stdout.write("\n".join(ans))
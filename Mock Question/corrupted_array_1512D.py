"""
    Link: https://codeforces.com/problemset/problem/1512/D
"""

import sys
import bisect

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
ans = []
for _ in range(t):
    n = int(next(tokens))
    b = [int(next(tokens)) for _ in range(n + 2)]

    b.sort()
    prefix_sum = sum(b[:n + 1])

    # case 1: b[n] is the sum
    cur_pre_sum = prefix_sum - b[n]
    if cur_pre_sum == b[n]:
        a = list(map(str, b[:n]))
        ans.append(" ".join(a))
        continue
    
    # case 2: b[n + 1] is the sum
    possible_x = prefix_sum - b[n + 1]
    index = bisect.bisect_left(b, possible_x, lo=0, hi=n + 1)
    if index <= n and b[index] == possible_x:
        a = b[:index] + b[index+1:n+1]
        a = list(map(str, a))
        ans.append(" ".join(a))
        continue

    ans.append("-1")

sys.stdout.write("\n".join(ans))



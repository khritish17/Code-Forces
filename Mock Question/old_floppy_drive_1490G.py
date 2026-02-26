"""
    Link: https://codeforces.com/problemset/problem/1490/G
"""

import sys
import math
import bisect

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))

ans = []
for _ in range(t):
    n, m = int(next(tokens)), int(next(tokens))
    a = [int(next(tokens)) for _ in range(n)]
    x = [int(next(tokens)) for _ in range(m)]
    
    prefix_sum = 0
    max_prefix = []
    max_idx = []
    M = 0
    
    for i in range(n):
        ele = a[i]
        prefix_sum += ele
        if max_prefix:
            if prefix_sum > max_prefix[-1]:
                max_prefix.append(prefix_sum)
                max_idx.append(i)
        else:
            max_prefix.append(prefix_sum)
            max_idx.append(i)
    
    M = max(max_prefix)
    S = prefix_sum
    
    res = []
    for xi in x:
        if xi > M and S <= 0:
            res.append("-1")
            continue
        k = 0
        if xi > M:
            k = math.ceil((xi - M)/S)
        rem = xi - k*S
        
        pos = bisect.bisect_left(max_prefix, rem)
        p = max_idx[pos]
        res.append(str(k*n + p))
    ans.append(" ".join(res))

sys.stdout.write("\n".join(ans))
        


    
        
"""
    Link: https://codeforces.com/problemset/problem/1619/E
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
res = []
for _ in range(t):
    n = int(next(tokens))
    a = [int(next(tokens)) for _ in range(n)]

    freq = [0] * (n + 1)
    spare_pool = []
    for ele in a:
        freq[ele] += 1
    
    permanent_cost = 0
    ans = []
    possible = True
    for i in range(n + 1):
        if not possible:
            ans.append(-1)
            continue
        cost = permanent_cost + freq[i]
        ans.append(cost)
        if freq[i] > 0:
            for _ in range(freq[i] - 1):
                spare_pool.append(i)
        else:
            if spare_pool:
                permanent_cost += i - spare_pool.pop()
            else:
                possible = False
    ans = list(map(str, ans))
    res.append(" ".join(ans))

sys.stdout.write("\n".join(res))

            

"""
    https://codeforces.com/problemset/problem/1343/C
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))

for _ in range(t):
    n = int(next(tokens))
    a = [int(next(tokens)) for x in range(n)]
    
    cur_arr = []
    ans = 0
    for ele in a:
        if not cur_arr:
            cur_arr.append(ele)
            continue
        if ele/cur_arr[-1] > 0:
            cur_arr.append(ele)
        else:
            ans += max(cur_arr)
            cur_arr = [ele]
    ans += max(cur_arr)
    print(ans)

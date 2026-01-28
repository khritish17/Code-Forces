"""
    Link: https://codeforces.com/problemset/problem/1692/E
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
ans = []
for _ in range(t):
    n, s = int(next(tokens)), int(next(tokens))
    a = [int(next(tokens)) for _ in range(n)]
    if sum(a) < s:
        ans.append(-1)
        continue
    l = 0
    cur_sum = 0
    max_length = 0
    for r in range(n):
        cur_sum += a[r]

        while cur_sum > s:
            cur_sum -= a[l]
            l += 1
        
        if cur_sum == s:
            max_length = max(max_length, r - l + 1)
    ans.append(n - max_length)
ans = list(map(str, ans))
sys.stdout.write("\n".join(ans))
        

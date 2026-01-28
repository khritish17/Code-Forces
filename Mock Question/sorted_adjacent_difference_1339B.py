"""
    Link: https://codeforces.com/problemset/problem/1339/B
"""

import sys

tokens = iter(sys.stdin.read().strip().split())
t = int(next(tokens))

res =[]
for _ in range(t):
    n = int(next(tokens))
    a = [int(next(tokens)) for i in range(n)]

    a.sort()
    start = n//2
    ans = [a[start]]
    l = start -1 
    r = start  + 1
    for i in range(n - 1):
        if l >= 0:
            ans.append(a[l])
            l -= 1
        if r < n:
            ans.append(a[r])
            r += 1
    ans = list(map(str, ans))
    res.append(" ".join(ans))
sys.stdout.write("\n".join(res))
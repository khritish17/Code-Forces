"""
    Link: https://codeforces.com/problemset/problem/1614/B
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))

ans = []
for _ in range(t):
    n = int(next(tokens))
    a = [(int(next(tokens)),i) for i in range(n)]

    a.sort(reverse=True)
    x = [0]*n
    xi = 1
    res = 0
    for i in range(n):
        ai, ind = a[i]
        if i % 2 == 1:
            x[ind] = str(-xi)
            res += ai*(xi * 2)
            xi += 1
        else:
            x[ind] = str(xi)
            res += ai*(xi * 2)
    ans.append(str(res))
    ans.append("0 " + " ".join(x))
sys.stdout.write("\n".join(ans))

    


"""
    Link: https://codeforces.com/problemset/problem/1559/C
    Level: 1200
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
ans = []
for _ in range(t):
    n = int(next(tokens))
    a = [int(next(tokens)) for _ in range(n)]
    path = []
    if a[0] == 1:
        path.append(str(n + 1))
        for i in range(1, n+1):
            path.append(str(i))
    elif a[n - 1] == 0:
        for i in range(1, n+1):
            path.append(str(i))
        path.append(str(n + 1))
    else:
        for i in range(1, n + 1):
            ind = i - 1
            path.append(str(i))
            if a[ind] == 0 and a[ind + 1] == 1:
                path.append(str(n + 1))
                for j in range(i + 1, n + 1):
                    path.append(str(j))
                break
    ans.append(" ".join(path))

sys.stdout.write("\n".join(ans))



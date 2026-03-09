"""
    Link: https://codeforces.com/problemset/problem/1360/E
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
ans = []

for _ in range(t):
    n = int(next(tokens))
    field = [list(next(tokens)) for _ in range(n)]

    possible = True
    for i in range(n - 1):
        for j in range(n - 1):
            if field[i][j] == '1':
                if field[i + 1][j] == "0" and field[i][j + 1] == "0":
                    possible = False
                    break
        if not possible:
            break
    
    if possible:
        ans.append("YES")
    else:
        ans.append("NO")

sys.stdout.write("\n".join(ans))
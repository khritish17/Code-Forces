"""
    https://codeforces.com/problemset/problem/1669/G
    Level: 1200
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
ans = []


for _ in range(t):
    n, m = int(next(tokens)), int(next(tokens))
    ans_grid = [["."] * m for _ in range(n)]
    grid = []
    for _ in range(n):
        row = list(next(tokens))
        grid.append(row)
    
    for j in range(m):
        index = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j] == "o":
                ans_grid[i][j] = "o"
                index = i - 1
            elif grid[i][j] == "*":
                ans_grid[index][j] = "*"
                index -= 1
    for i in range(n):
        ans.append("".join(ans_grid[i]))

sys.stdout.write("\n".join(ans))
    
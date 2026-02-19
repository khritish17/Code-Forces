"""
    Link: https://codeforces.com/problemset/problem/1703/E
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))

ans = []
for _ in range(t):
    n = int(next(tokens))
    grid = []
    for _ in range(n):
        row = list(next(tokens))
        grid.append(row)
    
    flips = 0
    for i in range(n//2):
        for j in range((n+1)//2):
            coords = [(i, j), (j, n - i -1), (n - i -1, n - j - 1), (n - j -1, i)]
            count_one = 0
            for dx, dy in coords:
                if grid[dx][dy] == "1":
                    count_one += 1
            count_zero = 4 - count_one
            flips += min(count_one, count_zero)
    ans.append(flips)
ans = list(map(str, ans))
sys.stdout.write("\n".join(ans))
    



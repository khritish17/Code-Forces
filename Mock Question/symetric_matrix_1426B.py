"""
    Link: https://codeforces.com/problemset/problem/1426/B
    level: 900
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
ans= []
for _ in range(t):
    n, m = int(next(tokens)), int(next(tokens))
    sym_diag = False
    even_matrix = True
    if m % 2 == 1:
        even_matrix = False
    
    for _ in range(n):
        top_left = int(next(tokens))
        top_right = int(next(tokens))
        bottom_left = int(next(tokens))
        bottom_right = int(next(tokens))

        if top_right ==  bottom_left:
            sym_diag = True
    
    if even_matrix and sym_diag:
        ans.append("YES")
    else:
        ans.append("NO")

sys.stdout.write("\n".join(ans))
        
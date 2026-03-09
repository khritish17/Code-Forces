"""
    Link: https://codeforces.com/problemset/problem/1520/E
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
ans = []
for _ in range(t):
    n = int(next(tokens))
    order = list(next(tokens))
    pos = [i for i, ele in enumerate(order) if ele == "*"]
    if not pos:
        ans.append("0")
        continue
    median_index = len(pos)//2

    moves = 0
    median = pos[median_index]
    for i in range(len(pos)):
        target_pos = median - (median_index - i)
        moves += abs(pos[i] - target_pos)
    ans.append(str(moves))

    

sys.stdout.write("\n".join(ans))

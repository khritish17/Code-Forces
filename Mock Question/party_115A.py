"""
    https://codeforces.com/problemset/problem/115/A
    level: 900
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

n = int(next(tokens))

stack = []
adj_list = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    imd_mngr = int(next(tokens))
    if imd_mngr == -1:
        stack.append(i)
    else:
        adj_list[imd_mngr].append(i)

level = 0
while stack:
    new_stack = []
    for ele in stack:
        for node in adj_list[ele]:
            new_stack.append(node)
    level += 1
    stack = new_stack

sys.stdout.write(f"{level}\n")


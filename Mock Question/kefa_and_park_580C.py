"""
    Link: https://codeforces.com/problemset/problem/580/C
    Level: 1500
"""
import sys

tokens = iter(sys.stdin.read().strip().split())

n = int(next(tokens))
m = int(next(tokens))
isCat = [0]+[int(next(tokens)) for _ in range(n)]

adj_list = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y = int(next(tokens)), int(next(tokens))
    adj_list[x].append(y)
    adj_list[y].append(x)

stack = [(1, isCat[1], 0)] # (node, cat_count, parent)

count = 0

while stack:
    node, cat_count, parent = stack.pop()
    if cat_count > m:
        continue
    adj_nodes = adj_list[node]
    if adj_nodes == [parent] and node != 1:
        if cat_count <= m:
            count += 1

    for adj_node in adj_nodes:
        if adj_node == parent:
            continue
        if isCat[adj_node] == 1:
            stack.append((adj_node, cat_count + 1, node))
        else:
            stack.append((adj_node, 0, node))

sys.stdout.write(f"{count}\n")




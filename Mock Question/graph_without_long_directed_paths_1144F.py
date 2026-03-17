"""
    Link: https://codeforces.com/problemset/problem/1144/F
    Level: 1700
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

n, m = int(next(tokens)), int(next(tokens))
adj_list = [[] for _ in range(n + 1)]

node_color = [-1] * (n + 1) # -1: not visited, 0: into the node, 1: out of the node
edges = []
for _ in range(m):
    u, v = int(next(tokens)), int(next(tokens))
    edges.append((u, v))
    adj_list[u].append(v)
    adj_list[v].append(u)

stack = [(1, 0)]
node_color[1] = 0
possible = True
while stack:
    node, color = stack.pop()
    next_color = 1 if color == 0 else 0
    for next_node in adj_list[node]:
        if node_color[next_node] == -1:
            node_color[next_node] = next_color
            stack.append((next_node, next_color))
        elif node_color[next_node] != next_color:
            possible = False
            break
    if not possible:
        break

if possible:
    seq = []
    for u, v in edges:
        if node_color[u] == 0 and node_color[v] == 1:
            seq.append("1")
        else:
            seq.append("0")
    sys.stdout.write(f"YES\n{"".join(seq)}")
else:
    sys.stdout.write(f"NO\n")





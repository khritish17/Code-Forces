"""
    Link: https://codeforces.com/problemset/problem/1328/E
    Level: 1900
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

n, m = int(next(tokens)), int(next(tokens))
adj_list = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = int(next(tokens)), int(next(tokens))
    adj_list[u].append(v)
    adj_list[v].append(u)
depths = [0] * (n + 1)
time_in = [0] * (n + 1)
time_out = [0] * (n + 1)
parents = [0] *(n + 1)

stack = [(1, False)] # (node, backttrack)
time = 0
while stack:
    node, backtrack =  stack.pop()
    if node != 1 and not backtrack:
        depths[node] = depths[parents[node]] + 1
    if not backtrack:
        time_in[node] = time
        stack.append((node, True))
        for next_node in adj_list[node]:
            if next_node == parents[node]:
                continue
            stack.append((next_node, False))
            parents[next_node] = node
    else:
        time_out[node] = time
    time += 1


def is_ancestor(node, anc_node):
    ti_anc_node, to_anc_node = time_in[anc_node], time_out[anc_node]
    ti_node, to_node = time_in[node], time_out[node]
    if ti_anc_node <= ti_node  and to_node <= to_anc_node:
        return True
    return False
ans = []
for _ in range(m):
    k = int(next(tokens))
    queries = []
    for _ in range(k):
        node = int(next(tokens))
        queries.append((depths[node], parents[node] if node != 1 else 1))
    queries.sort(reverse=True)
    possible = True
    for i in range(1, k):
        node, node_anc = queries[0][1], queries[i][1]
        if not is_ancestor(node, node_anc):
            possible = False
            break
    if possible:
        ans.append("YES")
    else:
        ans.append("NO")

sys.stdout.write("\n".join(ans))
    



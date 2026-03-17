"""
    Link: https://codeforces.com/problemset/problem/161/D
    level: 1800
    Choose language as PyPy 3
"""

import sys
from collections import deque

tokens = iter(sys.stdin.read().strip().split())

n, k = int(next(tokens)), int(next(tokens))
adj_list = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = int(next(tokens)), int(next(tokens))
    adj_list[a].append(b)
    adj_list[b].append(a)

# post order
order = []
parent = [-1] * (n + 1)
visited = [False] * (n + 1)
visited[1] = True
q = deque([1])

while q:
    node = q.popleft()
    order.append(node)
    for child_node in adj_list[node]:
        if visited[child_node] == False:
            q.append(child_node)
            visited[child_node] = True
            parent[child_node] = node

dp = [[0] * (k + 1) for _ in range(n + 1)]

ans = 0
for u in reversed(order):
    dp[u][0] = 1
    for v in adj_list[u]:
        if v != parent[u]:
            for l in range(k):
                ans += dp[u][l] * dp[v][k - l - 1]
            
            for l in range(k):
                dp[u][l + 1] += dp[v][l]
sys.stdout.write(f"{ans}\n")


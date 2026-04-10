"""
    https://codeforces.com/problemset/problem/1334/C
    level:  1600
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
ans = []
for _ in range(t):
    n = int(next(tokens))
    a = []
    b = []
    for _ in range(n):
        a.append(int(next(tokens)))
        b.append(int(next(tokens)))
    
    cost_sum = 0
    for i in range(n):
        cost_sum += max(0, a[i] - b[(i - 1)%n]) 
    
    min_bullets = float('inf')
    for i in range(n):
        cost = cost_sum - max(0, a[i] - b[(i - 1)%n]) + a[i]
        min_bullets = min(min_bullets, cost)
    ans.append(f"{min_bullets}")

sys.stdout.write("\n".join(ans))

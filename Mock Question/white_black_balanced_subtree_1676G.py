"""
    Link: https://codeforces.com/problemset/problem/1676/G
"""

import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    parents = [-1,-1] + list(map(int, input().strip().split(" ")))
    colors = ["*"] + list(input().strip())

    balance = [0]
    for cl in colors[1:]:
        if cl == "B":
            balance.append(-1)
        else:
            balance.append(1)
    
    for i in range(n, 1, -1):
        parent_i = parents[i]
        balance[parent_i] += balance[i]
    
    count = 0
    for ele in balance[1:]:
        if ele == 0:
            count += 1
    sys.stdout.write(f"{count}\n")
    

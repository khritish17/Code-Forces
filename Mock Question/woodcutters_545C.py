"""
    https://codeforces.com/problemset/problem/545/C
    Level: 1500
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

n = int(next(tokens))

pos = []
height = []

for _ in range(n):
    pos.append(int(next(tokens)))
    height.append(int(next(tokens)))

last_occupied_pos = None

cut = 0
for i in range(n):
    x = pos[i]
    h = height[i]
    if i == 0:
        cut += 1
        last_occupied_pos = x
        continue

    if i == n - 1:
        cut += 1
        continue
    
    if x - h > last_occupied_pos:
        cut += 1
        last_occupied_pos = x
    elif x + h < pos[i + 1]:
        cut += 1
        last_occupied_pos = x + h
    else:
        last_occupied_pos = x
sys.stdout.write(f"{cut}\n")


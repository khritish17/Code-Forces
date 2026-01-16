"""
    Docstring for Practice.Level 800.bit_plus_plus
    link: https://codeforces.com/problemset/problem/282/A
"""

import sys

input = sys.stdin.readline

n = int(input())
x = 0
for _ in range(n):
    oprn = input()
    if "++" in oprn:
        x += 1
    elif "--" in oprn:
        x -= 1
print(x)
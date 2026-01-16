"""
    Docstring for Practice.Level 800.team
    link: https://codeforces.com/problemset/problem/231/A
"""
import sys

input = sys.stdin.readline

n = int(input())
count = 0
for _ in range(n):
    p, v, t = map(int, input().split(" "))
    if p + v + t >= 2:
        count += 1
print(count)
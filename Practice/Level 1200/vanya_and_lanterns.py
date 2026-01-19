"""
    Docstring for vanya_and_lanterns
    Link: https://codeforces.com/problemset/problem/492/B
"""
import sys

input = sys.stdin.readline

n, l = map(int, input().strip().split(" "))
lamps = list(map(int, input().strip().split(" ")))

lamps.sort()

max_diff = 0
for i in range(1, len(lamps)):
    max_diff = max(max_diff, lamps[i] - lamps[i - 1])

d1 = lamps[0]
d2 = l - lamps[-1]

print(max(max_diff/2, d1, d2))
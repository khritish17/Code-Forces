"""
    LInk: https://codeforces.com/problemset/problem/158/A
"""

import sys

input = sys.stdin.readline

n, k = map(int, input().split(" "))
scores = list(map(int, input().split(" ")))

scores.sort(reverse=True)
limit = scores[k - 1]

count = 0
for ele in scores:
    if ele > 0 and ele >= limit:
        count += 1

print(count)
"""
Docstring for twins
Link: https://codeforces.com/problemset/problem/160/A
"""

import sys

input = sys.stdin.readline

n = int(input().strip())

coins = list(map(int, input().strip().split(" ")))

total = sum(coins)
coins.sort(reverse=True)

count = 0
coin_sum = 0
for ele in coins:
    coin_sum += ele
    count += 1
    if coin_sum > total//2:
        break
print(count)
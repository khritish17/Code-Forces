"""
Docstring for even_odds
Link: https://codeforces.com/problemset/problem/318/A
"""

import sys

input = sys.stdin.readline

n, k = map(int, input().strip().split(" "))

even_count = n//2
odd_count = n - n//2

if k <= odd_count:
    print(2*k - 1)
else:
    print(2*(k - odd_count))
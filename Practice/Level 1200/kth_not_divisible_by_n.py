"""
    Docstring for kth_not_divisible_by_n
    Link: https://codeforces.com/problemset/problem/1352/C
"""

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().strip().split(" "))
    exact_block = (k - 1)//(n -1)
    rem = (k - 1)%(n - 1)
    ans = n * exact_block + rem + 1
    print(ans)

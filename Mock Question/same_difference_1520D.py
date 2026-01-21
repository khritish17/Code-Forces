"""
    Link: https://codeforces.com/problemset/problem/1520/D
"""

import sys

input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = map(int, input().strip().split(" "))

    hash_map = {}
    counts = 0
    for i, ele in enumerate(arr):
        diff = ele - i
        if diff in hash_map:
            counts += hash_map[diff]
            hash_map[diff] += 1
        else:
            hash_map[diff] = 1
    print(counts)


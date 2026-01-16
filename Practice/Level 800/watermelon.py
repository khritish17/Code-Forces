"""
Question Link: https://codeforces.com/problemset/problem/4/A
"""

import sys
input = sys.stdin.readline


w = int(input())
if w > 2 and w % 2 == 0:
    print("YES")
else:
    print("NO")

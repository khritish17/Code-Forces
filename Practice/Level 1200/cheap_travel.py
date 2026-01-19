"""
    Docstring for cheap_travel
    link: https://codeforces.com/problemset/problem/466/A
"""

import sys

input = sys.stdin.readline

n, m, a, b = map(int, input().strip().split(" "))
option1 = (n//m)*b + (n % m)*a
option2 = n * a
option3 = ((n + m - 1) // m)*b
print(min(option1, option2, option3))
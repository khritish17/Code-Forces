"""
    Docstring for pair_of_topics_1324D
    Link: https://codeforces.com/problemset/problem/1324/D
"""

import sys

input = sys.stdin.readline


n = int(input().strip())
a = list(map(int, input().strip().split(" ")))
b = list(map(int, input().strip().split(" ")))

c = []
for i in range(n):
    ai = a[i]
    bi = b[i]
    c.append(ai - bi)

c.sort()
i, j = 0, len(c) - 1

ans = 0
while i < j:
    if c[i] + c[j] > 0:
        ans += j - i
        j -= 1
    else:
        i += 1
print(ans)
"""
    https://codeforces.com/problemset/problem/1324/E
    Level: 1700
"""

import sys
tokens = iter(sys.stdin.read().strip().split())

n, h, l, r = int(next(tokens)), int(next(tokens)), int(next(tokens)), int(next(tokens))
a = [int(next(tokens)) for _ in range(n)]


prev_dp = [0] * h

i = n - 1
while i >= 0:
    cur_dp = [0] * h
    for j in range(h):
        option1 = prev_dp[(j + a[i]) % h] + (1 if l <= (j + a[i]) % h <= r else 0)
        option2 = prev_dp[(j + a[i] -1) % h] + (1 if l <= (j + a[i] - 1) % h <= r else 0)
        cur_dp[j] =  max(option1, option2)
    prev_dp = cur_dp
    i -= 1
sys.stdout.write(f"{prev_dp[0]}\n")


"""
    https://codeforces.com/problemset/problem/455/A
    level: 1500
"""
import sys

tokens = iter(sys.stdin.read().strip().split())

n = int(next(tokens))
a = []
limit = 10**5
freq = [0] * (limit + 1)
for _ in range(n):
    val = int(next(tokens))
    a.append(val)
    freq[val] += 1

dp = [0] * (limit + 1)

for i in range(limit + 1):
    option_1 = i * freq[i] + (dp[i - 2] if i - 2 >= 0 else 0)
    option_2 = dp[i - 1] if i - 1 >= 0 else 0
    dp[i] = max(option_1, option_2)

sys.stdout.write(f"{dp[limit]}\n")
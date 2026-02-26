"""
    Link: https://codeforces.com/problemset/problem/1514/B
    Level: 1200
"""

import sys
tokens = iter(sys.stdin.read().strip().split())
MOD = (10**9) + 7
t = int(next(tokens))
ans = []
for _ in range(t):
    n, k = int(next(tokens)), int(next(tokens))
    ans.append(str(pow(n, k, MOD)))

sys.stdout.write("\n".join(ans))
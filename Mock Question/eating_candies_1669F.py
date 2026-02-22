"""
    Link: https://codeforces.com/problemset/problem/1669/F
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))

ans = []
for _ in range(t):
    n = int(next(tokens))
    candies = [int(next(tokens)) for _ in range(n)]
    alice , bob = 0, n - 1
    alice_wt = 0
    bob_wt = 0
    count = 0
    while alice <= bob:
        if alice_wt <= bob_wt:
            alice_wt += candies[alice]
            alice += 1
        else:
            bob_wt += candies[bob]
            bob -= 1
        
        if alice_wt == bob_wt:
            count = alice + n - bob - 1
    ans.append(count)

ans = list(map(str, ans))

sys.stdout.write("\n".join(ans))

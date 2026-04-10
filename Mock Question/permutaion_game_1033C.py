"""
    https://codeforces.com/problemset/problem/1033/C
    level: 1600
"""

import sys
tokens = iter(sys.stdin.read().strip().split())

n = int(next(tokens))
a = [int(next(tokens)) for _ in range(n)]

pos = [0] * (n + 1)

for i in range(n):
    pos[a[i]] = i

dp = [False] * n
for i in range(n, 0, -1):
    val = i
    cur_ind = pos[i]
    can_win = False

    for next_indx in range(cur_ind + val, n, val):
        if a[next_indx] > val:
            if not dp[next_indx]:
                can_win = True
                break
    if not can_win:
        for next_indx in range(cur_ind - val, -1, -val):
            if a[next_indx] > val:
                if not dp[next_indx]:
                    can_win = True
                    break
    if can_win:
        dp[cur_ind] = True

ans = ["A" if ele else "B" for ele in dp]
sys.stdout.write("".join(ans))





"""
    Link: https://codeforces.com/problemset/problem/1619/C
"""

import sys
from collections import deque

tokens  = iter(sys.stdin.read().strip().split())


t = int(next(tokens))
ans = []
for _ in range(t):
    a, s = next(tokens), next(tokens)
    
    A, S = list(map(int, a)), list(map(int, s))
    B = deque()
    possible = True
    while S:
        a_val = A.pop() if A else 0
        s_val = S.pop()

        if s_val >= a_val:
            B.appendleft(s_val - a_val)
        else:
            expected_b = 10 + s_val - a_val
            if not S or S.pop() != 1:
                possible = False
                break
            else:
                B.appendleft(expected_b)
    if A:
        possible = False
    if possible:
        ans.append("".join(list(map(str, B))).lstrip('0'))
    else:
        ans.append("-1")
sys.stdout.write("\n".join(ans))

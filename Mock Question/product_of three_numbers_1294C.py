"""
    https://codeforces.com/problemset/problem/1294/C
    Level: 1300
"""

import sys, math

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
ans = []
for _ in range(t):
    n = int(next(tokens))
    a, b, c = -1, -1, -1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            a = i
            n = n//a
            break
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and i != a:
            b = i
            c = n//b
            break
    
    if c >=2 and a != b and b != c and c != a:
        ans.append(f"YES\n{a} {b} {c}")
    else:
        ans.append("NO")

sys.stdout.write("\n".join(ans))
    
    
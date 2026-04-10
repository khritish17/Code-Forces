"""
    https://codeforces.com/problemset/problem/2210/C1?locale=en
    Level: 
"""

import sys, math

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
res = []
for _ in range(t):
    n = int(next(tokens))
    a = [int(next(tokens)) for _ in range(n)]
    b = [int(next(tokens)) for _ in range(n)]

    ans = 0
    for i in range(n):
        A = math.gcd(a[(i - 1)%n], a[i])
        B = math.gcd(a[i], a[(i + 1)%n])

        if i == 0:
            if B < a[i]:
                ans += 1
            continue

        if i == n-1:
            if A < a[i]:
                ans += 1
            continue

        lcm = (A * B)//math.gcd(A, B)
        if lcm < a[i]:
            ans += 1
    res.append(str(ans))

sys.stdout.write("\n".join(res))
        

"""
    Link: https://codeforces.com/problemset/problem/1454/D
    level : 1300
"""

import sys
tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
res = []
for _ in range(t):
    n = int(next(tokens))
    max_prime, max_factor = n, 1
    d = 2
    temp = n
    
    while d * d <= temp:
        if temp % d == 0:
            factor = 0
            while temp % d == 0:
                factor += 1
                temp //= d
            if factor > max_factor:
                max_prime = d
                max_factor = factor
        d += 1
    other_factor = n // (max_prime**max_factor)
    ans = [f"{max_prime}"] * (max_factor - 1) + [f"{max_prime*other_factor}"]
    res.append(f"{max_factor}")
    res.append(" ".join(ans))

sys.stdout.write("\n".join(res))
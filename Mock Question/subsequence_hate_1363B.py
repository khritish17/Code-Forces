"""
    https://codeforces.com/problemset/problem/1363/B
    Level: 1400
"""

import sys


tokens = iter(sys.stdin.read().strip().split())


t = int(next(tokens))
res = []
for _ in range(t):
    s = next(tokens)
    n = len(s)
    ones = [0] * n
    zeros = [0] * n

    for i, ele in enumerate(s):
        if ele == '1':
            ones[i] = 1
        
        if ele == '0':
            zeros[i] = 1
        
        ones[i] += ones[i - 1] if i - 1 >= 0 else 0
        zeros[i] += zeros[i - 1] if i - 1 >= 0 else 0
    
    ans = float('inf')
    for i in range(n):
        # for 000001111 pattern
        ans1 = (ones[i - 1] if i - 1 >= 0 else 0) + zeros[n - 1] - (zeros[i - 1] if i - 1 >= 0 else 0)
        ans2 = (zeros[i - 1] if i - 1 >= 0 else 0) + ones[n - 1] - (ones[i - 1] if i - 1 >= 0 else 0)
        ans = min(ans, ans1, ans2)
    res.append(str(ans))

sys.stdout.write("\n".join(res))


"""
    Link: https://codeforces.com/problemset/problem/1370/C
"""

import sys
import math

tokens = iter(sys.stdin.read().strip().split())

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(next(tokens))
ans = []
for _ in range(t):
    n = int(next(tokens))
    if n == 1:
        ans.append("FastestFinger")
    elif n == 2:
        ans.append("Ashishgup")
    elif n % 2 == 1:
        ans.append("Ashishgup")
    elif n % 2 == 0:
        if (n & (n -1)) == 0:
            ans.append("FastestFinger")
        else:
            if isPrime(n//2):
                ans.append("FastestFinger")
            else:
                ans.append("Ashishgup")

sys.stdout.write("\n".join(ans))




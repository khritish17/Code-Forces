"""
    Link: https://codeforces.com/problemset/problem/1538/C
"""
import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))

def count(n, arr, limit):
    lf, rt = 0, n - 1 
    res = 0
    while lf < rt:
        if arr[lf] + arr[rt] <= limit:
            res += rt - lf
            lf += 1
        else:
            rt -= 1
    return res

ans = []
for _ in range(t):
    n, l, r = int(next(tokens)), int(next(tokens)), int(next(tokens))
    a = [int(next(tokens)) for _ in range(n)]
    a.sort()
    ans.append(count(n, a, r) - count(n, a, l - 1))

ans = list(map(str, ans))
sys.stdout.write("\n".join(ans))
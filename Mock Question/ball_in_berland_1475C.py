"""
    Link: https://codeforces.com/problemset/problem/1475/C
"""

import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
def comb_nc2(n):
    return (n * (n - 1))//2

ans = []
for _ in range(t):
    a, b, k = int(next(tokens)), int(next(tokens)), int(next(tokens))
    boys = [int(next(tokens)) for _ in range(k)]
    girls = [int(next(tokens)) for _ in range(k)]

    freq_boys = [0] * (a + 1)
    freq_girls = [0] * (b + 1)

    for ele in boys:
        freq_boys[ele] += 1
    
    for ele in girls:
        freq_girls[ele] += 1
    
    total_pairs = comb_nc2(k)
    invalid_boys = 0
    invalid_girls = 0

    for ele in freq_boys:
        invalid_boys += comb_nc2(ele)

    for ele in freq_girls:
        invalid_girls += comb_nc2(ele)
    ans.append(str(total_pairs - invalid_boys - invalid_girls))

sys.stdout.write("\n".join(ans))
     
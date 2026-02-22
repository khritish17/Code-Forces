"""
    Link: https://codeforces.com/problemset/problem/1624/D
"""

import sys
tokens = iter(sys.stdin.read().strip().split())
ans = []
t = int(next(tokens))
for _ in range(t):
    n, k = int(next(tokens)), int(next(tokens))
    s = next(tokens)
    freq = [0] *26
    for ele in s:
        index = ord(ele) - ord('a')
        freq[index] += 1
    pairs = 0
    leftovers = 0
    for ele in freq:
        pairs += ele//2
        leftovers += ele%2
    length = (pairs//k)*2
    leftovers += (pairs%k)*2
    if leftovers >= k:
        length += 1
    ans.append(str(length))

sys.stdout.write("\n".join(ans))

    
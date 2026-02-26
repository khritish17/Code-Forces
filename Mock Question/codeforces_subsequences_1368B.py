"""
    Link: https://codeforces.com/problemset/problem/1368/B
"""

import sys

k = int(sys.stdin.read().strip())

subseq = "codeforces"
freq = [1] * 10
product = 1
i = 0
while product < k:
    product = product//freq[i]
    freq[i] += 1
    product = product * freq[i]
    i = (i + 1) % 10
ans = ""
for i in range(10):
    ele = subseq[i]
    f = freq[i]
    ans += "".join([ele] * f)

sys.stdout.write(ans)

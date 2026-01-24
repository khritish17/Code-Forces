"""
    Link: https://codeforces.com/problemset/problem/1490/F
"""

import sys

input_data = sys.stdin.read().split()
t = int(input_data[0])
i = 1

def solve(n, a):
    freq = {}
    for ele in a:
        if ele in freq:
            freq[ele] +=1
        else:
            freq[ele] = 1
    
    count = {}
    for f in freq.values():
        if f in count:
            count[f] += 1
        else:
            count[f] = 1
    
    ans = float('inf')
    for c, cnt in count.items():
        total = 0
        kept = 0
        for C, CNT in count.items():
            total += C*CNT
            if C >= c:
                kept += c * CNT
        delete = total - kept
        ans = min(ans, delete)
    return str(ans)


ans = []
for _ in range(t):
    n = int(input_data[i])
    i += 1
    a = list(map(int, input_data[i:i+n]))
    i += n
    ans.append(solve(n, a))
print("\n".join(ans))

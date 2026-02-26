"""
    Link: https://codeforces.com/problemset/problem/1535/C
    Level: 1400
"""
import sys

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))
ans = []

for _ in range(t):
    s = next(tokens)
    last_conflict = [-1, -1] # [starts with 0 pattern, starts with 1 pattern]
    count = 0
    for i in range(len(s)):
        ele = s[i]
        if ele != "?":
            ele = int(s[i])
            if ele != i % 2: # conflict with 0 start pattern
                last_conflict[0] = i
            if ele != (i + 1) % 2: # conflict with 1 start pattern
                last_conflict[1] = i
            
        length = max(i - last_conflict[0], i - last_conflict[1])
        count += length
    ans.append(str(count))

sys.stdout.write("\n".join(ans))



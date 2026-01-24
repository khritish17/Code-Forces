"""
    Docstring for special_elements_1352E
    Link: https://codeforces.com/problemset/problem/1352/E
"""

import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split(" ")))

    prefix = [a[0]]
    freq = [0] * (n + 1)
    freq[a[0]] += 1
    for ele in a[1:]:
        freq[ele] += 1
        prefix.append(ele + prefix[-1])
    
    ans = 0
    is_special = [False] * (n + 1)
    for i in range(n):
        for j in range(i + 1, n):
            sum_ = prefix[j] - (prefix[i - 1] if i - 1 >= 0 else 0)
            if sum_ > n:
                break
            else:
                is_special[sum_] = True
    
    for i,special in enumerate(is_special):
        if special:
            ans += freq[i]
    sys.stdout.write(f"{ans}\n")


    

"""
    Link: https://codeforces.com/problemset/problem/1551/B2
"""

import sys

def solve(n, k, a):
    indexes = {}
    for i, ele in enumerate(a):
        if ele in indexes:
            indexes[ele].append(i)
        else:
            indexes[ele] = [i]
    
    paintable_indexes = []
    M = 0
    for ele, indexs in indexes.items():
        fx = len(indexs)
        limit = min(k, fx)
        M += limit
        paintable_indexes += indexs[:limit]
    m = M//k
    total_paintable = m * k
    assigned_color = [0] * len(paintable_indexes)
    c = 1
    count = 0
    for i in range(len(paintable_indexes)):
        if count < total_paintable:
            assigned_color[i] = c
            count += 1
            c += 1
            if c > k:
                c = 1
        else:
            break
    ans = [str(0)] * n
    for i, ele in enumerate(paintable_indexes):
        ans[ele] = str(assigned_color[i])
    return " ".join(ans)


    
# def solve(n, k, a):
#     indexes = {}
#     M = 0
#     for i, ele in enumerate(a):
#         if ele in indexes and len(indexes[ele]) < k:
#             indexes[ele].append(i)
#         elif ele not in indexes:
#             indexes[ele] = [i]
    
#     for ele, indexs in indexes.items():
#         M += len(indexs)
    
#     m = M//k
#     total_paintable = m * k
#     count = 0
#     ans = ["0"] * n
#     c = 1
#     for ele, indexs in indexes.items():
#         for i in indexs:
#             if count < total_paintable:
#                 ans[i] = str(c)
#                 c += 1
#             if c > k:
#                 c = 1

#     return " ".join(ans)

input = sys.stdin.read().strip().split()
t = int(input[0])
i = 1

ans = []
for _ in range(t):
    n, k = map(int, input[i: i+ 2])
    i += 2
    a = list(map(int, input[i:i + n]))
    i += n
    ans.append(solve(n, k, a))

sys.stdout.write("\n".join(ans))

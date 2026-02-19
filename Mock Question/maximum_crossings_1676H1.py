"""
    Link: https://codeforces.com/problemset/problem/1676/H1
"""

import sys

class FenwickTree:
    def __init__(self, n):
        """
        Initialize a BIT for an array of size n.
        The internal tree is size n+1 to accommodate 1-based indexing.
        """
        self.tree = [0] * (n + 1)
        self.n = n

    def update(self, i, delta):
        """
        Adds delta to the element at index i (1-based).
        Complexity: O(log n)
        """
        while i <= self.n:
            self.tree[i] += delta
            # The bitwise magic: add the least significant bit
            i += i & (-i)

    def query(self, i):
        """
        Returns the prefix sum from index 1 to i (inclusive).
        Complexity: O(log n)
        """
        s = 0
        while i > 0:
            s += self.tree[i]
            # The bitwise magic: subtract the least significant bit
            i -= i & (-i)
        return s

    def query_range(self, left, right):
        """
        Returns the sum in the range [left, right].
        """
        if left > right:
            return 0
        return self.query(right) - self.query(left - 1)
    

tokens = iter(sys.stdin.read().strip().split())

t = int(next(tokens))

res = []
for _ in range(t):
    n = int(next(tokens))
    a = [int(next(tokens)) for _ in range(n)]
    
    ft = FenwickTree(n)
    ans = 0
    for ele in a:
        count = ft.query_range(ele, n)
        ans += count
        ft.update(ele, 1)
    res.append(ans)

res = list(map(str, res))
sys.stdout.write("\n".join(res))
    

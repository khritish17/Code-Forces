"""
    Docstring for chewbacca_and_number
    Link: https://codeforces.com/problemset/problem/514/A
"""

import sys


input = sys.stdin.readline

x = input().strip()

ans = 0

for i in range(len(x)):
    if i == 0 and x[i] == "9":
        ans = ans * 10 + 9
        continue
    digit = int(x[i])
    if 9 - digit >= digit:
        ans = ans * 10 + digit
    else:
        ans = ans * 10 + 9 - digit
print(ans) 



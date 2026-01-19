import sys

input = sys.stdin.readline

sit = input()
if "1111111" in sit or "0000000" in sit:
    print("YES")
else:
    print("NO")
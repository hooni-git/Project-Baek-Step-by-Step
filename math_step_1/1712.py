import sys

A, B, C = map(int, sys.stdin.readline().split())
ans = 0
all_money = A
revenue = 0

revenue = C - B

if revenue <= 0:
    print(-1)
else:
    ans = all_money // revenue
    print(ans+1)
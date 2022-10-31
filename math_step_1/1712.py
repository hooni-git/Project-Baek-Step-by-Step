import sys

A, B, C = map(int, sys.stdin.readline().split())
ans = 0
all_money = A
revenue = 0

revenue = C - B

ans = all_money // revenue

if revenue < 0:
    print(-1)
else:
    print(ans+1)
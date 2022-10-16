import sys

T = int(input())
result = []

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    result.append(a+b)

for n in range(len(result)):
    print("Case #%d:" %(n+1),result[n])
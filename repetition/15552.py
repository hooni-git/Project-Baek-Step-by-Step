import sys

T = int(input())
result = []

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    result.append(a+b)

for n in result:
    print(n)
import sys

T = int(input())
result = []
num_a = []
num_b = []

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    num_a.append(a)
    num_b.append(b)
    result.append(a+b)

for n in range(len(result)):
    print("Case #%d:" %(n+1), num_a[n], "+", num_b[n], "=", result[n])
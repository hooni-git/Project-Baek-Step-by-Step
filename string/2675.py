import sys

t = int(input())

str_in = [sys.stdin.readline().split() for _ in range(t)]

for i in range(t):
    for j in str_in[i][1]:
        print(j*int(str_in[i][0]), end='')
    print()
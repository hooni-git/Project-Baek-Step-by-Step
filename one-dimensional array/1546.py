import sys


T = int(input())
big = 0
num_all = 0

num = list(map(int, sys.stdin.readline().split()))

for i in num:
    if big < i:
        big = i

for n in num:
    n = n/big*100
    num_all = num_all + n

print(num_all/T)
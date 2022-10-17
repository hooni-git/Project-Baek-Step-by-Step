from operator import ilshift

T = int(input())
num_li = list(map(int, input().split()))
big = num_li[0]
small = num_li[0]

for i in num_li[1:]:
    if i > big:
        big = i
    elif i < small:
        small = i

print(small, big)
from itertools import count
from re import I


num = int(input())
result = 0

for i in range(num):
    i = i + 1
    result = result + i

print(result)
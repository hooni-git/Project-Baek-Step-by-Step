import sys

all_t, num_t = map(int, input().split())
data = list(map(int, sys.stdin.readline().split()))
data_re = []

for i in range(len(data)):
    if num_t > data[i]:
        data_re.append(data[i])
print(*data_re)
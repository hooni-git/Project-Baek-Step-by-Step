num_count = 0
N = int(input())
num_arr = list(map(int, input().split()))
num_find = int(input())

for n in num_arr:
    if n == num_find:
        num_count += 1

print(num_count)
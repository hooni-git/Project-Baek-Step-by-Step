num_org = set(range(1,10001))
num_com = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    num_com.add(i)

self_num = sorted(num_org - num_com)
for k in self_num:
    print(k)
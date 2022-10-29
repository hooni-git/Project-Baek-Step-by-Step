n = int(input())
num = input()
num_arry = []
ans = 0
for i in num:
    num_arry.append(int(i))

for j in range(len(num)):
    ans += num_arry[j]

print(ans)
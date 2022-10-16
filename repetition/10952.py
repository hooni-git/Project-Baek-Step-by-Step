n = 1
count = 0
result_num = []

while n != 0:
    num1, num2 = map(int, input().split())
    result_num.append(num1+num2)
    count = count + 1
    n = num1

for i in range(len(result_num)-1):
    print(result_num[i])
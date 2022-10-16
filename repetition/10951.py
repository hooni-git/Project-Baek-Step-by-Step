from pickle import TRUE

result_num = []

while TRUE:
    try:
        num1, num2 = map(int, input().split())
        result_num.append(num1+num2)
        n = num1
    except:
        break

for i in range(len(result_num)):
    print(result_num[i])
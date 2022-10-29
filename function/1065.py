def sequence(num):      #수를 입력받아서 등차수열인지 판단하는 함수
    num_arry = []
    for i in str(num):
        num_arry.append(int(i))
    if num < 10: # 1의 자리수 일때 공차 0 인 상수수열
        return True
    elif 10 <= num < 100:
        return True
    elif num_arry[0] - num_arry[1] == num_arry[1] - num_arry[2]:
        return True
    else:
        False

n = int(input())
ans_count = 0

for i in range(1, n+1):
    if sequence(i):
        ans_count += 1

print(ans_count)
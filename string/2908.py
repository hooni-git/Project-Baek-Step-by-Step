import sys

num1, num2 = sys.stdin.readline().split()

re_num1 = num1[::-1]
re_num2 = num2[::-1]

if re_num1 > re_num2:
    print(re_num1)
else:
    print(re_num2)
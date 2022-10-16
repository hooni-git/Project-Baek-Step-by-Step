t = int(input())
result = []

for num in range(0,t):
    a, b = map(int, input().split())
    result.append(a+b)

for i in result:
    print(i)
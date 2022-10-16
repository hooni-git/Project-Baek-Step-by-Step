price = int(input())
count = int(input())
p_price = []
p_count = []
result = 0

for i in range(count):
    a, b = map(int, input().split())
    p_price.append(a), p_count.append(b)

for i in range(0,count):
    result = p_count[i] * p_price[i] + result

if result == price:
    print("Yes")
else:
    print("No")
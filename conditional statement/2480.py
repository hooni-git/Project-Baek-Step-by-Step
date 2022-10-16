a, b, c = map(int, input().split())

if a==b:
    same = a
elif a==c:
    same = c
elif b==c:
    same = b

if a > b:
    if a > c:
        big = a
    else:
        big = c
elif b > c:
    big = b
else:
    big = c

if a==b==c:
    print(10000+a*1000)
elif a==b or a==c or b==c:
    print(1000+same*100)
else:
    print(big*100)
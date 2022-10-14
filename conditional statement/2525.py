h, m = map(int, input().split())
cook = int(input())

cook_h = (m+cook)//60
cook_m = (m+cook) % 60

if(m+cook) >= 60:
    if(h+cook_h) >= 24:
        h = h - 24
    h = h + cook_h
    print(h, cook_m)
else:
    if h >= 24:
        h = h -24
    print(h,cook_m)
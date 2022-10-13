H, M = map(int, input().split())

if  M - 45 < 0:
    M = (M - 45) + 60
    if H - 1< 0:
        H = 23
        print(H, M)
    else:
        print (H-1, M)
elif M >= 45:
    print(H, M-45)
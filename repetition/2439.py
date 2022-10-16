T = int(input())
n = 0
for i in range(T,0,-1):
    n = n + 1
    print("+"*(T-n)+"*"*n)
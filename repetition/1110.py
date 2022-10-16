from pickle import TRUE

T = input()
count = 0

if 10 > int(T):
    T = "0" + T
orginal_T = T

while TRUE:
    plus_num = int(T[0]) + int(T[1])

    if 10 > plus_num:
        plus_num_str = str(plus_num)
        T = T[1] + plus_num_str
    else:
        plus_num_str = str(plus_num)
        T = T[1] + plus_num_str[1]
    
    count += 1

    if T == orginal_T:
        break;

print(count)
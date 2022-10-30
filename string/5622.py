str_num = input()

num_str_arry = [[0,0,0],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]

dial_num = []
time = 0

for i in str_num:
    for j in range(9):
        if i in num_str_arry[j]:
            dial_num.append(j+1)

for k in dial_num:
    time += int(k)+1

print(time)
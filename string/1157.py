from string import ascii_lowercase
from string import ascii_uppercase

arry_alph1 = list(ascii_lowercase)
arry_alph2 = list(ascii_uppercase)

count_alph = [0] * 26
count_num = 0
remember_j = 0
big = 0
cnt = 0

sentence = input()

for i in sentence:
    for j in range(26):
        if i == arry_alph1[j] or i == arry_alph2[j]:
            count_num += 1
            remember_j = j
    count_alph[remember_j] = count_alph[remember_j] + count_num
    count_num = 0
    remember_j = 0

remember_j = count_alph.index(max(count_alph))

cnt = count_alph.count(count_alph[remember_j])

if cnt == 1:
    print(arry_alph2[remember_j])
else:
    print('?')
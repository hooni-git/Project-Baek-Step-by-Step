from string import ascii_lowercase

str_abc = input()
arry_abc = [-1] * 26
arry_alph = list(ascii_lowercase)
k = 0;

for i in range(len(str_abc)):
    for j in range(len(arry_alph)):
        if arry_abc[j] == -1:
            if str_abc[i] == arry_alph[j]:
                arry_abc[j] = k
    k += 1
print(*arry_abc)
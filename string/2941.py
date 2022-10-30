str_in = input()
croatia_alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia_alph:
    str_in = str_in.replace(i, '*')

print(len(str_in))
num_arry = []
big = 0; small = 0; count = 0

for i in range(9):
    num_arry.append(int(input()))

for n in num_arry:
    if n > big:
        big = n

for j in num_arry:
    count += 1
    if big == j:
        break
print(big)
print(count)
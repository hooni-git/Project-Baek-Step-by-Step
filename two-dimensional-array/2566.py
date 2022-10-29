matrix_o = [list(map(int, input().split())) for _ in range(9)]
big = 0
big_i = 0
big_j = 0

for i in range(9):
    for j in range(9):
        if big < matrix_o[i][j]:
            big = matrix_o[i][j]
            big_i = i
            big_j = j

print(big)
print(big_i+1, big_j+1)
A, B = [], []

N, M = map(int, input().split())

for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)
    
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()


    
for i in range(9):
    for j in range(9):
        if big < matrix_o[i][j]:
            big = matrix_o[i][j]
            big_i = i
            big_j = j

print(big)
print(big_i+1, big_j+1)
t = int(input())

data = list(input() for _ in range(t))

score = [0 for k in range(t)]
count_0 = 0

for i in range(t):
    for j in range(len(data[i])):
        if data[i][j] == 'O':
            count_0 += 1
            score[i] += count_0
        else:
            count_0 = 0
    count_0 = 0

for m in range(t):
    print(score[m])
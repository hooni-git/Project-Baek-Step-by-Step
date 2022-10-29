import sys
row = 0; col = 0;
confetti_width = 0
drawing_paper = [[0] * 100 for _ in range(100)]        #전제 도화지의 넓이

n = int(input())

confetti = [list(map(int, input().split())) for _ in range(n)] #입려받고 리스트롤 만들기

confetti_width_all = n * 100        #도화지에 붙는 색종이의 넓이

for _ in range(n):
    for i in range(10):
        for n in range(10):
            if drawing_paper[confetti[row][col]+i][confetti[row][col+1]+n] == 1:
                confetti_width += 1
            else:
                drawing_paper[confetti[row][col]+i][confetti[row][col+1]+n] = 1
    
    row += 1
    col = 0
print(confetti_width_all - confetti_width)
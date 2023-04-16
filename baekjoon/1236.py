## 성 지키기 ##
        
n, m = map(int,input().split())
board = []

for _ in range(n):
    board.append(input())

row, col = 0, 0


## X가 없는 행 갯수
for i in range(n):
    if "X" not in board[i]:
        row += 1
## X가 없는 열 갯수 
for j in range(m):
    if "X" not in [board[i][j] for i in range(n)]:
        col += 1

print(max(row ,col))
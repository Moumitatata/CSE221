N, M ,K = map(int,input().split())
board = []
for i in range(N+1):
    board.append(([0]*(M+1)))
knights_move = []

for i in range(K):
    x,y = map(int,input().split())
    board[x][y]= 1
    knights_move.append((x,y))

moves =  [
    (-2, -1), (-2, 1),   # 2 up, 1 left and right
(-1, -2), (-1, 2),    # 1 up, 2 left and also right
    (1, -2), (1, 2),     # 1 down, 2 left and right
    (2, -1), (2, 1)      # 2 down, 1 left / right
]

for x,y in knights_move:
    for dx,dy in moves:
        i,j = x+dx , y+dy

        if 1<=i<=N and 1<=j<=M:
            if board[i][j]==1:  #if theres 1 that means theres already a knight
                print("YES")
                exit()
print("NO")



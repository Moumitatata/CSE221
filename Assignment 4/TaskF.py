N = int(input())
x,y = map(int,input().split())

directions =  [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0), (1, 1)
]

moves = []

for i,j in directions :
    new_x = x+i
    new_y = y+ j

    if 1<= new_x<=N and 1<=new_y<=N:
        moves.append((new_x,new_y))

print(len(moves))

for i in moves:
    print(i[0],i[1])



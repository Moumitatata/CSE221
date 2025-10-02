N = int(input())

mat = [[0]*N for i in range(N)]

for i in range(N):
    line = list(map(int,input().split()))
    k = line[0]
    neighbor = line[1:]

    for j in neighbor:
        mat[i][j] = 1

for r in mat:
    print(*r)


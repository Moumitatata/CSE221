#TASK A
N, M = map(int, input().split())
matrix = [[0]* N for i in range(N)]

for j in range(M):
    ui, vi, wi = map(int, input().split())
    matrix[ui-1][vi-1] = wi  # -1 for 0-based indexing
for row in matrix:
    print(*row)

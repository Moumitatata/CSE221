from collections import deque 

N, M = map(int,input().split())
x = [[] for i in range(N+1)]

for i in range (M):
    u,v = map(int,input().split())
    x[u].append(v)
    x[v].append(u)

visited = [0]*(N+1)
q = deque([1])
visited[1] = 1
y = []

while q:
    u = q.popleft()
    y.append(u)
    for v in x[u]:
        if visited[v] == 0:
            visited[v] = 1
            q.append(v)
print(*y)


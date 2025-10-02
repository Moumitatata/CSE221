from collections import deque 

n,m,s,d = map(int,input().split())
u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))

x = [[] for _ in range(n+1)]
for i in range(m):
    u, v = u_list[i], v_list[i]
    x[u].append(v)
    x[v].append(u)

for i in range(1, n+1):
    x[i].sort()

# BFS
visited = [0]*(n+1)
parent = [0]*(n+1)
q = deque([s])
visited[s] = 1

while q:
    u = q.popleft()
    if u == d:  
        break
    for v in x[u]:
        if visited[v] == 0:
            visited[v] = 1
            parent[v] = u
            q.append(v)

if visited[d] == 0:
    print(-1)
else:
    path = []
    node = d
    while node != 0:
        path.append(node)
        node = parent[node]
    path.reverse()

    print(len(path)-1) 
    print(*path)
from collections import deque


N, M, S, D, K = map(int, input().split())
adj = [[] for i in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    adj[u].append(v) 

def bfs_path(start, end):
    visited = [0]*(N+1)
    parent = [0]*(N+1)
    q = deque([start])
    visited[start] = 1
    
    while q:
        u = q.popleft()
        if u == end:
            break
        for v in adj[u]:
            if visited[v] == 0:
                visited[v] = 1
                parent[v] = u
                q.append(v)
    
    if visited[end] == 0:
        return []
    

    path = []
    node = end
    while node != 0:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path

# Step 1: S -> K
path1 = bfs_path(S, K)
# Step 2: K -> D
path2 = bfs_path(K, D)

if not path1 or not path2:
    print(-1)
else:
    # merge paths, avoid duplicating K
    full_path = path1 + path2[1:]
    print(len(full_path)-1)
    print(*full_path)
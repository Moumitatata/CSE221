import sys
sys.setrecursionlimit(2*100000+5)

n , m = map(int,input().split())
u_list = list(map(int,input().split()))
v_list = list(map(int,input().split()))

adj = [[]for i in  range(n+1)]

for i in range(m):
    u, v = u_list[i], v_list[i]
    adj[u].append(v)
    adj[v].append(u)

visited = [0] * (n + 1)
dfs_order = []
stack = [1]

while stack:
    u = stack.pop()
    if visited[u] == 0 :
        visited[u] = 1
        dfs_order.append(u)
        
        for v in reversed(adj[u]):
            if visited[v] == 0:
                stack.append(v)
print(*dfs_order)
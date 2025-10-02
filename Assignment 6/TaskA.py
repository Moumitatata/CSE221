from collections import deque 

def solve():
    import sys 
    input = sys.stdin.readline 

    n,m = map(int,input().split())
    g = [[]for i in range(n+1)]
    indegree = [0]*(n+1)

    for i in range(m):
        x, y = map(int,input().split())
        g[x].append(y)
        indegree[y] +=1

    q = deque([i for i in range(1,n+1) if indegree[i]==0])
    topo = []
    while q:
            u = q.popleft()
            topo.append(u)
            for ver in g[u]:
                indegree[ver]-=1
                if indegree[ver] == 0:
                    q.append(ver)

    if len(topo) == n:
        print(*topo)
    else:
        print(-1 )
solve()

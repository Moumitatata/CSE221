from collections import deque
def solve():
    import sys
    input = sys.stdin.readline

    N, M, S, Q = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    sources = list(map(int, input().split()))
    destinations = list(map(int, input().split()))
    
    dist = [-1] * (N + 1)
    q = deque()
    for s in sources:
        dist[s] = 0
        q.append(s)

    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)

    result = [str(dist[d]) for d in destinations]
    print(*result)

solve()
